import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💘 Paulina & Jan Philipp", page_icon="💘", layout="centered")

# ------------------ STATE ------------------
if "opened" not in st.session_state:
    st.session_state.opened = False
if "answer" not in st.session_state:
    st.session_state.answer = None
if "celebrated" not in st.session_state:
    st.session_state.celebrated = False

# ------------------ QUERY PARAM OPEN ------------------
def _get_query_params():
    try:
        return dict(st.query_params)
    except Exception:
        return st.experimental_get_query_params()

def _clear_query_params():
    try:
        st.query_params.clear()
    except Exception:
        st.experimental_set_query_params()

qp = _get_query_params()
if not st.session_state.opened and ("open" in qp):
    st.session_state.opened = True
    _clear_query_params()

# ------------------ HEARTS FX (fixed) ------------------
def hearts_rain(amount=320, speed_ms=16):
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
            heart.style.transition =
              'transform ' + duration + 'ms linear, ' +
              'top ' + duration + 'ms linear, ' +
              'opacity ' + duration + 'ms linear';

            doc.body.appendChild(heart);

            setTimeout(() => {{
              heart.style.top = '115vh';
              heart.style.transform = 'translateX(' + (Math.random()*360-180) + 'px) rotate(' + (Math.random()*720) + 'deg)';
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

# ------------------ PAGE CSS ------------------
st.markdown(
    """
<style>
.block-container {padding-top: 2.0rem; padding-bottom: 3.0rem; max-width: 900px;}
.center {text-align:center;}
.big-title {font-size: clamp(34px, 6vw, 54px); font-weight: 900; text-align: center; margin: 0.2rem 0 0.2rem;}
.sub {font-size: clamp(16px, 2.2vw, 20px); text-align: center; opacity: 0.92; margin: 0 0 1.2rem;}
.card {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.16);
  padding: 18px;
  border-radius: 22px;
  box-shadow: 0 14px 34px rgba(0,0,0,0.16);
}
.fade-in { animation: fadeIn 650ms ease-in-out; }
@keyframes fadeIn { from {opacity: 0; transform: translateY(10px);} to {opacity: 1; transform: translateY(0);} }
</style>
""",
    unsafe_allow_html=True,
)

# ------------------ HEADER (DE) ------------------
st.markdown('<div class="big-title">Paulina 💘 Jan Philipp</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Ich habe eine kleine Überraschung für dich.</div>', unsafe_allow_html=True)

# ------------------ ENVELOPE (components.html so nothing shows as code) ------------------
def render_envelope_clickable():
    st.markdown(
        """
<div style="display:flex; justify-content:center; margin: 0.8rem 0 0.4rem;">
  <div class="env">
    <div class="letter"></div>

    <div class="diag left"></div>
    <div class="diag right"></div>

    <div class="fold"></div>

    <div class="corner tl">P</div>
    <div class="mini tlh">♥</div>

    <div class="mini brh">♥</div>
    <div class="corner br">J</div>

    <!-- clickable wax seal: normal link on the real page -->
    <a href="?open=1" class="seal-link" aria-label="Brief öffnen">
      <div class="wax">
        <span>P ♥ J</span>
      </div>
    </a>
  </div>
</div>

<div class="center" style="font-size:18px; margin-top: 0.3rem;">
  Tippe auf das Wachssiegel, um den Brief zu öffnen 💌
</div>

<style>
  a.seal-link { text-decoration: none !important; }
  a.seal-link:visited { color: inherit; }

  .env{
    width: min(620px, 92vw);
    aspect-ratio: 4 / 2.65;
    background: #f1e7d8;
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
      radial-gradient(circle at 30% 20%, rgba(123,15,20,0.10), transparent 46%),
      radial-gradient(circle at 80% 72%, rgba(123,15,20,0.10), transparent 42%);
    pointer-events:none;
  }
  .letter{
    position:absolute;
    left: 9%;
    right: 9%;
    top: 12%;
    bottom: 18%;
    background: #fbfbfb;
    border-radius: 18px;
    box-shadow: 0 18px 28px rgba(0,0,0,0.12);
  }
  .fold{
    position:absolute;
    left: 50%;
    top: 30%;
    width: 54%;
    height: 2px;
    background: rgba(0,0,0,0.15);
    transform: translateX(-50%);
  }
  .diag{
    position:absolute;
    width: 72%;
    height: 70%;
    top: 26%;
    border-top: 3px solid rgba(0,0,0,0.18);
  }
  .diag.left{ left:-16%; transform: rotate(19deg); }
  .diag.right{ right:-16%; transform: rotate(-19deg); }

  .wax{
    position:absolute;
    left: 50%;
    top: 67%;
    transform: translate(-50%, -50%);
    width: 102px;
    height: 102px;
    border-radius: 999px;
    background: radial-gradient(circle at 30% 25%, #c01721, #7b0f14 68%);
    box-shadow: 0 14px 26px rgba(0,0,0,0.28);
    display:flex;
    align-items:center;
    justify-content:center;
    cursor: pointer;
    transition: transform 140ms ease, filter 140ms ease;
    user-select: none;
  }
  .wax:hover{ filter: brightness(1.03); transform: translate(-50%, -50%) scale(1.03); }
  .wax:active{ transform: translate(-50%, -50%) scale(0.98); }

  .wax span{
    font-weight: 900;
    font-size: 22px;
    color: rgba(255,255,255,0.92);
    letter-spacing: 0.6px;
    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial;
  }

  .corner{
    position:absolute;
    font-weight: 900;
    font-size: 34px;
    color: #7b0f14;
    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial;
  }
  .tl{ left: 22px; top: 14px; }
  .br{ right: 22px; bottom: 12px; }

  .mini{
    position:absolute;
    font-size: 20px;
    color: #7b0f14;
    opacity: 0.9;
  }
  .tlh{ left: 30px; top: 54px; }
  .brh{ right: 30px; bottom: 54px; }
</style>
        """,
        unsafe_allow_html=True,
    )


# ------------------ FLOW ------------------
if not st.session_state.opened:
    render_envelope_clickable()

else:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)

    st.image("us.jpg", use_container_width=True)
    st.write("")

    st.markdown('<div class="card center fade-in">', unsafe_allow_html=True)
    st.markdown("### Paulina… willst du am **14. Februar** mein Valentine sein? 💘")
    st.write("")

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

    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")

    if st.session_state.answer == "YES":
        st.success("JAAAA!!! 💘💘💘")

        if not st.session_state.celebrated:
            hearts_rain(amount=380, speed_ms=14)  # große Herz-Party (keine Ballons)
            st.session_state.celebrated = True

        st.markdown(
            """
            <div class='center fade-in' style='font-size:22px; font-weight:800; line-height:1.35;'>
              Ich liebe dich, Paulina. ❤️<br/>
              Dein Jan Philipp 😘
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif st.session_state.answer == "NO":
        st.warning("Okaaay… aber bist du dir *wirklich* sicher? 😄")
        st.markdown(
            """
            <div class='center fade-in' style='font-size:18px; line-height:1.45;'>
              Vielleicht klickst du <b>Ja</b> nur zur Sicherheit nochmal 😉
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)
