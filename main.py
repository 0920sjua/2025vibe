import streamlit as st
import os

# GPT 사용 가능 여부 확인
try:
    import openai
    api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
    if api_key:
        openai.api_key = api_key
        GPT_AVAILABLE = True
    else:
        GPT_AVAILABLE = False
except ModuleNotFoundError:
    GPT_AVAILABLE = False

# 페이지 설정
st.set_page_config(page_title="AI 글쓰기 도우미", page_icon="📝", layout="centered")
st.title("📝 AI 글쓰기 도우미")
st.caption("말투는 유지하고, 더 자연스럽게. 발표용 글 다듬기에 딱!")

# 스타일 선택
style = st.selectbox("원하는 느낌의 말투는?", ["자연스럽고 정중하게", "친근하지만 또렷하게", "공식 발표용으로 격식 있게"])

# 입력 받기
user_input = st.text_area("🗣️ 문장을 입력하세요", height=200, placeholder="예: 제가 이 발표를 준비하면서 느낀 점은...")

# 버튼
if st.button("✍️ 문장 다듬기"):
    if not user_input.strip():
        st.warning("문장을 입력해주세요.")
    elif not GPT_AVAILABLE:
        st.error("❌ GPT 기능이 설정되어 있지 않습니다.\n\nopenai 모듈을 설치하거나, secrets.toml에 OPENAI_API_KEY를 넣어주세요.")
    else:
        prompt = (
            f"다음 문장을 말투는 그대로 유지하면서 "
            f"{style} 표현으로 자연스럽게 고쳐줘. 거짓 정보는 절대 넣지 말고 문장만 다듬어줘.\n\n"
            f"원문:\n{user_input.strip()}\n\n수정된 문장:"
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
            )
            result = response.choices[0].message.content.strip()
            st.success("🪄 다듬어진 문장:")
            st.text_area("✏️ 결과", value=result, height=200, label_visibility="collapsed")
            st.download_button("📋 복사해서 저장", data=result, file_name="수정된문장.txt")
        except Exception as e:
            st.error(f"GPT 호출 중 오류 발생: {e}")
