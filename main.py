import streamlit as st
import pandas as pd
import datetime
import time
import random

# -------------------------------
# cv2 불러오기 (없으면 기능 비활성)
# -------------------------------
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False

# -------------------------------
# 기본 설정
# -------------------------------
st.set_page_config(page_title="공부 타이머", page_icon="📚", layout="centered")

motivation_messages = [
    "조금만 더 하면 목표에 가까워집니다!",
    "집중은 최고의 무기입니다!",
    "오늘의 노력은 내일의 자신감!",
    "포기하지 말고 한 걸음 더!",
    "작은 습관이 큰 변화를 만듭니다.",
    "공부는 배신하지 않는다.",
    "쉬운 길 말고 옳은 길을 가자.",
    "이 시간은 다시 오지 않는다.",
    "남과 비교하지 말고 어제의 나와 비교하자.",
    "성공은 준비된 자의 것.",
    "끝까지 가면 이긴다.",
    "노력은 절대 헛되지 않는다.",
    "오늘도 성장 중!",
    "시작이 반이다.",
    "네가 포기하지 않는 한 끝난 게 아니다.",
    "조금 힘들면 성장하고 있다는 증거.",
    "하루하루 쌓아가자.",
    "오늘 공부는 내일의 자산.",
    "성실은 최고의 재능.",
    "불가능은 없다.",
    "끝까지 집중!",
    "목표는 멀어도 한 걸음씩.",
    "좋은 습관은 최고의 친구.",
    "오늘의 1시간이 미래의 1년을 만든다.",
    "지금의 너를 이겨라.",
    "집중하는 순간 불가능은 사라진다.",
    "실패는 성장의 일부다.",
    "꾸준함이 승리한다.",
    "노력 없이는 결과도 없다.",
    "조금 더, 단 10분만!"
]

subjects = ["수학", "영어", "정법", "국어", "한지", "생윤"]

# -------------------------------
# 공부 기록 불러오기/저장
# -------------------------------
def load_records():
    try:
        return pd.read_csv("study_records.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["날짜", "과목", "공부시간(분)"])

def save_record(subject, minutes):
    df = load_records()
    today = datetime.date.today().strftime("%Y-%m-%d")
    new_row = pd.DataFrame([[today, subject, minutes]], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("study_records.csv", index=False)

# -------------------------------
# 타이머 기능
# -------------------------------
if "running" not in st.session_state:
    st.session_state.running = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed_minutes" not in st.session_state:
    st.session_state.elapsed_minutes = 0
if "current_message" not in st.session_state:
    st.session_state.current_message = random.choice(motivation_messages)

subject = st.selectbox("공부할 과목을 선택하세요", subjects)

col1, col2 = st.columns(2)
if col1.button("▶ 시작"):
    st.session_state.running = True
    st.session_state.start_time = time.time()
if col2.button("⏹ 멈춤"):
    st.session_state.running = False
    if st.session_state.start_time:
        elapsed = (time.time() - st.session_state.start_time) / 60
        st.session_state.elapsed_minutes += elapsed
        save_record(subject, round(st.session_state.elapsed_minutes))
        st.success(f"{subject} {round(st.session_state.elapsed_minutes)}분 기록 저장 완료!")
        st.session_state.elapsed_minutes = 0

# -------------------------------
# 타이머 표시 + 동기부여 메시지 변경
# -------------------------------
if st.session_state.running:
    elapsed = (time.time() - st.session_state.start_time) / 60
    total_elapsed = st.session_state.elapsed_minutes + elapsed
    st.metric("공부 시간(분)", f"{int(total_elapsed)}")
    if int(total_elapsed) % 10 == 0:
        st.session_state.current_message = random.choice(motivation_messages)
    st.info(st.session_state.current_message)

# -------------------------------
# 기록 보기
# -------------------------------
st.markdown("### 📜 공부 기록")
st.dataframe(load_records())

# -------------------------------
# 얼굴 탐지 (cv2 있을 경우만)
# -------------------------------
if CV2_AVAILABLE:
    st.markdown("### 🙂 얼굴 감지 (집중도 체크)")
    img_file = st.camera_input("사진을 찍어주세요")
    if img_file is not None:
        file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        st.write(f"감지된 얼굴 수: {len(faces)}")
else:
    st.warning("⚠ OpenCV(cv2)가 설치되어 있지 않아 얼굴 감지 기능을 사용할 수 없습니다.")
