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
.block-container{max-width: 900px; padding-top: 2.2rem; padding-bottom: 3.2rem;}
.center{ text-align:center; }
h1,h2,h3{ letter-spacing: -0.02em; }
.big-title{
  font-size: clamp(34px, 6vw, 56px);
  font-weight: 900;
  text-align:center;
  margin: 0.2rem 0 0.3rem;
}
.sub{
  font-size: clamp(16px, 2.2vw, 20px);
  text-align:center;
  opacity: 0.92;
  margin: 0 0 1.4rem;
}
.section{
  margin: 2.2rem 0;
}
.card{
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.16);
  padding: 18px;
  border-radius: 22px;
  box-shadow: 0 14px 34px rgba(0,0,0,0.16);
}
.fade-in{ animation: fadeIn 650ms ease-in-out; }
@keyframes fadeIn{
  from{opacity:0; transform: translateY(10px);}
  to{opacity:1; transform: translateY(0);}
}
.small-note{
  opacity: 0.8;
  font-size: 14px;
}

/* Buttons */
div.stButton > button{
  border-radius: 18px;
  padding: 0.95rem 1rem;
  font-weight: 900;
  font-size: 1.05rem;
}

/* Photo with overlay text */
.photo-wrap{
  position: relative;
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 18px 46px rgba(0,0,0,0.22);
  border: 1px solid rgba(255,255,255,0.14);
}
.photo-overlay{
  position:absolute;
  left: 0; right: 0;
  bottom: 0;
  padding: 18px 18px 16px;
  background: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.55) 70%, rgba(0,0,0,0.65) 100%);
}
.photo-overlay .line1{
  color: rgba(255,255,255,0.92);
  font-size: clamp(18px, 2.5vw, 26px);
  font-weight: 900;
  letter-spacing: -0.01em;
}
.photo-overlay .line2{
  color: rgba(255,255,255,0.85);
  font-size: 14px;
  margin-top: 3px;
}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------ HEADER ------------------
st.markdown('<div class="big-title">Paulina 💘 Jan Philipp</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Ich habe etwas für dich vorbereitet.</div>', unsafe_allow_html=True)

