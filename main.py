import streamlit as st
import openai
import os

# 🔐 OpenAI API 키 로딩
openai.api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI 글쓰기 도우미", page_icon="📝", layout="centered")
st.title("📝 AI 글쓰기 도우미")
st.caption("당신의 말투는 그대로, 더 자연스럽고 발표용으로 정리된 문장을 만들어드립니다.")

# 🔧 스타일 선택
style = st.selectbox("말투 유지 옵션", ["자연스럽고 정중하게", "친근하지만 또렷하게", "공식 발표용으로 격식 있게"])

# 🧾 입력 문장
user_input = st.text_area("🗣️ 문장을 입력하세요", placeholder="예: 저는 이 문제를 해결하기 위해 여러 방안을 생각했어요.", height=200)

# ✨ 결과 출력
if st.button("✍️ 문장 다듬기"):
    if not user_input.strip():
        st.warning("문장을 입력해주세요.")
    else:
        prompt = (
            f"다음 문장을 사용자의 말투는 최대한 그대로 유지하면서 "
            f"{style} 표현으로 더 자연스럽게 고쳐줘. 절대 새로운 정보는 넣지 말고, 문장을 바르게 다듬기만 해줘.\n\n"
            f"원문:\n{user_input.strip()}\n\n수정된 문장:"
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
            )
            result = response.choices[0].message.content.strip()
            st.success("🪄 다듬은 문장:")
            st.text_area("✏️ 결과", value=result, height=200, label_visibility="collapsed")
            st.download_button("📋 복사해서 쓰기", data=result, file_name="수정문장.txt")
        except Exception as e:
            st.error(f"GPT 호출 중 오류 발생: {e}")

