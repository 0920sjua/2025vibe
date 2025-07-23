import streamlit as st
import streamlit.components.v1 as components

# 키워드 기반 정보
battle_data = {
    "몽골": {"opponent": "고려", "summary": "고려는 강화도로 천도하며 몽골 침입을 버텨냈습니다."},
    "일본": {"opponent": "조선", "summary": "임진왜란 중 조선은 이순신 장군의 활약으로 해전을 승리로 이끌었습니다."},
    "청나라": {"opponent": "조선", "summary": "병자호란 당시 남한산성에서 조선이 끝까지 항전했습니다."},
    "미국": {"opponent": "조선", "summary": "신미양요에서 조선 수비대는 강화도에서 격렬히 저항했습니다."},
    "명나라": {"opponent": "조선", "summary": "임진왜란 말기, 명은 조선을 도와 일본과 싸웠습니다."}
}

# 사용자 입력
st.set_page_config(page_title="전투 구슬", layout="centered")
st.markdown("""
<style>
    .main, body, html {
        background-color: black;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚔️ 한국사 전투 시뮬레이션")
keyword = st.text_input("역사 키워드를 입력하세요 (예: 몽골, 일본, 청나라, 미국, 명나라)")

if keyword and keyword in battle_data:
    opponent = battle_data[keyword]["opponent"]
    summary = battle_data[keyword]["summary"]

    html_content = f"""
    <!DOCTYPE html>
    <html lang=\"ko\">
    <head>
      <meta charset=\"UTF-8\">
      <title>{opponent} vs {keyword} 전투 시뮬레이션</title>
      <style>
        html, body {{
          background-color: black;
          margin: 0;
          padding: 0;
        }}
        body {{
          color: white;
          font-family: sans-serif;
          text-align: center;
        }}
        #arena {{
          width: 800px;
          height: 400px;
          border: 2px solid white;
          margin: 20px auto;
          position: relative;
          background-color: #333;
          overflow: hidden;
        }}
        .ball {{
          width: 100px;
          height: 100px;
          border-radius: 50%;
          position: absolute;
          cursor: grab;
          user-select: none;
          font-weight: bold;
          display: flex;
          justify-content: center;
          align-items: center;
          font-size: 16px;
          transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        #ballA {{ background-color: red; left: 100px; top: 150px; }}
        #ballB {{ background-color: blue; left: 600px; top: 150px; }}
        #summary {{
          margin-top: 20px;
        }}
        .explosion {{
          position: absolute;
          width: 100px;
          height: 100px;
          background: radial-gradient(circle, orange, red, black);
          border-radius: 50%;
          animation: explode 0.4s ease-out;
          pointer-events: none;
        }}
        @keyframes explode {{
          0% {{ transform: scale(0.2); opacity: 1; }}
          100% {{ transform: scale(2.5); opacity: 0; }}
        }}
      </style>
    </head>
    <body>
      <h1>{opponent} vs {keyword}</h1>
      <div id=\"arena\">
        <div class=\"ball\" id=\"ballA\">{opponent}</div>
        <div class=\"ball\" id=\"ballB\">{keyword}</div>
      </div>
      <div id=\"summary\">
        <p>{summary}</p>
        <p>※ 마우스로 구슬을 드래그해서 충돌시킬 수 있습니다!</p>
      </div>
      <script>
        function makeDraggable(ballId) {{
          const ball = document.getElementById(ballId);
          let offsetX, offsetY, isDragging = false;

          ball.addEventListener('mousedown', (e) => {{
            isDragging = true;
            offsetX = e.offsetX;
            offsetY = e.offsetY;
            ball.style.cursor = 'grabbing';
          }});

          document.addEventListener('mousemove', (e) => {{
            if (isDragging) {{
              const arena = document.getElementById('arena').getBoundingClientRect();
              let x = e.clientX - arena.left - offsetX;
              let y = e.clientY - arena.top - offsetY;
              x = Math.max(0, Math.min(x, arena.width - ball.offsetWidth));
              y = Math.max(0, Math.min(y, arena.height - ball.offsetHeight));
              ball.style.left = x + 'px';
              ball.style.top = y + 'px';
              checkCollision();
            }}
          }});

          document.addEventListener('mouseup', () => {{
            isDragging = false;
            ball.style.cursor = 'grab';
          }});
        }}

        function checkCollision() {{
          const ballA = document.getElementById('ballA');
          con
