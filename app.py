import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💘 Paulina & Jan Philipp", page_icon="💘", layout="centered")

# ------------------ STATE ------------------
if "answer" not in st.session_state:
    st.session_state.answer = None
if "celebrated" not in st.session_state:
    st.session_state.celebrated = False

# ------------------ GLOBAL STYLES ------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;800&family=Inter:wght@400;600;800;900&display=swap');

:root{
  --red: #7b0f14;
  --red2:#b3121a;
  --ink:#151515;
}

.block-container{max-width: 920px; padding-top: 2.2rem; padding-bottom: 3.2rem;}
.center{ text-align:center; }

.big-title{
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  font-size: clamp(34px, 6vw, 56px);
  font-weight: 900;
  text-align:center;
  margin: 0.2rem 0 0.35rem;
  letter-spacing: -0.03em;
}
.sub{
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  font-size: clamp(16px, 2.2vw, 20px);
  text-align:center;
  opacity: 0.88;
  margin: 0 0 1.5rem;
}

.card{
  background: rgba(255,255,255,0.92);
  border: 1px solid rgba(0,0,0,0.05);
  padding: 22px;
  border-radius: 22px;
  box-shadow: 0 18px 40px rgba(0,0,0,0.12);
}

.card p{
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  font-size: 17px;
  line-height: 1.65;
  color: var(--ink);
  margin: 0 0 12px 0;
}

.lead{
  font-family: Playfair Display, Georgia, serif;
  font-size: 22px;
  font-weight: 800;
  color: var(--red);
  margin-bottom: 12px;
}

.fade-in{ animation: fadeIn 650ms ease-in-out; }
@keyframes fadeIn{
  from{opacity:0; transform: translateY(10px);}
  to{opacity:1; transform: translateY(0);}
}

.photo-wrap{
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 22px 55px rgba(0,0,0,0.18);
  border: 8px solid rgba(123,15,20,0.25);
}

.small-note{
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  opacity: 0.75;
  font-size: 14px;
}

/* Buttons */
div.stButton > button{
  border-radius: 18px;
  padding: 0.95rem 1rem;
  font-weight: 900;
  font-size: 1.05rem;
  border: 1px solid rgba(0,0,0,0.08);
}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------ HEADER ------------------
st.markdown('<div class="big-title">Paulina 💘 Jan Philipp</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Ich habe etwas für dich vorbereitet.</div>', unsafe_allow_html=True)

