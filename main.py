import streamlit as st
import random

st.set_page_config(page_title="한국사 이미지 퀴즈", layout="centered")
st.markdown("""
<h1 style='text-align: center;'>📚 <span style='background: linear-gradient(to bottom, red, blue); -webkit-background-clip: text; color: transparent;'>한국사</span> 1등급 맞기! 🏺🗡️</h1>
""", unsafe_allow_html=True)

quizzes = [
    {
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSV_VORmJQUsajxnnJ5u3axX2561gx-CW017A&s",
        "caption": "거북선 전체 모습",
        "question": "이순신이 탄 배의 이름은?",
        "options": ["바닥배", "겨울왕국의배", "용머리 배", "거북선"],
        "answer": "거북선",
        "explanation": "✅ 거북선은 이순신 장군님께서 타신 배의 이름입니다."
    },
    {
        "image_url": "https://i.namu.wiki/i/VwZNvG4mEd4yK_jmwrtUD14DoUWU2VvrmXQgs4jdVZdHW4NWWYq9xoGsRvnJ6-0W7eED3igHt56B5pqtx0t5Hw.webp",
        "caption": "강감찬 장군 초상화 (고려 귀주대첩)",
        "question": "귀주대첩은 어느 민족의 침입을 막은 전투였나요?",
        "options": ["몽골", "거란", "왜구", "여진"],
        "answer": "거란",
        "explanation": "✅ 고려의 강감찬 장군이 거란족을 물리친 전투입니다."
    },
    {
        "image_url": "https://cdn.edujin.co.kr/news/photo/202208/39617_80825_108.jpg",
        "caption": "이순신 장군 초상화",
        "question": "이순신 장군이 활약한 전쟁은 무엇인가요?",
        "options": ["병자호란", "임진왜란", "정묘호란", "신미양요"],
        "answer": "임진왜란",
        "explanation": "✅ 이순신 장군은 임진왜란 당시 수군을 이끌어 활약했습니다."
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/34/Seokguram_Buddha.jpg",
        "caption": "경주 석굴암 내부 불상",
        "question": "이 불상이 위치한 유적지는 어디인가요?",
        "options": ["불국사", "석굴암", "화엄사", "해인사"],
        "answer": "석굴암",
        "explanation": "✅ 석굴암은 경주의 불국사와 함께 유네스코 세계문화유산으로 지정된 석굴 사찰입니다."
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/df/Tripitaka_Koreana_Woodblocks.jpg",
        "caption": "팔만대장경 목판 (해인사 장경판전)",
        "question": "팔만대장경이 보관된 사찰은 어디인가요?",
        "options": ["통도사", "해인사", "불국사", "송광사"],
        "answer": "해인사",
        "explanation": "✅ 해인사는 팔만대장경이 보관된 장경판전으로 유명한 사찰입니다."
    }
]

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
    st.session_state.score = 0
    random.shuffle(quizzes)

if "next" not in st.session_state:
    st.session_state.next = False

if st.session_state.quiz_index < len(quizzes):
    q = quizzes[st.session_state.quiz_index]

    st.image(q["image_url"], caption=q["caption"], use_container_width=True)
    st.markdown("**질문:**")
    st.write(q["question"])

    choice = st.radio("답을 선택하세요:", q["options"], key=f"question_{st.session_state.quiz_index}")

    if st.button("제출하기", key=f"submit_{st.session_state.quiz_index}"):
        if choice == q["answer"]:
            st.success("정답입니다! " + q["explanation"])
            st.session_state.score += 1
        else:
            st.error(f"오답입니다. ❌ 정답: {q['answer']}\n\n{q['explanation']}")

        st.session_state.quiz_index += 1
        st.session_state.next = True

if st.session_state.next:
    st.session_state.next = False
    st.experimental_rerun()

if st.session_state.quiz_index >= len(quizzes):
    st.write("---")
    st.subheader(f"🎉 퀴즈 종료! 총 점수: {st.session_state.score} / {len(quizzes)}")
    if st.button("처음부터 다시 시작하기"):
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        random.shuffle(quizzes)
        st.experimental_rerun()

st.write("---")
st.markdown("더 많은 역사 이미지 퀴즈를 계속 추가해드릴까요? 🏯")
