import streamlit as st
from urllib.parse import quote
import streamlit.components.v1 as components

st.set_page_config(page_title="키워드 광고 보기", page_icon="📺")
st.title("📺 키워드 기반 광고 영상 보여주기")

# 사용자 단어 입력
keyword = st.text_input("광고를 보고 싶은 키워드를 입력하세요", placeholder="예: 커피, 운동화, 햄버거")

if keyword:
    # YouTube 검색 URL 생성
    search_query = quote(f"{keyword} 광고")
    youtube_search_url = f"https://www.youtube.com/results?search_query={search_query}"

    st.markdown(f"🔍 '{keyword}'에 대한 광고를 유튜브에서 검색 중...")

    # YouTube 임베드 - 첫 영상 예측 (동적 미리보기)
    st.markdown("👇 아래는 YouTube 검색 결과 페이지입니다.")
    components.iframe(youtube_search_url, height=600, scrolling=True)
