import streamlit as st
import streamlit.components.v1 as components

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="💘 Paulina & Jan Philipp", page_icon="💘", layout="centered")

# ------------------ STATE ------------------
if "opened" not in st.session_state:
    st.session_state.opened = False
if "answer" not in st.session_state:
    st.session_state.answer = None
if "celebrated" not in st.session_state:
    st.session_state.celebrated = False

# ------------------ HEARTS FX ------------------
def hearts_rain(amount=220, speed_ms=25):
    """
    Creates falling heart emojis over the whole page.
    Implemented via an iframe script that writes into window.parent.document.
    """
    components.html(
        f"""
        <script>
        (function() {{
          const doc = window.parent.document;
          const emojis = ["💖","💗","💘","💝","💞","💕","❤️"];
          const duration = 6500;

          function makeHeart() {{
            const heart = doc.createElement('div');
            heart.textContent = emojis[Math.floor(Math.random() * emojis.length)];
            heart.style.position = 'fixed';
            heart.style.left = (Math.random() * 100) + 'vw';
            heart.style.top = '-8vh';
            heart.style.fontSize = (16 + Math.random() * 36) + 'px';
            heart.style.opacity = '0.95';
            heart.style.zIndex = '999999';
            heart.style.pointerEvents = 'none';
            heart.style.filter = 'drop-shadow(0 8px 12px rgba(0,0,0,0.18))';
            heart.style.transition = `transform ${duration}ms linear, top ${duration}ms linear, opacity ${duration}ms linear`;

            doc.body.appendChild(heart);

            setTimeout(() => {{
              heart.style.top = '115vh';
              heart.style.transform = `translateX(${{(Math.random()*320-160)}}px) rotate(${{(Math.random()*720)}}deg)`;
              heart.style.opacity = '0';
            }}, 30);

            setTimeout(() => {{
              try {{ heart.remove(); }} catch(e) {{}}
            }}, duration + 200);
          }}

          for (let i = 0; i < {amount}; i++) {{
            setTimeout(makeHeart, i * {speed_ms});
          }}
        }})();
        </script>
        """,
        height=0,
        width=0,
    )

# ------------------ GLOBAL STYLES ------------------
st.markdown(
    """
<style>
/* Page layout */
.block-container {padding-top: 2.0rem; padding-bottom: 3.0rem; max-width: 850px;}
.center {text-align:center;}
.big-title {font-size: clamp(34px, 6vw, 52px); font-weight: 900; text-align: center; margin: 0.2rem 0 0.2rem;}
.sub {font-size: clamp(16px, 2.2vw, 20px); text-align: center; opacity: 0.92; margin: 0 0 1.2rem;}

/* Buttons */
div.stButton > button {
  border-radius: 18px;
  padding: 0.95rem 1rem;
  font-weight: 800;
  font-size: 1.05rem;
}

/* Card */
.card {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.16);
  padding: 18px;
  border-radius: 20px;
  box-shadow: 0 14px 34px rgba(0,0,0,0.16);
}

/* Simple reveal */
.fade-in { animation: fadeIn 650ms ease-in-out; }
@keyframes fadeIn {
  from {opacity: 0; transform: translateY(10px);}
  to {opacity: 1; transform: translateY(0);}
}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------ HEADER ------------------
st.markdown('<div class="big-title">Paulina 💘 Jan Philipp</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">I made a little surprise for you.</div>', unsafe_allow_html=True)

# ------------------ ENVELOPE HTML (INLINE CSS!) ------------------
def render_envelope():
    # IMPORTANT: CSS is inside this HTML so it applies within the component iframe.
    components.html(
        """
<div style="display:flex; justify-content:center; margin: 1.1rem 0 1.2rem;">
  <div class="env">
    <div class="paper"></div>

    <div class="corner corner-tl">P</div>
    <div class="miniheart miniheart-tl">♥</div>

    <div class="diagonal left"></div>
    <div class="diagonal right"></div>

    <div class="wax">
      <span>P ♥ J</span>
    </div>

    <div class="miniheart miniheart-br">♥</div>
    <div class="corner corner-br">J</div>
  </div>
</div>

<style>
  .env{
    width: min(540px, 92vw);
    height: min(360px, 62vw);
    background: #f7f1e6;
    border-radius: 22px;
    position: relative;
    box-shadow: 0 18px 46px rgba(0,0,0,0.20);
    overflow:hidden;
    border: 10px solid #7b0f14;
  }
  .env::before{
    content:"";
    position:absolute;
    inset:0;
    background:
      radial-gradient(circle at 30% 20%, rgba(123,15,20,0.09), transparent 46%),
      radial-gradient(circle at 80% 72%, rgba(123,15,20,0.09), transparent 42%);
    pointer-events:none;
  }

  /* inner paper hint */
  .paper{
    position:absolute;
    left: 7%;
    right: 7%;
    top: 9%;
    bottom: 22%;
    background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(255,255,255,0.70));
    border-radius: 18px;
    box-shadow: inset 0 0 0 2px rgba(0,0,0,0.04);
  }

  /* diagonals */
  .diagonal{
    position:absolute;
    width: 64%;
    height: 62%;
    top: 24%;
    background: transparent;
    border-top: 3px solid rgba(60,60,60,0.24);
  }
  .diagonal.left{ left:-12%; transform: rotate(20deg); }
  .diagonal.right{ right:-12%; transform: rotate(-20deg); }

  /* wax seal */
  .wax{
    position:absolute;
    left: 50%;
    top: 67%;
    transform: translate(-50%, -50%);
    width: 96px;
    height: 96px;
    border-radius: 999px;
    background: radial-gradient(circle at 30% 25%, #b3121a, #7b0f14 68%);
    box-shadow: 0 12px 22px rgba(0,0,0,0.26);
    display:flex;
    align-items:center;
    justify-content:center;
  }
  .wax span{
    font-weight: 900;
    font-size: 24px;
    color: rgba(255,255,255,0.90);
    letter-spacing: 0.6px;
    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial;
  }

  /* corners */
  .corner{
    position:absolute;
    font-weight: 900;
    font-size: 34px;
    color: #7b0f14;
    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial;
  }
  .corner-tl{ left: 22px; top: 14px; }
  .corner-br{ right: 22px; bottom: 12px; }

  .miniheart{
    position:absolute;
    font-size: 22px;
    color: #7b0f14;
    opacity: 0.92;
  }
  .miniheart-tl{ left: 28px; top: 54px; }
  .miniheart-br{ right: 30px; bottom: 54px; }
</style>
        """,
        height=420,
        scrolling=False,
    )

# ------------------ FLOW ------------------
if not st.session_state.opened:
    render_envelope()

    st.markdown("<div class='center' style='font-size:18px; margin-top: 0.2rem;'>Tap to open the letter 💌</div>", unsafe_allow_html=True)

    if st.button("Open the letter 💌", use_container_width=True, key="open_letter_btn"):
        st.session_state.opened = True
        st.session_state.answer = None
        st.session_state.celebrated = False
        hearts_rain(amount=120, speed_ms=35)  # small tease
        st.rerun()

else:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)

    st.image("us.jpg", use_container_width=True)

    st.write("")
    st.markdown('<div class="card center fade-in">', unsafe_allow_html=True)
    st.markdown("### Paulina… will you be my Valentine on **February 14**? 💘")
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes 💖", use_container_width=True, key="yes_btn"):
            st.session_state.answer = "YES"
            st.session_state.celebrated = False
            st.rerun()
    with col2:
        if st.button("No 🙈", use_container_width=True, key="no_btn"):
            st.session_state.answer = "NO"
            st.session_state.celebrated = False
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")

    if st.session_state.answer == "YES":
        st.success("YAAAY!!! 💘💘💘")

        # Trigger celebration once (avoid raining again on every rerun)
        if not st.session_state.celebrated:
            hearts_rain(amount=320, speed_ms=18)  # LOTS of hearts, no balloons
            st.session_state.celebrated = True

        st.markdown(
            """
            <div class='center fade-in' style='font-size:22px; font-weight:800; line-height:1.35;'>
              I love you, Paulina. ❤️<br/>
              Your Jan Philipp 😘
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif st.session_state.answer == "NO":
        st.warning("Okay… but are you *sure*? 😄")
        st.markdown(
            """
            <div class='center fade-in' style='font-size:18px; line-height:1.45;'>
              Maybe click <b>Yes</b> just to double-check 😉
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)
