import streamlit as st
import os

# GPT 가능 여부 확인
GPT_AVAILABLE = False
try:
    import openai
    api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
    if api_key:
        openai.api_key = api_key
        GPT_AVAILABLE = True
except ModuleNotFoundError:
    GPT_AVAILABLE = False

# 📱 Streamlit 앱 구성
st.set_page_config(page_title="AI 글쓰기 도우미", page_icon="📝", layout="centered")
st.title("📝 AI 글쓰기 도우미")
st.caption("말투는 그대로, 더 매끄럽고 정돈된 문장으로 바꿔드려요.")

# 🎨 스타일 옵션
style = st.selectbox("어떤 느낌으로 다듬을까요?", [
    "자연스럽고 정중하게",
    "친근하지만 또렷하게",
    "공식 발표용으로 격식 있게"
])

# ✍️ 문장 입력
user_input = st.text_area("🗣️ 문장을 입력하세요", height=200, placeholder="예: 저는 발표를 준비하면서 여러 가지 생각을 하게 되었어요.")

# 🧠 GPT 문장 수정 함수
def fix_text_with_gpt(text, style_description):
    prompt = (
        f"다음 문장을 사용자의 말투와 의도는 유지하면서 "
        f"{style_description} 표현으로 자연스럽게 고쳐줘. "
        f"절대 새로운 정보는 넣지 말고, 문장만 더 정돈되게 바꿔줘.\n\n"
        f"원문:\n{text.strip()}\n\n수정된 문장:"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 필요시 gpt-3.5-turbo로 바꿔도 됩니다
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT 오류: {str(e)}"

# 🚀 버튼 클릭 시 처리
if st.button("✍️ 문장 다듬기"):
    if not user_input.strip():
        st.warning("문장을 먼저 입력해주세요.")
    elif not GPT_AVAILABLE:
        st.error("❌ 현재 GPT 기능이 활성화되지 않았습니다. \n\n`.streamlit/secrets.toml`에 OPENAI_API_KEY를 설정하거나 환경변수로 추가해주세요.")
    else:
        with st.spinner("AI가 문장을 다듬는 중입니다..."):
            result = fix_text_with_gpt(user_input, style)
            st.success("🪄 다듬어진 문장:")
            st.text_area("✏️ 결과", value=result, height=200, label_visibility="collapsed")
            st.download_button("📋 복사해서 저장", data=result, file_name="수정된문장.txt")
