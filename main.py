import streamlit as st
import random
import time

# 🎲 슬롯 심볼
symbols = ["🍒", "🍋", "🔔", "⭐", "🍉", "💎"]

# 💰 기본 포인트
if 'points' not in st.session_state:
    st.session_state.points = 100

# 🎨 페이지 구성
st.set_page_config(page_title="잭팟 룰렛 게임", page_icon="🎰", layout="centered")
st.title("🎰 잭팟 룰렛")
st.caption("운을 시험해보세요! 버튼을 눌러 룰렛을 돌려보세요.")

# 📊 포인트 표시
st.markdown(f"### 💰 보유 포인트: `{st.session_state.points}`")

# 버튼
if st.button("🎯 룰렛 돌리기 (10포인트 소모)"):
    if st.session_state.points < 10:
        st.warning("포인트가 부족해요!")
    else:
        st.session_state.points -= 10

        with st.spinner("돌리는 중..."):
            time.sleep(1.5)
            result = [random.choice(symbols) for _ in range(3)]
            st.markdown(f"## {' | '.join(result)}")

        # 결과 분석
        if result[0] == result[1] == result[2]:
            st.success("🎉 잭팟! 100포인트 획득!")
            st.session_state.points += 100
        elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            st.info("😊 두 개 일치! 30포인트 획득!")
            st.session_state.points += 30
        else:
            st.write("🙃 꽝이에요! 다시 도전해보세요.")

# 리셋 버튼
if st.button("🔄 포인트 초기화"):
    st.session_state.points = 100
    st.success("포인트가 100으로 초기화됐어요.")
