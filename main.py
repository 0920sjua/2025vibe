import streamlit as st
import random

st.set_page_config(page_title="한국사 이미지 퀴즈", layout="centered")
st.title("🖼️ 깜짝! 한국사국사 퀴즈")

quizzes = [
    {
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSV_VORmJQUsajxnnJ5u3axX2561gx-CW017A&s",
        "caption": "거북선 전체 모습",
        "question": "이순신이 탄 배의 이름은?",
        "options": ["바닥배", "겨울왕국의배", "용머리 배","거북선"],
        "answer": "거북선",
        "explanation": "✅ 거북선은 이순신 장군님께서 타신 배의이름입니다"
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
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/47/Suwon_Hwaseong.jpg",
        "caption": "수원 화성",
        "question": "수원 화성을 축조한 조선의 왕은 누구인가요?",
        "options": ["세종", "정조", "태조", "영조"],
        "answer": "정조",
        "explanation": "✅ 정조는 아버지 사도세자를 기리기 위해 수원 화성을 건설했습니다."
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Jang_Bogo.jpg",
        "caption": "장보고 장군 초상화",
        "question": "장보고는 어느 시대의 인물인가요?",
        "options": ["고구려", "백제", "신라", "고려"],
        "answer": "신라",
        "explanation": "✅ 장보고는 신라 중대 해상무역과 해군력을 장악한 인물입니다."
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/86/King_Sejong_statue_in_Gwanghwamun_Square.jpg",
        "caption": "세종대왕 동상 (광화문 광장)",
        "question": "세종대왕이 만든 문자는 무엇인가요?",
        "options": ["훈민정음", "이두문", "향찰", "가림토"],
        "answer": "훈민정음",
        "explanation": "✅ 세종대왕은 백성을 위해 훈민정음을 창제했습니다."
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Hong_Gyeongnae.jpg",
        "caption": "홍경래의 난 지도와 설명",
        "question": "홍경래의 난은 어느 왕의 시기에 일어났나요?",
        "options": ["정조", "순조", "영조", "헌종"],
        "answer": "순조",
        "explanation": "✅ 홍경래의 난은 조선 후기 순조 대에 발생한 민란입니다."
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Daehan_Jeonggukgi.jpg",
        "caption": "대한제국 국기 (태극기 초기형)",
        "question": "대한제국을 선포한 조선의 황제는 누구인가요?",
        "options": ["고종", "순종", "흥선대원군", "철종"],
        "answer": "고종",
        "explanation": "✅ 고종은 1897년 대한제국을 선포하고 황제에 즉위했습니다."
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/90/Independence_Gate.jpg",
        "caption": "독립문",
        "question": "독립문은 어떤 나라로부터의 자주독립을 상징하나요?",
        "options": ["청나라", "일본", "미국", "러시아"],
        "answer": "청나라",
        "explanation": "✅ 독립문은 청나라 간섭에서 벗어나 자주를 선언한 상징물입니다."
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/fd/Yuji_Sohn_1909.jpg",
        "caption": "안중근 의사 초상화",
        "question": "안중근 의사가 처단한 인물은 누구인가요?",
        "options": ["이토 히로부미", "도요토미 히데요시", "고노에 후미마로", "요시다 쇼인"],
        "answer": "이토 히로부미",
        "explanation": "✅ 안중근 의사는 하얼빈에서 이토 히로부미를 처단했습니다."
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e2/March_First_Movement.jpg",
        "caption": "3.1운동 태극기 시위 장면",
        "question": "3.1 운동이 일어난 해는 언제인가요?",
        "options": ["1910년", "1919년", "1923년", "1931년"],
        "answer": "1919년",
        "explanation": "✅ 3.1 운동은 1919년 전국적으로 일어난 독립운동입니다."
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/34/Kim_Koo_2.jpg",
        "caption": "백범 김구 선생",
        "question": "김구 선생이 이끈 임시정부는 어느 나라에 있었나요?",
        "options": ["중국 상하이", "일본 도쿄", "미국 샌프란시스코", "러시아 블라디보스토크"],
        "answer": "중국 상하이",
        "explanation": "✅ 대한민국 임시정부는 중국 상하이에 설립되었습니다."
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Joseon_confucian_school.jpg",
        "caption": "조선 시대 서원 건물",
        "question": "서원은 어떤 목적의 시설인가요?",
        "options": ["불교 수련", "무예 훈련", "유교 교육", "의학 실험"],
        "answer": "유교 교육",
        "explanation": "✅ 서원은 지방 사림이 유학 교육을 위해 설립한 사설 교육 기관입니다."
    }
]

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
    st.session_state.score = 0
    random.shuffle(quizzes)

q = quizzes[st.session_state.quiz_index]

st.image(q["image_url"], caption=q["caption"], use_column_width=True)
st.markdown("**질문:**")
st.write(q["question"])

choice = st.radio("답을 선택하세요:", q["options"], key=q["question"])

if st.button("제출하기"):
    if choice == q["answer"]:
        st.success("정답입니다! " + q["explanation"])
        st.session_state.score += 1
    else:
        st.error(f"오답입니다. ❌ 정답: {q['answer']}\n\n{q['explanation']}")

    st.session_state.quiz_index += 1
    if st.session_state.quiz_index >= len(quizzes):
        st.write("---")
        st.subheader(f"🎉 퀴즈 종료! 총 점수: {st.session_state.score} / {len(quizzes)}")
        if st.button("처음부터 다시 시작하기"):
            st.session_state.quiz_index = 0
            st.session_state.score = 0
            random.shuffle(quizzes)
        st.stop()
    else:
        st.experimental_rerun()

st.write("---")
st.markdown("더 많은 역사 이미지 퀴즈를 계속 추가해드릴까요? 🏯")
