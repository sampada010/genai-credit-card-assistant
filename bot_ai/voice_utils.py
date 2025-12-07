import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def speech_to_text(audio_bytes: bytes) -> str:
    response = client.audio.transcriptions.create(
        file=("audio.wav", audio_bytes, "audio/wav"),
        model="whisper-large-v3-turbo"
    )
    return response.text
