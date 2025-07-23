import streamlit as st
import random
import pandas as pd
import os
from datetime import datetime

# GPT 기능 (선택)
try:
    import openai
    openai.api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
    GPT_AVAILABLE = openai.api_key is not None
except:
    GPT_AVAILABLE = False

# 동물 목록
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
