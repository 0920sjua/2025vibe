=import streamlit as st
import random
import pandas as pd
import os
from datetime import datetime
import openai

# 🎯 OpenAI API 키 설정 (환경변수 또는 직접 입력 가능)
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

# 🍱 메뉴 데이터베이스
menu_db = {
    "한식": ["김치찌개", "불고기", "비빔밥", "된장찌개", "제육볶음"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마파두부"],
    "일식": ["초밥", "라멘", "돈카츠", "우동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거"],
    "분식": ["떡볶이", "순대", "김밥", "튀김"],
    "디저트": ["빙수", "케이크", "아이스크림", "와플"]
}

# 즐겨찾기 CSV 파일 경로
FAV_FILE = "favorites.csv"

# ⏰ 현재 시간으로 식사 시간대 설정
hour = datetime.now().hour
if hour < 11:
    meal_time = "아침"
elif hour < 17:
    meal_time = "점심"
else:
    meal_time = "저녁"

# 🎨 페이지 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍽️", layout="centered")
st.title("🍽️ 오늘 뭐 먹지?")
st.caption(f"지금은 **{meal_time}** 시간이에요. 메뉴 고민은 그만!")

# 🧭 음식 카테고리 선택
category = st.selectbox("먹고 싶은 음식 종류를 골라보세요", ["전체"] + list(menu_db.keys()))

# ⭐️ GPT 추천 함수
def get_gpt_menu():
    prompt = f"지금은 {meal_time} 시간이야. 추천할 만한 한 끼 식사 메뉴 하나만 알려줘. 음식 이름만 간단하게 대답해줘."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"오류 발생: {e}"

# 🎲 추천 버튼
col1, col2 = st.columns(2)

with col1:
    if st.button("랜덤 메뉴 추천 🎲"):
        if category == "전체":
            all_menus = sum(menu_db.values(), [])
            menu = random.choice(all_menus)
        else:
            menu = random.choice(menu_db[category])
        st.success(f"👉 오늘의 추천 메뉴는 **{menu}** 어때요?")
        st.image(f"https://source.unsplash.com/600x400/?{menu}", caption=menu)

        if st.button("⭐ 즐겨찾기 추가", key=menu):
            fav_df = pd.DataFrame([[menu, datetime.now().strftime('%Y-%m-%d %H:%M')]], columns=["menu", "date"])
            if os.path.exists(FAV_FILE):
                fav_df.to_csv(FAV_FILE, mode='a', header=False, index=False)
            else:
                fav_df.to_csv(FAV_FILE, index=False)
            st.toast("즐겨찾기에 추가됐어요!")

with col2:
    if st.button("GPT에게 물어보기 🧠"):
        ai_menu = get_gpt_menu()
        st.info(f"🤖 GPT 추천 메뉴는 **{ai_menu}** 입니다!")
        st.image(f"https://source.unsplash.com/600x400/?{ai_menu}", caption=ai_menu)

        if st.button("⭐ 즐겨찾기 추가", key=ai_menu):
            fav_df = pd.DataFrame([[ai_menu, datetime.now().strftime('%Y-%m-%d %H:%M')]], columns=["menu", "date"])
            if os.path.exists(FAV_FILE):
                fav_df.to_csv(FAV_FILE, mode='a', header=False, index=False)
            else:
                fav_df.to_csv(FAV_FILE, index=False)
            st.toast("GPT 추천 메뉴가 즐겨찾기에 추가됐어요!")

# 📂 즐겨찾기 목록 보기
with st.expander("⭐ 내가 찜한 메뉴 보기"):
    if os.path.exists(FAV_FILE):
        fav_data = pd.read_csv(FAV_FILE)
        st.table(fav_data.tail(10))
    else:
        st.write("아직 즐겨찾기한 메뉴가 없어요!")

