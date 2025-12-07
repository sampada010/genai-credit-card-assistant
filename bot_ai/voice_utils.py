import streamlit as st
from groq import Groq
import base64

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def speech_to_text(audio_bytes):
    audio_b64 = base64.b64encode(audio_bytes).decode("utf-8")

    response = client.audio.transcriptions.create(
        file={"content": audio_b64, "mime_type": "audio/wav"},
        model="whisper-large-v3-turbo"
    )

    return response.text