# ------------------ INTRO ------------------
st.markdown(
    """
<div class="card fade-in">
  <div class="lead">Paulina, ich frage mich das wirklich oft…</div>

  <p>
    wie kann ein Mensch das Leben so sehr verändern – nicht laut, nicht auf einmal,
    sondern in tausend kleinen Momenten: wenn du lachst, wenn du mich ansiehst,
    wenn du einfach da bist.
  </p>

  <p>
    Seit es dich gibt, fühlt sich mein Alltag wärmer an. Ich bin dankbar für jeden Tag mit dir –
    für unsere Höhen, für unsere Tiefen, und für alles dazwischen.
    Und selbst an den schwierigen Tagen: <i>mit dir</i> ist es besser als ohne dich.
  </p>

  <p style="margin-bottom:0;">
    Ich liebe, wie wir zusammen sind. Und genau deshalb wollte ich dir heute etwas sagen –
    und dich etwas fragen.
  </p>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# ------------------ PHOTO (NO TEXT UNDER IT) ------------------
st.markdown('<div class="photo-wrap fade-in">', unsafe_allow_html=True)
st.image("us.jpg", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# ------------------ WEEKEND PLAN (rendered via components.html so it NEVER shows as code) ------------------
components.html(
    """
<div class="plan-card">
  <div class="plan-head">
    <div class="plan-title">Unser Plan</div>
    <div class="plan-sub">(scroll weiter… ich hab mir Gedanken gemacht 😉)</div>
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
      <div class="desc">abends wieder Dinner ✨</div>
    </div>

    <div class="plan-item bl">
      <div class="day">SUNDAY 15</div>
      <div class="title">Kuschelis</div>
      <div class="desc">den ganzen Morgen 🧸</div>
    </div>

    <div class="between b1">kleine Überraschung 🎁</div>
    <div class="between b2">Zeit für uns 😉</div>

    <svg class="curve" viewBox="0 0 1000 650" preserveAspectRatio="none" aria-hidden="true">
      <path d="M 260 140
               C 740 110, 780 260, 590 320
               C 360 395, 330 450, 420 515
               C 520 590, 680 590, 720 560"
            fill="none" stroke="#7b0f14" stroke-width="16" stroke-linecap="round"/>
    </svg>
  </div>
</div>

<style>
  :root{ --red:#7b0f14; --ink:#151515; }

  .plan-card{
    background: rgba(255,255,255,0.92);
    border: 1px solid rgba(0,0,0,0.05);
    padding: 22px;
    border-radius: 22px;
    box-shadow: 0 18px 40px rgba(0,0,0,0.12);
    font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  }

  .plan-head{ margin-bottom: 14px; }
  .plan-title{
    font-family: "Playfair Display", Georgia, serif;
    font-size: 26px;
    font-weight: 800;
    color: var(--red);
    letter-spacing: -0.01em;
  }
  .plan-sub{ opacity: 0.75; margin-top: 4px; }

  .plan{
    position: relative;
    height: 520px;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(123,15,20,0.06), rgba(255,255,255,0.55));
    overflow:hidden;
    border: 1px solid rgba(123,15,20,0.10);
  }

  .plan-item{ position:absolute; max-width: 320px; padding: 10px 12px; color: var(--ink); }
  .day{
    font-size: 34px;
    font-weight: 1000;
    letter-spacing: -0.02em;
    color: var(--red);
    line-height: 1.0;
  }
  .title{ font-size: 18px; font-weight: 900; margin-top: 2px; }
  .desc{ font-size: 14px; opacity: 0.85; margin-top: 2px; }

  .tl{ left: 24px; top: 22px; }
  .mr{ right: 22px; top: 205px; }
  .bl{ left: 24px; bottom: 28px; }

  .between{
    position:absolute;
    font-weight: 900;
    font-size: 16px;
    background: rgba(123,15,20,0.10);
    border: 1px solid rgba(123,15,20,0.18);
    padding: 8px 12px;
    border-radius: 999px;
    color: rgba(20,20,20,0.92);
    backdrop-filter: blur(3px);
  }
  .b1{ left: 360px; top: 130px; }
  .b2{ left: 330px; top: 370px; }

  .curve{
    position:absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    opacity: 0.95;
    pointer-events:none;
  }

  @media (max-width: 560px){
    .plan{ height: 560px; }
    .day{ font-size: 28px; }
    .plan-item{ max-width: 270px; }
    .b1{ left: 26px; top: 165px; }
    .b2{ left: 26px; top: 405px; }
    .mr{ right: 10px; left: 26px; top: 250px; }
  }
</style>
""",
    height=690,
    scrolling=False,
)

st.write("")
st.write("")

# ------------------ QUESTION ------------------
st.markdown(
    """
<div class="card fade-in center">
  <div style="font-family:Playfair Display, Georgia, serif; font-size:28px; font-weight:800; color:#7b0f14;">
    Und jetzt…
  </div>
  <div style="font-family:Inter, system-ui; font-size:18px; opacity:0.9; margin-top:6px;">
    Paulina, willst du mein Valentine sein? 💘
  </div>
  <div class="small-note" style="margin-top:10px;">(Du musst dich entscheiden 😇)</div>
</div>
""",
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)
with col1:
    if st.button("Ja 💖", use_container_width=True, key="yes_btn"):
        st.session_state.answer = "YES"
        st.session_state.celebrated = False
        st.rerun()
with col2:
    if st.button("Nein 🙈", use_container_width=True, key="no_btn"):
        st.session_state.answer = "NO"
        st.session_state.celebrated = False
        st.rerun()

# ------------------ PURE CSS HEART CELEBRATION (no JS, always works) ------------------
def css_hearts_overlay(message="Ich liebe dich über alles."):
    # Create many hearts with staggered delays + big message that fades in
    hearts_html = []
    # fixed set of positions + delays (stable, mobile friendly)
    positions = [5,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96]
    for i in range(1, 49):
        left = positions[i % len(positions)]
        delay = (i % 12) * 0.12
        dur = 2.8 + (i % 7) * 0.25
        size = 18 + (i % 9) * 4
        hearts_html.append(
            f"<span class='h' style='left:{left}vw; animation-delay:{delay}s; animation-duration:{dur}s; font-size:{size}px;'>❤️</span>"
        )

    st.markdown(
        f"""
<style>
#hearts-overlay {{
  position: fixed;
  inset: 0;
  z-index: 999999;
  pointer-events: none;
  overflow: hidden;
  background: rgba(0,0,0,0.10);
  animation: overlayFade 5.2s ease forwards;
}}

