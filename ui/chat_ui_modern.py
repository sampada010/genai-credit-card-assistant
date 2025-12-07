import streamlit as st
import os
import sys
from pathlib import Path

# ---------------- Add project root so imports work ----------------
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from bot_ai import retriever, generator
from bot_ai.voice_utils import speech_to_text

# --------------------- STREAMLIT PAGE SETUP -----------------------
st.set_page_config(page_title="GenAI Credit Card Assistant", layout="wide")

# ------------------------- CSS STYLES ------------------------------
st.markdown("""
<style>

body {
    color: white;
}

/* USER MESSAGE */
.user-bubble {
    background-color: #d4ffd4;
    padding: 12px 18px;
    border-radius: 10px;
    margin: 10px 0px;
    color: black !important;
    font-size: 16px;
    font-weight: 500;
}

/* BOT MESSAGE */
.bot-bubble {
    background-color: #ffffff;
    padding: 12px 18px;
    border-radius: 10px;
    margin: 10px 0px;
    color: black !important;
    font-size: 16px;
}

.quick-button {
    background-color: #222;
    padding: 10px 15px;
    border-radius: 8px;
    margin-bottom: 10px;
    width: 150px;
    color: white;
    border: 1px solid white;
}

.quick-button:hover {
    background-color: #444;
}

</style>
""", unsafe_allow_html=True)

# ------------------------- STATE INIT ------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ------------------------- SIDEBAR --------------------------------
with st.sidebar:
    st.header("OneCard Assistant")
    st.write("**User:** Demo User")
    st.write("**Card:** **** 1234")
    st.write("---")

    st.subheader("Quick Actions")

    if st.button("Block Card", key="block"):
        st.session_state.history.append(("assistant", "Card blocked (mock)."))

    if st.button("Bill Summary", key="bill"):
        st.session_state.history.append(("assistant", "Unable to fetch bill summary."))

    if st.button("Convert to EMI", key="emi"):
        st.session_state.history.append(("assistant", "Amount converted to EMI."))

# ----------------------- MAIN TITLE --------------------------------
st.title("GenAI Credit Card Assistant")

# ----------------------- VOICE INPUT --------------------------------
st.subheader("🎙 Speak your message")

audio = st.audio_input("Tap to record your voice")

if audio is not None:
    st.info("Processing voice message...")
    audio_bytes = audio.getvalue()

    text = speech_to_text(audio_bytes)

    if text:
        st.success("You said: " + text)
        st.session_state.history.append(("user", text))

        docs = retriever.retrieve(text)
        answer = generator.generate_answer(text, docs)
        st.session_state.history.append(("assistant", answer))

# ----------------------- TEXT INPUT --------------------------------
st.subheader("Type your message")

query = st.text_input("Enter message:", key="query_box")

if st.button("Send"):
    if query.strip():
        st.session_state.history.append(("user", query))

        docs = retriever.retrieve(query)
        answer = generator.generate_answer(query, docs)
        st.session_state.history.append(("assistant", answer))

# --------------------- CHAT HISTORY DISPLAY ------------------------
st.write("")
st.write("")

for sender, msg in st.session_state.history:
    if sender == "user":
        st.markdown(f"<div class='user-bubble'><b>You:</b> {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'><b>Assistant:</b> {msg}</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Knowledge base powered by Chroma + Local Embeddings. Voice by Groq Whisper.")
