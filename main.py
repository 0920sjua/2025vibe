import streamlit as st
import random
import time

# 🎲 슬롯 심볼
symbols = ["🍒", "🍋", "🔔", "⭐", "🍉", "💎"]

# 잭팟 판 (10칸짜리)
jackpot_board = [random.choice(symbols) for _ in range(10)]

# 💰 포인트 시스템
if 'points' not in st.session_state:
    st.session_state.points = 100

# 슬롯 위치 상태
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

if 'spinning' not in st.session_state:
    st.session_state.spinning = False

st.set_page_config(page_title="잭팟 룰렛 게임", page_icon="🎰")
st.title("🎰 고퀄 잭팟 룰렛")
st.caption("타이밍 맞춰 정지 버튼을 눌러 잭팟을 맞춰보세요!")

st.markdown(f"### 💰 현재 포인트: `{st.session_state.points}`")

# 게임판 출력
def draw_board(selected_index=None):
    board_visual = ""
    for i, symbol in enumerate(jackpot_board):
        if i == selected_index:
            board_visual += f"➡️ **{symbol}** ⬅️  \n"
        else:
            board_visual += f"　　{symbol}　　  \n"
    st.markdown(board_visual)

draw_board(st.session_state.current_index)

# ▶️ 돌리기 버튼
col1, col2 = st.columns(2)

with col1:
    if not st.session_state.spinning and st.button("🎯 룰렛 시작하기 (-10 포인트)"):
        if st.session_state.points < 10:
            st.warning("포인트가 부족해요!")
        else:
            st.session_state.spinning = True
            st.session_state.points -= 10

            # 보드 초기화
            jackpot_board[:] = [random.choice(symbols) for _ in range(10)]

            # 간단한 "회전 애니메이션"
            for i in range(15):
                st.session_state.current_index = i % 10
                draw_board(st.session_state.current_index)
                time.sleep(0.1)
                st.experimental_rerun()

with col2:
    if st.session_state.spinning and st.button("🛑 멈추기"):
        st.session_state.spinning = False
        selected = jackpot_board[st.session_state.current_index]
        st.success(f"멈춘 심볼은: **{selected}**")

        # 결과 평가
        if selected == "💎":
            st.balloons()
            st.markdown("🎉 **잭팟! 💎 100포인트 획득!**")
            st.session_state.points += 100
        elif selected == "⭐":
            st.markdown("✨ **꽤 좋은 선택! ⭐ 30포인트 획득!**")
            st.session_state.points += 30
        else:
            st.markdown("😅 아쉽지만 꽝이에요!")

        # 다음 게임을 위해 인덱스 초기화
        st.session_state.current_index = 0

# 🔄 포인트 초기화
if st.button("🔄 포인트 초기화"):
    st.session_state.points = 100
    st.session_state.current_index = 0
    st.success("포인트가 100으로 초기화됐어요!")
