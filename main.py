import streamlit as st
import random
import time

# 🎰 룰렛 심볼
symbols = ["🍒", "🍋", "🔔", "⭐", "🍉", "💎"]

# 보드 상태
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "board" not in st.session_state:
    st.session_state.board = [random.choice(symbols) for _ in range(10)]
if "spinning" not in st.session_state:
    st.session_state.spinning = False
if "animation_done" not in st.session_state:
    st.session_state.animation_done = False

# 페이지 설정
st.set_page_config(page_title="애니 룰렛", page_icon="🎰")
st.title("🎰 진짜 돌아가는 잭팟 룰렛")
st.caption("멈추기 타이밍을 잘 맞춰보세요! 돌아갑니다...")

# 룰렛 보드 출력 함수
def draw_board(highlight_index):
    board_output = ""
    for i, s in enumerate(st.session_state.board):
        if i == highlight_index:
            board_output += f"➡️ **{s}** ⬅️\n"
        else:
            board_output += f"　　{s}　　  \n"
    st.markdown(board_output)

# 룰렛 애니메이션 함수
def spin_animation():
    delays = [0.05] * 10 + [0.07] * 5 + [0.1] * 5 + [0.15] * 3 + [0.2] * 2 + [0.3]  # 점점 느려짐
    total_steps = len(delays)
    for i in range(total_steps):
        st.session_state.current_index = (st.session_state.current_index + 1) % 10
        draw_board(st.session_state.current_index)
        time.sleep(delays[i])
        st.experimental_rerun()

# 버튼 영역
col1, col2 = st.columns(2)

with col1:
    if not st.session_state.spinning and st.button("🎯 룰렛 돌리기"):
        st.session_state.spinning = True
        st.session_state.board = [random.choice(symbols) for _ in range(10)]
        st.session_state.animation_done = False
        spin_animation()

with col2:
    if st.session_state.spinning and st.button("🛑 멈추기"):
        st.session_state.spinning = False
        st.session_state.animation_done = True
        result = st.session_state.board[st.session_state.current_index]
        st.success(f"🎉 멈춘 심볼: **{result}**")

        if result == "💎":
            st.balloons()
            st.markdown("💎 **잭팟! 최고의 행운입니다!**")
        elif result == "⭐":
            st.markdown("⭐ **좋은 선택이에요!**")
        else:
            st.markdown("🙂 아쉽지만 다음 기회에!")

# 룰렛 보드 출력 (애니메이션 외)
if not st.session_state.spinning:
    draw_board(st.session_state.current_index)

# 다시하기
if st.button("🔄 다시하기"):
    st.session_state.spinning = False
    st.session_state.animation_done = False
    st.session_state.board = [random.choice(symbols) for _ in range(10)]
    st.session_state.current_index = 0
