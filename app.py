import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💘 Valentine?", page_icon="💘", layout="centered")

st.markdown("""
<style>
.big-title {font-size: 44px; font-weight: 800; text-align: center; margin-bottom: 0.2rem;}
.sub {font-size: 20px; text-align: center; opacity: 0.9; margin-top: 0;}
.card {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  padding: 18px;
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}
.center {text-align: center;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">Hi my love 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">I made this just for you.</div>', unsafe_allow_html=True)
st.write("")

st.image("us.jpg", use_container_width=True)

st.write("")
st.markdown('<div class="card center">', unsafe_allow_html=True)
st.markdown("### Will you be my Valentine on **February 14**? 💘")

if "answer" not in st.session_state:
    st.session_state.answer = None

col1, col2 = st.columns(2)
with col1:
    if st.button("Yes 💖", use_container_width=True):
        st.session_state.answer = "YES"
with col2:
    if st.button("No 🙈", use_container_width=True):
        st.session_state.answer = "NO"

st.markdown("</div>", unsafe_allow_html=True)
st.write("")

def hearts_rain():
    components.html(
        """
        <script>
        const makeHeart = () => {
          const heart = document.createElement('div');
          heart.innerHTML = '💖';
          heart.style.position = 'fixed';
          heart.style.left = Math.random() * 100 + 'vw';
          heart.style.top = '-5vh';
          heart.style.fontSize = (16 + Math.random() * 30) + 'px';
          heart.style.opacity = 0.8;
          heart.style.zIndex = 9999;
          heart.style.transition = 'transform 6s linear, top 6s linear, opacity 6s linear';
          document.body.appendChild(heart);
          setTimeout(() => {
            heart.style.top = '110vh';
            heart.style.transform = `translateX(${(Math.random()*200-100)}px) rotate(${(Math.random()*360)}deg)`;
            heart.style.opacity = 0.0;
          }, 50);
          setTimeout(() => heart.remove(), 6500);
        };
        for (let i=0; i<80; i++) setTimeout(makeHeart, i*80);
        </script>
        """,
        height=0,
    )

if st.session_state.answer == "YES":
    st.success("YAAAY!!! 💘💘💘 I can't wait ❤️")
    hearts_rain()
    st.balloons()
    st.markdown("<div class='center' style='font-size:22px;'>I love you so much. See you on Feb 14 😘</div>", unsafe_allow_html=True)
elif st.session_state.answer == "NO":
    st.warning("Okay… but are you *sure*? 😄")
    st.markdown("<div class='center' style='font-size:18px;'>Maybe click 'Yes' just to double-check 😉</div>", unsafe_allow_html=True)
