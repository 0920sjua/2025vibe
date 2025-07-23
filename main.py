import streamlit as st
import openai

st.set_page_config(page_title="이슈 대응 도우미", page_icon="🧠")
st.title("🧠 키워드 기반 이슈 대처 가이드 & 역사적 배경")

# 🔑 OpenAI API 키 입력
openai.api_key = st.secrets["OPENAI_API_KEY"]  # .streamlit/secrets.toml 필요

keyword = st.text_input("이슈나 키워드를 입력하세요", placeholder="예: 폭염, 전쟁, 방사능, 바이러스, AI, 뿡")

if keyword:
    with st.spinner("AI가 정보를 정리 중입니다..."):
        prompt = f"""
사용자가 '{keyword}'라는 단어를 입력했습니다.  
이 단어와 관련된 아래 내용을 3단으로 짧고 정확하게 요약해줘:

1. 간단한 설명 (한두 문장)
2. 실용적인 대처법 또는 행동 요령
3. 역사적 배경 또는 이전 사례 (있다면)

말투는 친절하고, 가볍게 알려주는 뉴스처럼 써줘.
"""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content.strip()
        st.success(f"✅ '{keyword}' 관련 정보")
        st.markdown(result)
