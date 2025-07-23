import streamlit as st
import random
import time

# 🎰 심볼 목록과 확률 가중치
symbols = ["💎", "⭐", "🍒", "🍋", "🔔", "🍉"]
weights = [0.25, 0.25, 0.15, 0.15, 0.1, 0.1]  # 💎, ⭐ 확률을 높임

# 상태 초기화
if "board" not in st.session_state:
    st.session_state.board = random.choices(symbols, weights, k=6)
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "selected_symbol" not in st.session_state:
    st.session_state.selected_symbol = ""
if "spinning" not in st.session_state:
    st.session_state.spinning = False

st.set_page_config(page_title="6칸 잭팟 룰렛", page_icon="🎰")
st.title("🎰 잭팟 룰렛 (6칸)")
st.caption("룰렛을 돌리고 타이밍에 맞춰 멈춰보세요!")

# 보드 출력 함수
def draw_board(highlight_index):
    output = ""
    for i, symbol in enumerate(st.session_state.board):
        if i == highlight_index:
            output += f"➡️ **{symbol}** ⬅️\n"
        else:
            output += f"　　{symbol}　　  \n"
    return output

# 애니메이션 함수
def spin_animation():
    delays = [0.05] * 8 + [0.08] * 4 + [0.1] * 3 + [0.15] * 2 + [0.25]
    slot = st.empty()
    for delay in delays:
        st.session_state.current_index = (st.session_state.current_index + 1) % 6
        slot.markdown(draw_board(st.session_state.current_index))
        time.sleep(delay)
    return st.session_state.current_index

# 버튼
col1, col2 = st.columns(2)

with col1:
    if st.button("🎯 룰렛 돌리기"):
        st.session_state.board = random.choices(symbols, weights, k=6)
        st.session_state.spinning = True
        st.session_state.selected_symbol = ""
        idx = spin_animation()
        st.session_state.current_index = idx
        st.session_state.spinning = False

with col2:
    if st.button("🔄 다시하기"):
        st.session_state.board = random.choices(symbols, weights, k=6)
        st.session_state.current_index = 0
        st.session_state.selected_symbol = ""
        st.session_state.spinning = False

# 결과 출력
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
