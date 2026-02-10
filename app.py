import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💘 Paulina & Jan Philipp", page_icon="💘", layout="centered")

# ------------------ STATE ------------------
if "answer" not in st.session_state:
    st.session_state.answer = None
if "celebrated" not in st.session_state:
    st.session_state.celebrated = False

# ------------------ GLOBAL STYLES (RED SERIF EVERYWHERE) ------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;800;900&display=swap');

:root{
  --red:#7b0f14;
  --red2:#b3121a;
  --paper: rgba(255,255,255,0.94);
  --shadow: 0 18px 42px rgba(0,0,0,0.12);
}

*{
  font-family: "Playfair Display", Georgia, serif !important;
}

.block-container{
  max-width: 980px;
  padding-top: 2.2rem;
  padding-bottom: 3.4rem;
}

.center{ text-align:center; }

.big-title{
  font-size: clamp(34px, 6vw, 62px);
  font-weight: 900;
  letter-spacing: -0.03em;
  color: var(--red);
  text-align:center;
  margin: 0.2rem 0 0.35rem;
}

.sub{
  font-size: clamp(16px, 2.2vw, 22px);
  color: rgba(123,15,20,0.78);
  text-align:center;
  margin: 0 0 1.7rem;
}

.card{
  background: var(--paper);
  border: 1px solid rgba(123,15,20,0.12);
  padding: 24px;
  border-radius: 24px;
  box-shadow: var(--shadow);
}

.card p{
  color: rgba(123,15,20,0.92);
  font-size: 18px;
  line-height: 1.65;
  margin: 0 0 12px 0;
}

.lead{
  font-size: 26px;
  font-weight: 900;
  color: var(--red);
  letter-spacing: -0.02em;
  margin-bottom: 12px;
}

.fade-in{ animation: fadeIn 650ms ease-in-out; }
@keyframes fadeIn{
  from{opacity:0; transform: translateY(10px);}
  to{opacity:1; transform: translateY(0);}
}

.photo-wrap{
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 22px 60px rgba(0,0,0,0.16);
  border: 8px solid rgba(123,15,20,0.20);
}

.small-note{
  color: rgba(123,15,20,0.65);
  font-size: 14px;
}

/* Buttons */
div.stButton > button{
  border-radius: 20px;
  padding: 1.0rem 1rem;
  font-weight: 900;
  font-size: 1.08rem;
  color: var(--red) !important;
  background: rgba(255,255,255,0.95) !important;
  border: 1px solid rgba(123,15,20,0.20) !important;
  box-shadow: 0 10px 20px rgba(0,0,0,0.08);
}
div.stButton > button:hover{
  border-color: rgba(123,15,20,0.35) !important;
  transform: translateY(-1px);
}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------ HEADER ------------------
st.markdown('<div class="big-title">Pauli & JP V-Day</div>', unsafe_allow_html=True)
st.markdown('<div class="sub"></div>', unsafe_allow_html=True)

