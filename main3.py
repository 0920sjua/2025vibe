import streamlit as st
import streamlit.components.v1 as components

# HTML 콘텐츠
html_content = """
<!DOCTYPE html>
<html lang=\"ko\">
<head>
  <meta charset=\"UTF-8\">
  <title>국가 전투 구슬 시뮬레이션</title>
  <style>
    body {
      background-color: #1e1e1e;
      color: white;
      font-family: sans-serif;
      text-align: center;
    }
    #arena {
      width: 800px;
      height: 400px;
      border: 2px solid white;
      margin: 20px auto;
      position: relative;
      background-color: #333;
    }
    .ball {
      width: 60px;
      height: 60px;
      border-radius: 50%;
      position: absolute;
      cursor: grab;
      user-select: none;
      font-weight: bold;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 14px;
    }
    #ballA { background-color: red; left: 100px; top: 150px; }
    #ballB { background-color: blue; left: 600px; top: 150px; }
    #summary {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>국가 그룹 전투 시뮬레이션</h1>
  <div id=\"arena\">
    <div class=\"ball\" id=\"ballA\">고려</div>
    <div class=\"ball\" id=\"ballB\">몽골</div>
  </div>
  <div id=\"summary\">
    <h2>고려 vs 몽골</h2>
    <p>고려는 강한 도적을 기절로 몽골의 가편적인 기발을 맞아 거절했습니다.</p>
    <p>※ 마우스로 각 진영을 끌어다 충돌시킬 수 있습니다. 승패는 없습니다!</p>
  </div>
  <script>
    function makeDraggable(ballId) {
      const ball = document.getElementById(ballId);
      let offsetX, offsetY, isDragging = false;

      ball.addEventListener('mousedown', (e) => {
        isDragging = true;
        offsetX = e.offsetX;
        offsetY = e.offsetY;
        ball.style.cursor = 'grabbing';
      });

      document.addEventListener('mousemove', (e) => {
        if (isDragging) {
          const arena = document.getElementById('arena').getBoundingClientRect();
          let x = e.clientX - arena.left - offsetX;
          let y = e.clientY - arena.top - offsetY;
          x = Math.max(0, Math.min(x, arena.width - ball.offsetWidth));
          y = Math.max(0, Math.min(y, arena.height - ball.offsetHeight));
          ball.style.left = x + 'px';
          ball.style.top = y + 'px';
        }
      });

      document.addEventListener('mouseup', () => {
        isDragging = false;
        ball.style.cursor = 'grab';
      });
    }

    makeDraggable('ballA');
    makeDraggable('ballB');
  </script>
</body>
</html>
"""

# Streamlit 앱 실행
st.set_page_config(page_title="전투 구슬", layout="centered")
st.title("⚔️ 고려 vs 몽골 구슬 시뮬레이션")

components.html(html_content, height=600)
