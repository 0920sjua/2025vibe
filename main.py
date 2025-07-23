import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="키워드 광고/웹 추천기", page_icon="🔍")
st.title("🔍 단어 기반 광고 또는 공식 웹사이트 추천기")
st.caption("단어를 입력하면 광고 영상 또는 관련된 공식 웹사이트를 추천해드립니다!")

# ✅ 광고 키워드 DB (영상 또는 사이트 링크)
keyword_map = {
    # 명확한 광고 매핑
    "커피": "https://www.starbucks.co.kr/",
    "햄버거": "https://www.mcdonalds.co.kr/kor/main.do",
    "치킨": "https://www.bbq.co.kr/",
    "피자": "https://www.dominos.co.kr/",
    "라면": "https://www.nongshim.com/",
    "아이폰": "https://www.apple.com/kr/iphone/",
    "갤럭시": "https://www.samsung.com/sec/smartphones/",
    "에어팟": "https://www.apple.com/kr/airpods/",
    "운동화": "https://www.nike.com/kr/",
    "초콜릿": "https://www.lotteconf.co.kr/",
    "자동차": "https://www.hyundai.com/kr/ko",
    "여행": "https://www.agoda.com/ko-kr",
    "호텔": "https://www.hotelscombined.co.kr/",
    "배달": "https://www.baemin.com/",
    "콜라": "https://www.coca-cola.co.kr/",
    "스타벅스": "https://www.starbucks.co.kr/",
    
    # ✅ 유머/유사 확장 키워드
    "뿡": "https://www.toto.co.kr/",  # 변기 브랜드
    "방구": "https://www.lgcare.com/product/air_freshener",  # 방향제
    "화장실": "https://www.kyowon.co.kr/business/housing/",
    "냄새": "https://www.febreze.co.kr/",  # 페브리즈
    "변기": "https://www.insaengmall.co.kr/",  # 변기 리모델링
    "방향제": "https://www.ambipur.co.kr/",
    "탈취제": "https://www.gmarket.co.kr/n/product?keyword=탈취제"
}

# 🔤 사용자 입력
keyword = st.text_input("단어를 입력하세요 (예: 커피, 뿡, 방구, 햄버거, 아이폰)").strip()

if keyword:
    url = keyword_map.get(keyword)
    
    if url:
        st.success(f"✅ '{keyword}' 관련 추천 링크입니다:")
        st.markdown(f"👉 [클릭해서 이동하기]({url})")
        # 웹사이트 임베드 (일부만 iframe 허용)
        if "youtube.com/embed" in url:
            components.iframe(url, height=360)
        else:
            st.info("웹사이트로 이동합니다. 새 창에서 여는 것이 더 좋을 수 있어요.")
    else:
        st.warning("🔍 아직 등록되지 않은 단어예요.")
        st.info("예: 커피, 뿡, 콜라, 라면, 운동화, 방구, 변기, 호텔 등")

# 💬 FAQ
with st.expander("❓ 자주 묻는 질문"):
    st.markdown("""
**Q. 이상한 단어 넣어도 되나요?**  
→ 네! "뿡", "방구", "냄새"처럼 유머 있는 단어도 알아듣고 관련 제품으로 연결해드려요.

**Q. 왜 영상 대신 사이트가 나오나요?**  
→ 일부 환경에서는 YouTube 영상이 막히거나 느려서, 확실히 열리는 공식 웹사이트를 대신 추천해드립니다.

**Q. 내가 원하는 단어를 추가할 수 있나요?**  
→ 물론입니다! 다음 버전에 반영하거나 자동 검색 기능도 넣을 수 있어요.
""")
