import streamlit as st
import streamlit.components.v1 as components
from urllib.parse import quote

st.set_page_config(page_title="YouTube 광고 추천기", page_icon="📺")
st.title("📺 단어 기반 YouTube 광고 추천기")
st.caption("단어를 입력하면 관련된 광고 영상을 유튜브에서 찾아 보여드립니다!")

# 사용자 입력
keyword = st.text_input("광고를 보고 싶은 단어를 입력하세요", placeholder="예: 커피, 운동화, 뿡, 아이폰")

# 입력 처리
if keyword:
    query = quote(f"{keyword} 광고")
    youtube_search_url = f"https://www.youtube.com/results?search_query={query}"
    
    # 유튜브 자동 임베드 시도 (최상단 영상 예상 ID 미리 넣는 방식)
    # 기본 영상 매핑 (직접 확인한 ID들)
    fallback_videos = {
        "커피": "1q-Lyzvhnm0",
        "운동화": "ZTId2nZ33zQ",
        "아이폰": "c7nRTF2SowQ",
        "에어팟": "x3GczcT4PtI",
        "햄버거": "twY_FMDbAbE",
        "치킨": "JY3ZBR2lY3Y",
        "피자": "BbgTz4tSYGs",
        "제로콜라": "XgtTzTLms0U",
        "뿡": "rIJoOa6x-rE",   # 신라면 광고로 유머 처리
        "방구": "SaT7fTtyWxY", # 샴푸 광고 등 우회
    }

    video_id = fallback_videos.get(keyword.strip())

    if video_id:
        st.success(f"✅ '{keyword}' 관련 광고 영상입니다:")
        video_url = f"https://www.youtube.com/embed/{video_id}"
        components.iframe(video_url, height=360)
    else:
        st.warning("😅 정확한 광고 영상은 찾기 어려워요.")
        st.info(f"👉 [YouTube에서 직접 '{keyword} 광고' 검색하기]({youtube_search_url})")
        components.iframe(youtube_search_url, height=600, scrolling=True)