# ------------------ INTRO ------------------
st.markdown(
    """
<div class="card fade-in">
  <div class="lead">Pauli mein Schatz, </div>

  <p>
    Ich bin jeden Tag dankbar dich in meinem Leben zu haben –
    für unsere Höhen, für unsere Tiefen, und für alles dazwischen. Ich kann nicht in Worte fassen, wie unfassbar schön und bedeutungsvoll du mein Leben machst. Du bringst mir bei, was es heißt einen Menschen wirklich lieben zu lernen. Dafür werde ich dir immer dankbar sein.
  </p>

  <p style="margin-bottom:0;">
    Ich liebe dich und uns über alles :)
  </p>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# ------------------ PHOTO (NO EXTRA TEXT) ------------------
st.markdown('<div class="photo-wrap fade-in">', unsafe_allow_html=True)
st.image("us.jpg", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.write("")









# ------------------ WEEKEND PLAN (components.html so it never turns into code) ------------------
components.html(
    """
<div class="plan-card">
  <div class="plan-head">
    <div class="plan-title">V-Day Plan</div>
    <div class="plan-sub"></div>
  </div>

  <div class="plan">
    <div class="plan-item tl">
      <div class="day">FRIDAY 13</div>
      <div class="title">Dinner</div>
      <div class="desc">Überraschungsrestaurant 🍽️</div>
      <div class="desc">und reinfeiern in den V-Day 💘</div>
    </div>

    <div class="plan-item mr">
      <div class="day">SATURDAY 14</div>
      <div class="title">Rooftop Daydrinks</div>
      <div class="desc">El Palace ☀️🍸</div>
      <div class="desc">und abends wieder Dinner ✨</div>
    </div>

    <div class="plan-item bl">
      <div class="day">SUNDAY 15</div>
      <div class="title">Kuschelis</div>
      <div class="desc">den ganzen Morgen 🧸</div>
    </div>

    <!-- labels ON TOP of the curve (DESKTOP positions below in CSS) -->
    <div class="between b1">kleine Überraschung 🎁</div>
    <div class="between b2">Dessert 😉</div>

    <!-- Desktop curve -->
<svg class="curve curve-desktop" viewBox="0 0 1000 650" preserveAspectRatio="none" aria-hidden="true">
  <path d="M 330 145
         C 720 120, 825 255, 610 325
         C 410 390, 320 515, 360 580"
      fill="none" stroke="#7b0f14" stroke-width="16" stroke-linecap="round"/>

</svg>


    <!-- Mobile curve -->
<svg class="curve curve-mobile" viewBox="0 0 1000 650" preserveAspectRatio="none" aria-hidden="true">
  <path d="M 640 90
           C 860 150, 860 270, 650 335
           C 470 395, 500 520, 670 585
           C 790 635, 890 600, 930 545"
        fill="none" stroke="#7b0f14" stroke-width="16" stroke-linecap="round"/>
</svg>

  </div>
</div>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;800;900&display=swap');
  *{ font-family: "Playfair Display", Georgia, serif !important; }
  :root{ --red:#7b0f14; }

  .plan-card{
    background: rgba(255,255,255,0.94);
    border: 1px solid rgba(123,15,20,0.12);
    padding: 24px;
    border-radius: 24px;
    box-shadow: 0 18px 42px rgba(0,0,0,0.12);
  }

  .plan-head{
    margin-bottom: 16px;
    text-align: center;
  }

  .plan-title{
    font-size: 44px;
    font-weight: 900;
    color: var(--red);
    letter-spacing: -0.03em;
    line-height: 1.0;
  }

  .plan-sub{
    margin-top: 8px;
    font-size: 18px;
    color: rgba(123,15,20,0.70);
  }

  .plan{
    position: relative;
    height: 540px;
    border-radius: 18px;
    background: radial-gradient(circle at 20% 20%, rgba(123,15,20,0.06), transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(123,15,20,0.06), transparent 50%),
                linear-gradient(135deg, rgba(255,255,255,0.70), rgba(255,255,255,0.35));
    overflow: hidden;
    border: 1px solid rgba(123,15,20,0.12);
  }

  .plan-item{
    position: absolute;
    max-width: 340px;
    padding: 10px 12px;
    color: rgba(123,15,20,0.92);
    z-index: 4;
  }

  .day{
    font-size: 40px;
    font-weight: 900;
    letter-spacing: -0.03em;
    color: var(--red);
    line-height: 1.0;
  }

  .title{
    font-size: 22px;
    font-weight: 900;
    margin-top: 4px;
  }

  .desc{
    font-size: 16px;
    margin-top: 4px;
    color: rgba(123,15,20,0.82);
  }

  .tl{ left: 34px; top: 30px; }

  /* ✅ Saturday further right so it doesn't overlap the curve */
  .mr{ right: 12px; top: 235px; text-align: left; }

  .bl{ left: 34px; bottom: 34px; }

  /* pills ON TOP of the curve (make them readable even when overlapping the line) */
  .between{
    position: absolute;
    font-weight: 900;
    font-size: 18px;
    padding: 10px 14px;
    border-radius: 999px;
    color: rgba(123,15,20,0.92);
    white-space: nowrap;
    z-index: 8;

    /* key: white-ish pill so it sits cleanly on top of the curve */
    background: rgba(255,255,255,0.86);
    border: 1px solid rgba(123,15,20,0.22);
    box-shadow: 0 10px 22px rgba(0,0,0,0.10);
    backdrop-filter: blur(4px);
  }

  /* ✅ Desktop: both pills moved left onto the curve */
  .b1{ left: 455px; top: 112px; }  /* between Fri & Sat, clearly on the line */
  .b2{ left: 325px; top: 305px; }  /* between Sat & Sun, clearly on the line */

  .curve{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    opacity: 0.95;
    pointer-events: none;
    z-index: 1;
  }

  /* Desktop shows only desktop curve */
  .curve-desktop{ display: block; }
  .curve-mobile{ display: none; }

  
  
  
  
  
  
  
  
  @media (max-width: 560px){

  /* Head */
  .plan-title{ font-size: 30px; line-height: 1.05; }
  .plan-sub{ font-size: 13px; margin-top: 6px; }

  /* Plan container */
  .plan{
    height: auto;
    padding: 16px 14px 18px;
    display: flex;
    flex-direction: column;
    gap: 14px;
    align-items: stretch;
  }

  /* Gerade rote Linie im Hintergrund */
  .plan::before{
    content:"";
    position:absolute;
    left: 50%;
    top: 18px;
    bottom: 18px;
    width: 8px;
    transform: translateX(-50%);
    border-radius: 999px;
    background: rgba(123,15,20,0.90);
    opacity: 0.28;
    z-index: 0;
    pointer-events:none;
  }

  /* Alle Items werden normale Blöcke (nicht absolut) */
  .plan-item{
    position: relative;
    left: auto; right: auto; top: auto; bottom: auto;

    width: 100%;
    max-width: 100%;

    padding: 14px 14px;
    border-radius: 16px;

    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(123,15,20,0.16);

    box-shadow: 0 10px 22px rgba(0,0,0,0.08);
    z-index: 2;
  }

  /* Typo kleiner */
  .day{ font-size: 26px; line-height: 1.0; }
  .title{ font-size: 16px; margin-top: 6px; }
  .desc{ font-size: 13px; margin-top: 6px; }

  /* Pills: klein + mittig über der Linie */
  .between{
    position: relative;
    left: auto; top: auto;
    align-self: center;

    font-size: 14px;
    padding: 9px 12px;
    border-radius: 999px;

    background: rgba(255,255,255,0.92);
    border: 1px solid rgba(123,15,20,0.22);
    box-shadow: 0 10px 20px rgba(0,0,0,0.08);
    z-index: 3;
    white-space: nowrap;
  }

  /* Optional: kleine optische “Anker” zur Linie */
  .plan-item::before{
    content:"";
    position:absolute;
    left: 50%;
    top: 16px;
    width: 10px;
    height: 10px;
    transform: translateX(-50%);
    border-radius: 50%;
    background: rgba(123,15,20,0.55);
  }

  /* Desktop absolute positions egalisieren */
  .tl,.mr,.bl{ text-align:left; }

  /* Kurven auf Mobile aus */
  .curve-desktop{ display:none !important; }
  .curve-mobile{ display:none !important; }
}









</style>
""",
    height=740,
    scrolling=False,
)









st.write("")
st.write("")

# ------------------ QUESTION ------------------
# ------------------ QUESTION ------------------
st.markdown(
    """
<div class="card fade-in center">
  <div style="font-size:22px; font-weight:800; color:rgba(123,15,20,0.78); letter-spacing:-0.01em; line-height:1.2;">
  </div>

  <div style="font-size:46px; font-weight:900; color:#7b0f14; letter-spacing:-0.03em; line-height:1.05; margin-top:10px;">
    Can I claim you as my Valentine Pauli? :)
  </div>

  <div class="small-note" style="margin-top:14px; color:rgba(123,15,20,0.60); font-size:14px;">
  </div>
</div>
""",
    unsafe_allow_html=True,
)


col1, col2 = st.columns(2)
with col1:
    if st.button("Jaaaa", use_container_width=True, key="yes_btn"):
        st.session_state.answer = "YES"
        st.session_state.celebrated = False
        st.rerun()
with col2:
    if st.button("No Option", use_container_width=True, key="no_btn"):
        st.session_state.answer = "NO"
        st.session_state.celebrated = False
        st.rerun()

# ------------------ BIG HEART CELEBRATION (large hearts + message) ------------------
def big_hearts_overlay(message=None):
    hearts_html = []
    for i in range(1, 120):
        left = (i * 7) % 100
        delay = (i % 18) * 0.08
        dur = 3.2 + (i % 8) * 0.22

        if i % 20 == 0:
            size = 110
        elif i % 10 == 0:
            size = 78
        elif i % 5 == 0:
            size = 54
        else:
            size = 28 + (i % 12) * 3

        hearts_html.append(
            f"<span class='h' style='left:{left}vw; animation-delay:{delay}s; animation-duration:{dur}s; font-size:{size}px;'>❤️</span>"
        )

    love_text_html = ""
    if message and str(message).strip():
        love_text_html = f"""
<div id="love-text">
  <div class="t">{message}</div>
</div>
"""

    st.markdown(
        f"""
<style>
#hearts-overlay {{
  position: fixed;
  inset: 0;
  z-index: 999999;
  pointer-events: none;
  overflow: hidden;
  background: rgba(255,255,255,0.0);
}}

