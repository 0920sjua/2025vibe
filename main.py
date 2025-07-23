import streamlit as st
import random
import time

st.set_page_config(page_title="한국사 전투 시뮬레이터", page_icon="⚔️")
st.title("⚔️ 한국사 중심 전투 시뮬레이터")
st.caption("역사 키워드를 입력하면 한국 중심의 전투 이야기를 생성하고 두 진영의 충돌을 시각화합니다.")

# 사용자 입력
keyword = st.text_input("⚔️ 전투 키워드를 입력하세요", placeholder="예: 몽골, 일본, 청나라, 미국")

# 전투 데이터셋
historical_battles = {
    "몽골": {
        "opponent": "고려",
        "context": "13세기, 몽골은 고려를 침략하며 장기적인 전쟁이 벌어졌습니다. 몽골은 강력한 기병을 앞세워 침공했고, 고려는 강화도 천도를 통해 장기 저항을 이어갔습니다.",
        "battle_name": "몽골-고려 전쟁",
        "visual": ("🔴 몽골", "🔵 고려")
    },
    "일본": {
        "opponent": "조선",
        "context": "1592년 임진왜란, 일본 도요토미 히데요시의 침공으로 시작된 전쟁에서 조선은 왜군과 치열한 접전을 벌였습니다. 이순신 장군의 활약이 특히 두드러졌습니다.",
        "battle_name": "임진왜란",
        "visual": ("🔴 왜군", "🔵 조선")
    },
    "청나라": {
        "opponent": "조선",
        "context": "병자호란은 1636년 청나라가 조선을 침공하며 발생했습니다. 조선은 남한산성에서 결사항전했지만 결국 항복하게 되었습니다.",
        "battle_name": "병자호란",
        "visual": ("🔴 청나라", "🔵 조선")
    },
    "미국": {
        "opponent": "조선",
        "context": "1871년 신미양요 당시, 미국이 조선을 개항시키기 위해 무력 충돌을 일으켰으며, 조선 수비대는 광성보에서 격렬하게 저항했습니다.",
        "battle_name": "신미양요",
        "visual": ("🔴 미국", "🔵 조선")
    }
}

if keyword:
    battle = historical_battles.get(keyword)
    
    if battle:
        st.subheader(f"📜 {battle['battle_name']}")
        st.markdown(battle["context"])
        
        side_a, side_b = battle["visual"]

        # 구슬 충돌 애니메이션
        st.markdown(f"### 전투 시뮬레이션: {side_a} vs {side_b}")
        battle_log = ""
        for i in range(10):
            pos = " " * (10 - i) + side_a + " " * (i * 2) + side_b
            battle_log += pos + "\n"
            time.sleep(0.03)
        st.code(battle_log, language="")

        # 전개 및 결과 (무작위)
        outcome = random.choice([
            f"{battle['opponent']}의 전략적 승리! 결사항전으로 방어에 성공했습니다.",
            f"{keyword}의 압도적인 병력으로 인해 {battle['opponent']}는 일시 후퇴했습니다.",
            f"양측 모두 큰 피해를 입었으며 전쟁은 장기화됩니다.",
        ])
        st.success(f"📣 전투 결과: {outcome}")
    else:
        st.warning("아직 그 키워드에 대한 전투 정보가 없습니다. 예: 몽골, 일본, 청나라, 미국 등")
