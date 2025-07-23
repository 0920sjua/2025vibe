import streamlit as st
import random
import pandas as pd
import os
from datetime import datetime

# GPT 사용 설정 (선택)
try:
    import openai
    openai.api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
    GPT_AVAILABLE = openai.api_key is not None
except ImportError:
    GPT_AVAILABLE = False
except Exception:
    GPT_AVAILABLE = False

# 동물 데이터베이스
animal_db = {
    "조용하고 온순한": ["고양이", "햄스터", "거북이", "토끼"],
    "활동적이고 사교적인": ["강아지", "앵무새", "페럿", "미어캣"],
    "유니크하고 독특한": ["도마뱀", "이구아나", "타란툴라", "고슴도치"],
    "아이들과 잘 지내는": ["골든리트리버", "푸들", "기니피그", "러시안블루"],
    "작은 공간에 적합한": ["물고기", "고슴도치", "햄스터", "거북이"]
}

FAV_FILE = "favorite_animals.csv"

# GPT 추천 함수
def get_gpt_animal(traits):
    if not GPT_AVAILABLE:
        return "❌ OpenAI API 키가 설정되지 않았습니다."
    try:
        prompt = f"다음 조건에 맞는 애완동물 하나만 추천해줘. 조건: {traits}. 이름만 간단하게 알려줘."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"GPT 오류: {str(e)}"

# Streamlit 앱 시작
st.set_page_config(page_title="오늘의 동물 추천", page_icon="🐾", layout="centered")
st.title("🐾 오늘 어떤 동물이 어울릴까?")
st.caption("당신의 성격, 환경에 맞는 동물을 추천해드려요!")

# 사용자 성향 입력
trait = st.selectbox("당신의 성향 또는 원하는 특징은?", list(animal_db.keys()))

# 두 추천 버튼 영역
col1, col2 = st.columns(2)

with col1:
    if st.button("🎲 랜덤 추천"):
        animal = random.choice(animal_db[trait])
        st.success(f"오늘의 추천 동물은 **{animal}** 입니다!")
        st.image(f"https://source.unsplash.com/600x400/?{animal}", caption=animal)

        if st.button("⭐ 즐겨찾기 추가", key=f"fav_{animal}"):
            fav_df = pd.DataFrame([[animal, datetime.now().strftime('%Y-%m-%d %H:%M')]],
                                  columns=["animal", "date"])
            if os.path.exists(FAV_FILE):
                fav_df.to_csv(FAV_FILE, mode='a', header=False, index=False)
            else:
                fav_df.to_csv(FAV_FILE, index=False)
            st.toast("즐겨찾기에 추가했어요!")

with col2:
    if st.button("🧠 GPT 추천 받기"):
        gpt_animal = get_gpt_animal(trait)
        if gpt_animal.startswith("❌") or gpt_animal.startswith("GPT 오류"):
            st.warning(gpt_animal)
        else:
            st.info(f"GPT 추천 동물은 **{gpt_animal}** 입니다!")
            st.image(f"https://source.unsplash.com/600x400/?{gpt_animal}", caption=gpt_animal)

            if st.button("⭐ 즐겨찾기 추가", key=f"fav_{gpt_animal}"):
                fav_df = pd.DataFrame([[gpt_animal, datetime.now().strftime('%Y-%m-%d %H:%M')]],
                                      columns=["animal", "date"])
                if os.path.exists(FAV_FILE):
                    fav_df.to_csv(FAV_FILE, mode='a', header=False, index=False)
                else:
                    fav_df.to_csv(FAV_FILE, index=False)
                st.toast("즐겨찾기에 추가했어요!")

# 즐겨찾기 보기
with st.expander("📂 즐겨찾기한 동물 보기"):
    if os.path.exists(FAV_FILE):
        fav_data = pd.read_csv(FAV_FILE)
        st.table(fav_data.tail(10))
    else:
        st.info("아직 즐겨찾기한 동물이 없어요!")
