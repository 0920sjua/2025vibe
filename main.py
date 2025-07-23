import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="📺 광고 영상 추천기", page_icon="📺")
st.title("📺 키워드 기반 광고 영상 보기")
st.caption("단어를 입력하면 관련된 실제 광고 영상이 재생됩니다!")

# 안전하게 작동하는 YouTube embed 링크만 사용
video_map = {
    "커피": "https://www.youtube.com/embed/1q-Lyzvhnm0",  # 맥심 커피 광고
    "햄버거": "https://www.youtube.com/embed/twY_FMDbAbE",  # 맥도날드 광고
    "운동화": "https://www.youtube.com/embed/ZTId2nZ33zQ",  # 나이키 광고
    "제로콜라": "https://www.youtube.com/embed/XgtTzTLms0U",  # 코카콜라 제로
    "아이폰": "https://www.youtube.com/embed/c7nRTF2SowQ",  # iPhone 광고
    "에어팟": "https://www.youtube.com/embed/x3GczcT4PtI",  # AirPods Pro
    "갤럭시": "https://www.youtube.com/embed/8l8NcGtrnbg",  # Galaxy Fold
    "치킨": "https://www.youtube.com/embed/JY3ZBR2lY3Y",  # BBQ 광고
    "피자": "https://www.youtube.com/embed/BbgTz4tSYGs",  # 도미노 광고
    "라면": "https://www.youtube.com/embed/rIJoOa6x-rE",  # 신라면 광고
    "초콜릿": "https://www.youtube.com/embed/9RrgQb2FUhc",  # 가나초콜릿
    "여행": "https://www.youtube.com/embed/FKfLrXHhRRI",  # 대한항공
    "넷플릭스": "https://www.youtube.com/embed/Wfd0ZtAk3ag",  # Netflix 광고
    "스타벅스": "https://www.youtube.com/embed/Ea13UckUkoU",  # 스타벅스 광고
}

# 입력창
keyword = st.text_input("보고 싶은 광고 키워드를 입력하세요", placeholder="예: 커피, 햄버거, 넷플릭스")

# 결과 출력
if keyword:
    video_url = video_map.get(keyword.strip())
    if video_url:
        st.success(f"✅ '{keyword}' 광고 영상입니다:")
        components.iframe(video_url, height=360)
    else:
        st.warning("⚠️ 해당 키워드에 맞는 광고 영상이 아직 등록되지 않았어요.")
        st.info("예: 커피, 햄버거, 운동화, 아이폰, 에어팟, 갤럭시, 여행, 넷플릭스 등")

# FAQ
with st.expander("❓ 자주 묻는 질문 (FAQ)"):
    st.markdown("""
**Q. 영상이 안 나와요!**  
→ YouTube 재생을 위해 정확한 `embed` 링크를 사용해야 합니다. 위 예시 키워드를 사용해보세요.

**Q. 더 많은 키워드를 추가할 수 있나요?**  
→ 네! 원하시면 계속 추가해드릴 수 있어요.

**Q. 자동으로 찾아주는 건 되나요?**  
→ 지금은 수동 매핑 방식이지만, GPT 또는 YouTube API로 확장할 수 있습니다.
""")
