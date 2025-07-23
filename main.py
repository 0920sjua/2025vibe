import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="광고 추천기", page_icon="📺")
st.title("📺 키워드 기반 광고 영상 보기")

# 간단한 키워드별 영상 매핑 사전
video_map = {
    "커피": "https://www.youtube.com/embed/1q-Lyzvhnm0",  # 맥심 모카골드 광고
    "햄버거": "https://www.youtube.com/embed/twY_FMDbAbE",  # 맥도날드 광고
    "운동화": "https://www.youtube.com/embed/ZTId2nZ33zQ",  # 나이키 광고
    "여행": "https://www.youtube.com/embed/FKfLrXHhRRI",  # 대한항공 광고
    "아이폰": "https://www.youtube.com/embed/c7nRTF2SowQ",  # Apple 광고
    "초콜릿": "https://www.youtube.com/embed/9RrgQb2FUhc",  # 가나 초콜릿 광고
}

# 입력 받기
keyword = st.text_input("광고를 보고 싶은 키워드를 입력하세요", placeholder="예: 커피, 운동화, 햄버거")

# 결과
if keyword:
    video_url = video_map.get(keyword.strip())

    if video_url:
        st.success(f"✅ '{keyword}' 관련 광고 영상입니다:")
        components.iframe(video_url, height=360)
    else:
        st.warning("😅 아직 이 키워드에 대한 광고 영상은 등록되지 않았어요.")
        st.info("예: 커피, 햄버거, 운동화, 여행, 아이폰, 초콜릿")
