from groq import Groq
import streamlit as st

# Load API key from Streamlit Secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_answer(query, docs):
    context = "\n\n".join(docs)

    prompt = f"""
You are a helpful credit card assistant.
Use ONLY the context below to answer.

Context:
{context}

User question: {query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]