# ------------------ INTRO TEXT ------------------
st.markdown(
    """
<div class="section card fade-in">
  <div style="font-size:18px; line-height:1.55;">
    <b>Paulina</b>, ich frage mich das wirklich oft…<br><br>
    Wie kann ein Mensch das Leben so sehr verändern – nicht laut, nicht auf einmal,
    sondern in tausend kleinen Momenten: wenn du lachst, wenn du mich ansiehst,
    wenn du einfach da bist.<br><br>
    Seit es dich gibt, fühlt sich mein Alltag wärmer an. Ich bin dankbar für jeden Tag mit dir –
    für unsere Höhen, für unsere Tiefen, und für alles dazwischen.
    Weil selbst an den schwierigen Tagen: <i>mit dir</i> ist es besser als ohne dich.<br><br>
    Und genau deshalb wollte ich dir heute etwas sagen – und dich etwas fragen.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ------------------ PHOTO + "How lucky we are." ------------------
st.markdown('<div class="section fade-in">', unsafe_allow_html=True)
st.markdown('<div class="photo-wrap">', unsafe_allow_html=True)
st.image("us.jpg", use_container_width=True)
st.markdown(
    """
  <div class="photo-overlay">
    <div class="line1">How lucky we are.</div>
    <div class="line2">…dass wir uns haben. ✨</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ------------------ WEEKEND PLAN (TikTok-style curve) ------------------
st.markdown(
    """
<div class="section card fade-in">
  <div style="font-size:20px; font-weight:900; margin-bottom: 10px;">Unser Plan 🗓️</div>
  <div style="opacity:0.85; margin-bottom: 14px;">(Scroll weiter… ich hab mir Gedanken gemacht 😌)</div>

  <div class="plan">
    <div class="plan-item top-left">
      <div class="day">FRIDAY 13</div>
      <div class="title">Dinner</div>
      <div class="desc">Überraschungsrestaurant 🍽️</div>
      <div class="desc">und reinfeiern in den V-Day 💘</div>
    </div>

    <div class="plan-item mid-right">
      <div class="day">SATURDAY 14</div>
      <div class="title">Rooftop Daydrinks</div>
      <div class="desc">El Palace ☀️🍸</div>
      <div class="desc">abends wieder Dinner ✨</div>
    </div>

    <div class="plan-item bottom-left">
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
            fill="none" stroke="rgba(123,15,20,0.95)" stroke-width="16" stroke-linecap="round"/>
    </svg>
  </div>
</div>

<style>
.plan{
  position: relative;
  height: 520px;
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(255,255,255,0.12), rgba(255,255,255,0.06));
  overflow:hidden;
  border: 1px solid rgba(255,255,255,0.12);
}

.plan-item{
  position:absolute;
  max-width: 320px;
  padding: 10px 12px;
}
.day{
  font-size: 32px;
  font-weight: 1000;
  letter-spacing: -0.02em;
  color: rgba(123,15,20,0.95);
  line-height: 1.0;
}
.title{
  font-size: 18px;
  font-weight: 900;
  margin-top: 2px;
}
.desc{
  font-size: 14px;
  opacity: 0.85;
  margin-top: 2px;
}

.top-left{ left: 24px; top: 22px; }
.mid-right{ right: 22px; top: 205px; text-align:left; }
.bottom-left{ left: 24px; bottom: 28px; }

.between{
  position:absolute;
  font-weight: 900;
  font-size: 16px;
  background: rgba(123,15,20,0.10);
  border: 1px solid rgba(123,15,20,0.18);
  padding: 8px 12px;
  border-radius: 999px;
  color: rgba(30,30,30,0.92);
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

/* Mobile tweaks */
@media (max-width: 560px){
  .plan{ height: 560px; }
  .day{ font-size: 28px; }
  .plan-item{ max-width: 270px; }
  .b1{ left: 26px; top: 165px; }
  .b2{ left: 26px; top: 405px; }
  .mid-right{ right: 10px; left: 26px; top: 250px; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------ FINAL QUESTION ------------------
st.markdown(
    """
<div class="section card fade-in">
  <div class="center" style="font-size:22px; font-weight:1000;">Und jetzt…</div>
  <div class="center" style="font-size:18px; opacity:0.9; margin-top:6px;">
    Paulina, willst du mein Valentine sein? 💘
  </div>
  <div class="center small-note" style="margin-top:10px;">
    (Du musst dich entscheiden 😇)
  </div>
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

# ------------------ EFFECT: hearts -> text ------------------
def hearts_to_text_effect(text="Ich liebe dich über alles."):
    # Fullscreen canvas overlay in parent document + particle text made of hearts
    components.html(
        f"""
<script>
(function(){{
  const doc = window.parent.document;

  // Remove old overlay if any
  const old = doc.getElementById("heartTextOverlay");
  if (old) old.remove();

  // Overlay
  const overlay = doc.createElement("div");
  overlay.id = "heartTextOverlay";
  overlay.style.position = "fixed";
  overlay.style.left = "0";
  overlay.style.top = "0";
  overlay.style.width = "100vw";
  overlay.style.height = "100vh";
  overlay.style.zIndex = "999999";
  overlay.style.pointerEvents = "none";
  overlay.style.background = "rgba(0,0,0,0.00)";
  doc.body.appendChild(overlay);

  const canvas = doc.createElement("canvas");
  canvas.style.width = "100%";
  canvas.style.height = "100%";
  canvas.width = Math.floor(window.innerWidth * (window.devicePixelRatio || 1));
  canvas.height = Math.floor(window.innerHeight * (window.devicePixelRatio || 1));
  overlay.appendChild(canvas);

  const ctx = canvas.getContext("2d");
  const dpr = (window.devicePixelRatio || 1);
  ctx.scale(dpr, dpr);

  const W = window.innerWidth;
  const H = window.innerHeight;

  // Offscreen for text pixels
  const off = doc.createElement("canvas");
  off.width = W;
  off.height = H;
  const offCtx = off.getContext("2d");

  function getFontSize(){{
    // responsive
    return Math.max(34, Math.min(64, Math.floor(W * 0.065)));
  }}

  function buildTargets(){{
    offCtx.clearRect(0,0,W,H);
    offCtx.fillStyle = "#ffffff";
    offCtx.textAlign = "center";
    offCtx.textBaseline = "middle";
    offCtx.font = "900 " + getFontSize() + "px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial";
    offCtx.fillText({text!r}, W/2, H*0.48);

    const img = offCtx.getImageData(0,0,W,H).data;
    const targets = [];
    const step = Math.max(5, Math.floor(W / 180)); // density

    for (let y=0; y<H; y+=step){{
      for (let x=0; x<W; x+=step){{
        const i = (y*W + x)*4 + 3; // alpha
        if (img[i] > 10) targets.push({{x, y}});
      }}
    }}
    return targets;
  }}

  const emojis = ["💖","💗","💘","💝","💞","💕","❤️"];
  const targets = buildTargets();

  // Particles
  const N = Math.min(900, Math.max(420, targets.length));
  const particles = [];

  function rand(min,max){{ return min + Math.random()*(max-min); }}

  for (let i=0; i<N; i++){{
    const t = targets[Math.floor(Math.random()*targets.length)] || {{x:W/2,y:H/2}};
    particles.push({{
      x: rand(0,W),
      y: rand(-H, H),
      vx: rand(-3,3),
      vy: rand(-3,3),
      tx: t.x,
      ty: t.y,
      size: rand(16, 34),
      emoji: emojis[Math.floor(Math.random()*emojis.length)],
      phase: Math.random()*Math.PI*2
    }});
  }}

  let start = performance.now();
  const burstMs = 1200;
  const formMs = 2400;
  const totalMs = 5200;

  function draw(){{
    const now = performance.now();
    const t = now - start;

    ctx.clearRect(0,0,W,H);

    // subtle vignette while effect
    ctx.fillStyle = "rgba(0,0,0," + (t < totalMs ? 0.10 : 0) + ")";
    ctx.fillRect(0,0,W,H);

    for (let p of particles){{
      // Stage 1: wild burst
      if (t < burstMs){{
        p.x += p.vx * 2.6;
        p.y += p.vy * 2.6;
        p.vx += rand(-0.35,0.35);
        p.vy += rand(-0.35,0.35);
      }}
      // Stage 2: converge to text
      else if (t < burstMs + formMs){{
        const k = (t - burstMs) / formMs; // 0..1
        const ease = 1 - Math.pow(1-k, 3);

        p.x += (p.tx - p.x) * (0.06 + 0.10*ease);
        p.y += (p.ty - p.y) * (0.06 + 0.10*ease);

        // small wiggle
        p.phase += 0.08;
        p.x += Math.sin(p.phase) * 0.55;
        p.y += Math.cos(p.phase) * 0.35;
      }}
      // Stage 3: hold & shimmer
      else {{
        p.phase += 0.05;
        p.x += Math.sin(p.phase) * 0.20;
        p.y += Math.cos(p.phase) * 0.12;
      }}

      ctx.font = "900 " + p.size + "px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial";
      ctx.globalAlpha = 0.95;
      ctx.fillText(p.emoji, p.x, p.y);
    }}

    // Add crisp text glow on top near end
    if (t > burstMs + formMs * 0.75) {{
      ctx.globalAlpha = 0.85;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      const fs = getFontSize();
      ctx.font = "1000 " + fs + "px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial";
      ctx.fillStyle = "rgba(255,255,255,0.88)";
      ctx.shadowColor = "rgba(0,0,0,0.35)";
      ctx.shadowBlur = 16;
      ctx.fillText({text!r}, W/2, H*0.48);
      ctx.shadowBlur = 0;
    }}

    ctx.globalAlpha = 1;

    if (t < totalMs) {{
      requestAnimationFrame(draw);
    }} else {{
      // Fade out & remove
      overlay.style.transition = "opacity 700ms ease";
      overlay.style.opacity = "0";
      setTimeout(() => {{
        try {{ overlay.remove(); }} catch(e) {{}}
      }}, 800);
    }}
  }}

  requestAnimationFrame(draw);

  // Resize safety
  window.addEventListener("resize", () => {{
    try {{ overlay.remove(); }} catch(e) {{}}
  }}, {{ once: true }});
}})();
</script>
        """,
        height=0,
        width=0,
    )

if st.session_state.answer == "YES":
    st.success("JAAAA!!! 💘💘💘")

    # Run effect once
    if not st.session_state.celebrated:
        hearts_to_text_effect("Ich liebe dich über alles.")
        st.session_state.celebrated = True

    st.markdown(
        """
<div class="section card fade-in center">
  <div style="font-size:22px; font-weight:1000; line-height:1.35;">
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
<div class="section card fade-in center">
  <div style="font-size:18px; line-height:1.45;">
    Vielleicht klickst du <b>Ja</b> nur zur Sicherheit nochmal 😉
  </div>
</div>
""",
        unsafe_allow_html=True,
    )