#hearts-overlay .h {{
  position: absolute;
  top: 110vh;
  will-change: transform, top, opacity;
  opacity: 0.95;
  filter: drop-shadow(0 10px 14px rgba(0,0,0,0.18));
  animation-name: floatUp;
  animation-timing-function: ease-in-out;
  animation-iteration-count: 1;
}}

@keyframes floatUp {{
  0%   {{ top: 110vh; transform: translateX(0) rotate(0deg); opacity: 0; }}
  10%  {{ opacity: 0.95; }}
  100% {{ top: -20vh; transform: translateX(calc(-60px + 120px * var(--rand))) rotate(420deg); opacity: 0; }}
}}

@keyframes overlayFade {{
  0% {{ opacity: 1; }}
  80% {{ opacity: 1; }}
  100% {{ opacity: 0; }}
}}

#love-text {{
  position: fixed;
  left: 50%;
  top: 48%;
  transform: translate(-50%, -50%);
  z-index: 1000000;
  pointer-events: none;
  text-align: center;
  padding: 18px 18px;
  border-radius: 18px;
  background: rgba(255,255,255,0.72);
  border: 1px solid rgba(123,15,20,0.22);
  box-shadow: 0 18px 44px rgba(0,0,0,0.22);
  opacity: 0;
  animation: textIn 4.8s ease forwards;
  animation-delay: 1.0s;
}}

#love-text .t {{
  font-family: "Playfair Display", Georgia, serif;
  font-size: clamp(28px, 4.6vw, 54px);
  font-weight: 800;
  color: #7b0f14;
  letter-spacing: -0.02em;
}}

#love-text .s {{
  margin-top: 6px;
  font-family: Inter, system-ui;
  font-size: 14px;
  opacity: 0.75;
}}

@keyframes textIn {{
  0% {{ opacity: 0; transform: translate(-50%, -48%) scale(0.98); }}
  20% {{ opacity: 1; transform: translate(-50%, -50%) scale(1.0); }}
  85% {{ opacity: 1; }}
  100% {{ opacity: 0; }}
}}
</style>

<div id="hearts-overlay">
  {''.join(hearts_html)}
</div>
<div id="love-text">
  <div class="t">{message}</div>
  <div class="s">für immer du & ich 💘</div>
</div>

<script>
  // add a tiny random factor for horizontal drift (CSS variable) – safe, no parent hacks
  document.querySelectorAll('#hearts-overlay .h').forEach((el) => {{
    el.style.setProperty('--rand', Math.random().toFixed(2));
  }});
  // auto-remove nodes after animation
  setTimeout(() => {{
    const o = document.getElementById('hearts-overlay'); if(o) o.remove();
    const t = document.getElementById('love-text'); if(t) t.remove();
  }}, 5600);
</script>
        """,
        unsafe_allow_html=True,
    )

# ------------------ RESULTS ------------------
if st.session_state.answer == "YES":
    st.success("JAAAA!!! 💘💘💘")

    if not st.session_state.celebrated:
        css_hearts_overlay("Ich liebe dich über alles.")
        st.session_state.celebrated = True

    st.markdown(
        """
<div class="card fade-in center">
  <div style="font-family:Inter, system-ui; font-size:20px; font-weight:900; color:#151515; line-height:1.35;">
    Ich liebe dich, Paulina. ❤️<br/>
    Dein Jan Philipp 😘
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

elif st.session_state.answer == "NO":
    st.warning("Okaaay… aber bist du dir *wirklich* sicher? 😄")
    st.markdown(
        """
<div class="card fade-in center">
  <div style="font-family:Inter, system-ui; font-size:18px; line-height:1.45;">
    Vielleicht klickst du <b>Ja</b> nur zur Sicherheit nochmal 😉
  </div>
</div>
""",
        unsafe_allow_html=True,
    )