#hearts-overlay .h {{
  position: absolute;
  top: 115vh;
  opacity: 0.0;
  filter: drop-shadow(0 18px 22px rgba(0,0,0,0.18));
  animation-name: floatUp;
  animation-timing-function: ease-in-out;
  animation-iteration-count: 1;
  will-change: transform, top, opacity;
}}

@keyframes floatUp {{
  0%   {{ top: 115vh; transform: translateX(0) rotate(0deg) scale(0.98); opacity: 0; }}
  8%   {{ opacity: 0.98; }}
  100% {{ top: -25vh; transform: translateX(calc(-120px + 240px * var(--rand))) rotate(520deg) scale(1.02); opacity: 0; }}
}}

#love-text {{
  position: fixed;
  left: 50%;
  top: 48%;
  transform: translate(-50%, -50%);
  z-index: 1000000;
  pointer-events: none;
  text-align: center;
  padding: 18px 22px;
  border-radius: 22px;
  background: rgba(255,255,255,0.82);
  border: 1px solid rgba(123,15,20,0.22);
  box-shadow: 0 22px 55px rgba(0,0,0,0.18);
  opacity: 0;
  animation: textIn 5.0s ease forwards;
  animation-delay: 0.9s;
}}

#love-text .t {{
  font-size: clamp(34px, 4.9vw, 64px);
  font-weight: 900;
  color: #7b0f14;
  letter-spacing: -0.03em;
  line-height: 1.05;
}}

@keyframes textIn {{
  0% {{ opacity: 0; transform: translate(-50%, -48%) scale(0.98); }}
  18% {{ opacity: 1; transform: translate(-50%, -50%) scale(1.0); }}
  82% {{ opacity: 1; }}
  100% {{ opacity: 0; }}
}}
</style>

<div id="hearts-overlay">
  {''.join(hearts_html)}
</div>

{love_text_html}

<script>
  document.querySelectorAll('#hearts-overlay .h').forEach((el) => {{
    el.style.setProperty('--rand', Math.random().toFixed(2));
  }});
  setTimeout(() => {{
    const o = document.getElementById('hearts-overlay'); if(o) o.remove();
    const t = document.getElementById('love-text'); if(t) t.remove();
  }}, 6200);
</script>
        """,
        unsafe_allow_html=True,
    )


# ------------------ RESULTS ------------------
if st.session_state.answer == "YES":
    if not st.session_state.celebrated:
        big_hearts_overlay("")
        st.session_state.celebrated = True

    st.markdown(
        """
<div class="card fade-in center">
  <div style="font-size:28px; font-weight:900; color:#7b0f14; letter-spacing:-0.02em; line-height:1.25;">
    Ich liebe dich Paulina ❤️<br/>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )
