import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💘 Paulina & Jan Philipp", page_icon="💘", layout="centered")

# ------------------ STYLE ------------------
st.markdown("""
<style>
/* Layout */
.block-container {padding-top: 2.2rem; padding-bottom: 3rem; max-width: 800px;}
.center {text-align:center;}
.big-title {font-size: 44px; font-weight: 800; text-align: center; margin: 0.2rem 0 0.2rem;}
.sub {font-size: 18px; text-align: center; opacity: 0.9; margin: 0 0 1.2rem;}

.card {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  padding: 18px;
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}

/* Buttons */
div.stButton > button {
  border-radius: 16px;
  padding: 0.85rem 1rem;
  font-weight: 700;
}

/* Envelope wrapper */
.envelope-wrap{
  display:flex;
  justify-content:center;
  margin: 1.2rem 0 1.6rem;
}
.envelope{
  width: min(520px, 92vw);
  height: 360px;
  background: #f7f1e6;
  border-radius: 22px;
  position: relative;
  box-shadow: 0 18px 40px rgba(0,0,0,0.18);
  overflow:hidden;
  border: 10px solid #7b0f14; /* deep red frame */
}
.envelope::before{
  content:"";
  position:absolute;
  inset:0;
  background: radial-gradient(circle at 30% 20%, rgba(123,15,20,0.08), transparent 45%),
              radial-gradient(circle at 80% 70%, rgba(123,15,20,0.08), transparent 40%);
  pointer-events:none;
}

/* flap lines */
.flap-left, .flap-right{
  position:absolute;
  width: 62%;
  height: 62%;
  top: 22%;
  background: transparent;
  border-top: 3px solid rgba(60,60,60,0.25);
}
.flap-left{
  left:-12%;
  transform: rotate(20deg);
}
.flap-right{
  right:-12%;
  transform: rotate(-20deg);
}

/* wax seal */
.wax{
  position:absolute;
  left: 50%;
  top: 64%;
  transform: translate(-50%, -50%);
  width: 92px;
  height: 92px;
  border-radius: 999px;
  background: radial-gradient(circle at 30% 25%, #b3121a, #7b0f14 68%);
  box-shadow: 0 10px 18px rgba(0,0,0,0.25);
  display:flex;
  align-items:center;
  justify-content:center;
}
.wax span{
  font-weight: 900;
  font-size: 28px;
  color: rgba(255,255,255,0.85);
  letter-spacing: 1px;
}

/* corner initials */
.corner-left{
  position:absolute; left: 22px; top: 16px;
  font-weight: 900; font-size: 34px; color: #7b0f14;
}
.corner-right{
  position:absolute; right: 22px; bottom: 14px;
  font-weight: 900; font-size: 34px; color: #7b0f14;
}
.heart-mini{
  font-size: 22px; color: #7b0f14; opacity:0.9;
  position:absolute;
}
.heart-mini.hl{ left: 27px; top: 56px;}
.heart-mini.hr{ right: 30px; bottom: 56px;}

/* reveal animation helper */
.fade-in {
  animation: fadeIn 700ms ease-in-out;
}
@keyframes fadeIn {
  from {opacity: 0; transform: translateY(10px);}
  to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# ------------------ STATE ------------------
if "opened" not in st.session_state:
    st.session_state.opened = False
if "answer" not in st.session_state:
    st.session_state.answer = None

# ------------------ HEARTS FX ------------------
def hearts_rain(amount=140, speed_ms=45):
    # More hearts + denser rain
    components.html(
        f"""
        <script>
        const emojis = ["💖","💗","💘","💝","💞","💕","❤️"];
        const makeHeart = () => {{
          const heart = document.createElement('div');
          heart.innerHTML = emojis[Math.floor(Math.random()*emojis.length)];
          heart.style.position = 'fixed';
          heart.style.left = Math.random() * 100 + 'vw';
          heart.style.top = '-6vh';
          heart.style.fontSize = (16 + Math.random() * 34) + 'px';
          heart.style.opacity = 0.9;
          heart.style.zIndex = 9999;
          heart.style.filter = 'drop-shadow(0 6px 10px rgba(0,0,0,0.15))';
          heart.style.transition = 'transform 6.5s linear, top 6.5s linear, opacity 6.5s linear';
          document.body.appendChild(heart);

          setTimeout(() => {{
            heart.style.top = '112vh';
            heart.style.transform = `translateX(${{(Math.random()*260-130)}}px) rotate(${{(Math.random()*520)}}deg)`;
            heart.style.opacity = 0.0;
          }}, 30);

          setTimeout(() => heart.remove(), 6800);
        }};

        for (let i=0; i<{amount}; i++) setTimeout(makeHeart, i*{speed_ms});
        </script>
        """,
        height=0,
    )

# ------------------ PAGE ------------------
st.markdown('<div class="big-title">Paulina 💘 Jan Philipp</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">I made a little surprise for you.</div>', unsafe_allow_html=True)

# Envelope (closed) until opened
if not st.session_state.opened:
    components.html(
        """
        <div class="envelope-wrap">
          <div class="envelope">
            <div class="corner-left">P</div>
            <div class="heart-mini hl">♥</div>

            <div class="flap-left"></div>
            <div class="flap-right"></div>

            <div class="wax"><span>PJ</span></div>

            <div class="heart-mini hr">♥</div>
            <div class="corner-right">J</div>
          </div>
        </div>
        """,
        height=410,
    )

    st.markdown("<div class='center' style='font-size:18px;'>Tap to open the letter 💌</div>", unsafe_allow_html=True)
    if st.button("Open the letter 💌", use_container_width=True):
        st.session_state.opened = True
        hearts_rain(amount=90, speed_ms=55)
        st.rerun()


    st.markdown("<div class='center' style='font-size:18px;'>Tap to open the letter 💌</div>", unsafe_allow_html=True)
    if st.button("Open the letter 💌", use_container_width=True):
        st.session_state.opened = True
        hearts_rain(amount=90, speed_ms=55)  # little tease effect
        st.rerun()

else:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)

    # Your photo only after opening
    st.image("us.jpg", use_container_width=True)

    st.write("")
    st.markdown('<div class="card center fade-in">', unsafe_allow_html=True)
    st.markdown("### Paulina… will you be my Valentine on **February 14**? 💘")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes 💖", use_container_width=True):
            st.session_state.answer = "YES"
    with col2:
        if st.button("No 🙈", use_container_width=True):
            st.session_state.answer = "NO"

    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")

    if st.session_state.answer == "YES":
        st.success("YAAAY!!! 💘💘💘")
        hearts_rain(amount=220, speed_ms=35)   # LOTS of hearts
        st.markdown(
            "<div class='center fade-in' style='font-size:22px; font-weight:700;'>"
            "I love you, Paulina. ❤️<br>"
            "Your Jan Philipp 😘"
            "</div>",
            unsafe_allow_html=True
        )

    elif st.session_state.answer == "NO":
        st.warning("Okay… but are you *sure*? 😄")
        st.markdown(
            "<div class='center fade-in' style='font-size:18px;'>"
            "Maybe click <b>Yes</b> just to double-check 😉"
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)
