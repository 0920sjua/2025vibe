import streamlit as st
import random
import time

# 🎰 심볼 목록
symbols = ["🍒", "🍋", "🔔", "⭐", "🍉", "💎"]

# 잭팟 보드 및 상태 초기화
if "jackpot_board" not in st.session_state:
    st.session_state.jackpot_board = [random.choice(symbols) for _ in range(10)]

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "spinning" not in st.session_state:
    st.session_state.spinning = False

st.set_page_config(page_title="잭팟 룰렛", page_icon="🎰")
st.title("🎰 타이밍 잭팟 룰렛")
st.caption("회전 중에 '🛑 멈추기' 버튼을 눌러 잭팟을 노려보세요!")

# 보드 출력 함수
def draw_board(selected_index=None):
    board_output = ""
    for i, symbol in enumerate(st.session_state.jackpot_board):
        if i == selected_index:
            board_output += f"➡️ **{symbol}** ⬅️\n"
        else:
            board_output += f"　　{symbol}　　  \n"
    st.markdown(board_output)

draw_board(st.session_state.current_index)

# 돌리기 버튼
col1, col2 = st.columns(2)

with col1:
    if not st.session_state.spinning and st.button("🎯 룰렛 시작"):
        st.session_state.spinning = True
        st.session_state.jackpot_board = [random.choice(symbols) for _ in range(10)]

        # 회전 효과
        for _ in range(20):
            st.session_state.current_index = (st.session_state.current_index + 1) % 10
            draw_board(st.session_state.current_index)
            time.sleep(0.1)

        st.success("🌀 룰렛이 회전 중입니다! 이제 멈춰보세요.")

with col2:
    if st.session_state.spinning and st.button("🛑 멈추기"):
        st.session_state.spinning = False
        selected_symbol = st.session_state.jackpot_board[st.session_state.current_index]
        st.success(f"🎉 멈춘 위치: **{selected_symbol}**")

        # 결과 메시지
        if selected_symbol == "💎":
            st.balloons()
            st.markdown("💎 **잭팟! 최고의 행운입니다!**")
        elif selected_symbol == "⭐":
            st.markdown("⭐ **좋은 선택이에요!**")
        else:
            st.markdown("🙂 아쉽지만 다음 기회를!")

# 다시하기 버튼
if st.button("🔄 다시하기"):
    st.session_state.jackpot_board = [random.choice(symbols) for _ in range(10)]
    st.session_state.current_index = 0
    st.session_state.spinning = False
