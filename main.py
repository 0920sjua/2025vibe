import streamlit as st
from urllib.parse import quote

st.set_page_config(page_title="YouTube 광고 링크 추천기", page_icon="📺")
st.title("🔗 키워드 기반 YouTube 광고 검색기")
st.caption("입력한 단어에 맞는 유튜브 광고 영상을 검색할 수 있도록 링크를 제공합니다.")

# 🔤 입력
keyword = st.text_input("광고를 보고 싶은 단어를 입력하세요", placeholder="예: 커피, 운동화, 뿡, 초콜릿, 아이폰").strip()

# ✅ 유튜브 검색 링크 생성
if keyword:
    search_query = quote(f"{keyword} 광고")
    youtube_link = f"https://www.youtube.com/results?search_query={search_query}"
    
    st.success(f"✅ '{keyword}' 관련 유튜브 광고를 검색하려면 아래 링크를 클릭하세요:")
    st.markdown(f"👉 [🔎 유튜브에서 '{keyword} 광고' 검색하기]({youtube_link})")
