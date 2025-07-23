import streamlit as st
import random
import time

# 🎰 심볼
symbols = ["🍒", "🍋", "🔔", "⭐", "🍉", "💎"]

# 상태 초기화
if "board" not in st.session_state:
    st.session_state.board = [random.choice(symbols) for _ in range(10)]
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "selected_symbol" not in st.session_state:
    st.session_state.selected_symbol = ""
if "spinning" not in st.session_state:
    st.session_state.spinning = False

st.set_page_config(page_title="룰렛 잭팟", page_icon="🎰")
st.title("🎰 고퀄 잭팟 룰렛")
st.caption("멈추기 버튼을 눌러 타이밍 맞춰 잭팟을 노려보세요!")

# 룰렛 보드 시각화 함수
def draw_board(highlight_index):
    board_output = ""
    for i, symbol in enumerate(st.session_state.board):
        if i == highlight_index:
            board_output += f"➡️ **{symbol}** ⬅️\n"
        else:
            board_output += f"　　{symbol}　　  \n"
    return board_output

# 룰렛 애니메이션 함수 (rerun 없이 placeholder 사용)
def spin_animation():
    delays = [0.05] * 10 + [0.07] * 5 + [0.1] * 5 + [0.15] * 3 + [0.2] * 2 + [0.3]
    slot = st.empty()  # placeholder
    for delay in delays:
        st.session_state.current_index = (st.session_state.current_index + 1) % 10
        board_display = draw_board(st.session_state.current_index)
        slot.markdown(board_display)
        time.sleep(delay)
    return st.session_state.current_index

# 🎯 룰렛 시작 버튼
col1, col2 = st.columns(2)

with col1:
    if st.button("🎯 룰렛 돌리기"):
        st.session_state.board = [random.choice(symbols) for _ in range(10)]
        st.session_state.spinning = True
        st.session_state.selected_symbol = ""
        index = spin_animation()
        st.session_state.current_index = index
        st.session_state.spinning = False

# 🛑 멈추기 버튼 (타이밍 멈추기 아님 — 대신 자동으로 멈춤)
with col2:
    if st.session_state.selected_symbol:
        st.success(f"멈춘 결과: {st.session_state.selected_symbol}")

# 정지 후 결과 출력
if not st.session_state.spinning and st.session_state.board:
    index = st.session_state.current_index
    symbol = st.session_state.board[index]
    st.session_state.selected_symbol = symbol
    st.markdown("🎯 최종 결과:")
    st.markdown(draw_board(index))
    
    if symbol == "💎":
        st.balloons()
        st.success("💎 **잭팟! 최고의 행운입니다!**")
    elif symbol == "⭐":
        st.info("⭐ **좋은 선택이에요!**")
    else:
        st.write("🙂 아쉽지만 다음 기회를!")

# 다시하기
if st.button("🔄 다시하기"):
    st.session_state.board = [random.choice(symbols) for _ in range(10)]
    st.session_state.current_index = 0
    st.session_state.selected_symbol = ""
    st.session_state.spinning = False
