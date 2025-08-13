import streamlit as st
import cv2
import time
import numpy as np
import random
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="공부 타이머 & 집중도 기록", page_icon="📚", layout="wide")
st.title("📚 공부 타이머 & 집중도 기록")

# =====================
# 동기부여 문구 30개
# =====================
motivations = [
    "🚀 지금 이 순간이 당신의 미래를 만든다!",
    "🔥 포기하지 않는 한, 실패는 없다!",
    "🌱 작은 습관이 큰 변화를 만든다.",
    "💪 오늘의 땀방울이 내일의 성취다.",
    "🎯 목표를 향해 한 걸음 더!",
    "📚 꾸준함이 최고의 무기다.",
    "🏆 노력은 배신하지 않는다.",
    "🌟 당신은 생각보다 훨씬 강하다.",
    "⏳ 완벽한 순간을 기다리지 말고 지금 시작하라.",
    "⚡ 기회는 준비된 자에게 온다.",
    "📖 오늘 배우는 것이 내일의 무기가 된다.",
    "🚴‍♂️ 천천히 가도 멈추지 않으면 된다.",
    "🧠 집중은 최고의 생산성 도구다.",
    "🌞 하루의 첫 1시간이 하루 전체를 만든다.",
    "🛠️ 꾸준함은 재능을 이긴다.",
    "🌊 파도는 멈추지 않는다. 너도 멈추지 마라.",
    "🔥 지금의 선택이 미래를 만든다.",
    "🎵 작은 진전도 진전이다.",
    "🌻 오늘 심은 씨앗은 내일 꽃이 된다.",
    "🏃‍♀️ 시작이 반이다.",
    "🧗 도전 없이는 성장도 없다.",
    "📅 오늘을 최선을 다해 살아라.",
    "🕰️ 시간이 부족한 게 아니라, 우선순위가 문제다.",
    "🪴 하루하루가 쌓여 인생이 된다.",
    "⚙️ 실패는 시도했다는 증거다.",
    "🌟 불가능은 단지 시간이 더 필요한 것뿐이다.",
    "💡 배움은 평생의 자산이다.",
    "🚪 문이 닫히면 다른 문을 찾아라.",
    "🌍 작은 변화가 세상을 바꾼다.",
    "💖 자신을 믿는 것이 시작이다."
]

# =====================
# 공부 기록 불러오기
# =====================
RECORD_FILE = "study_record.csv"
if os.path.exists(RECORD_FILE):
    records_df = pd.read_csv(RECORD_FILE)
else:
    records_df = pd.DataFrame(columns=["날짜", "과목", "공부시간(분)", "집중도(%)"])

# =====================
# 과목 선택 & 공부 시간 입력
# =====================
subject = st.selectbox("📖 공부할 과목 선택", ["수학", "영어", "정법", "국어", "한지", "생윤"])
study_minutes = st.number_input("공부 시간(분)", min_value=1, value=25)
break_minutes = st.number_input("휴식 시간(분)", min_value=1, value=5)

if "focus_score" not in st.session_state:
    st.session_state.focus_score = 0
if "frames_checked" not in st.session_state:
    st.session_state.frames_checked = 0

start_button = st.button("타이머 시작")

# =====================
# 타이머 실행
# =====================
if start_button:
    st.write(f"📚 '{subject}' 공부 시작!")
    end_time = time.time() + (study_minutes * 60)
    last_motivation_time = time.time()
    current_motivation = random.choice(motivations)

    camera = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    placeholder_timer = st.empty()
    placeholder_focus = st.empty()
    placeholder_motivation = st.empty()

    while time.time() < end_time:
        ret, frame = camera.read()
        if not ret:
            st.error("카메라를 불러올 수 없습니다.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        st.session_state.frames_checked += 1
        if len(faces) > 0:
            st.session_state.focus_score += 1

        # 타이머 표시
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        placeholder_timer.subheader(f"남은 공부 시간: {minutes:02}:{seconds:02}")

        # 집중도 표시
        focus_percent = (st.session_state.focus_score / st.session_state.frames_checked) * 100
        placeholder_focus.progress(int(focus_percent))
        placeholder_focus.write(f"집중도: {focus_percent:.1f}%")

        # 10분마다 동기부여 문구 변경
        if time.time() - last_motivation_time >= 600:
            current_motivation = random.choice(motivations)
            last_motivation_time = time.time()

        placeholder_motivation.markdown(f"### 💡 {current_motivation}")

        time.sleep(1)

    camera.release()
    st.success("⏰ 공부 세션 종료!")

    # =====================
    # 기록 저장
    # =====================
    today = datetime.now().strftime("%Y-%m-%d")
    total_focus = (st.session_state.focus_score / st.session_state.frames_checked) * 100
    new_record = pd.DataFrame([[today, subject, study_minutes, round(total_focus, 1)]],
                              columns=["날짜", "과목", "공부시간(분)", "집중도(%)"])
    records_df = pd.concat([records_df, new_record], ignore_index=True)
    records_df.to_csv(RECORD_FILE, index=False)

    st.write("📄 오늘 기록이 저장되었습니다!")
    st.dataframe(records_df)
