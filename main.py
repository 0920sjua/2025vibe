import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="광고 추천기", page_icon="📺")
st.title("📺 키워드 기반 광고 영상 보기")
st.caption("단어를 입력하면 그에 어울리는 광고 영상을 바로 보여드려요!")

# ✅ 1. 기본 딕셔너리 정의
video_map = {
    "커피": "https://www.youtube.com/embed/1q-Lyzvhnm0",
    "햄버거": "https://www.youtube.com/embed/twY_FMDbAbE",
    "운동화": "https://www.youtube.com/embed/ZTId2nZ33zQ"
}

# ✅ 2. 추가 키워드 등록 (NameError 방지됨)
video_map.update({
    "제로콜라": "https://www.youtube.com/embed/XgtTzTLms0U",
    "불닭볶음면": "https://www.youtube.com/embed/CvPb6p-5cds",
    "노션": "https://www.youtube.com/embed/I6O9v0e1pOc",
    "에어팟": "https://www.youtube.com/embed/x3GczcT4PtI",
    "갤럭시Z폴드": "https://www.youtube.com/embed/8l8NcGtrnbg",
    "넷플릭스": "https://www.youtube.com/embed/Wfd0ZtAk3ag"
    # ... 계속 추가 가능 ...
})

# 🔍 사용자 입력
keyword = st.text_input("보고 싶은 광고 키워드를 입력하세요", placeholder="예: 커피, 에어팟, 넷플릭스")

# 결과 보여주기
if keyword:
    video_url = video_map.get(keyword.strip())
    if video_url:
        st.success(f"✅ '{keyword}' 관련 광고 영상입니다:")
        components.iframe(video_url, height=360)
    else:
        st.warning("😅 해당 키워드는 아직 등록되어 있지 않아요.")
        st.info("예: 커피, 햄버거, 제로콜라, 넷플릭스, 에어팟 등")

# FAQ
with st.expander("❓ 자주 묻는 질문 (FAQ)"):
    st.markdown("""
**Q. 영상이 안 나와요!**  
→ 등록되지 않은 키워드일 수 있어요. '커피', '제로콜라', '에어팟' 등 입력해보세요.

**Q. 광고가 진짜예요?**  
→ 대부분 유튜브의 공식 브랜드 광고입니다.
""")
