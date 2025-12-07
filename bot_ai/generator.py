from groq import Groq
import streamlit as st

# Load API key from Streamlit Secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# client = Groq(api_key=GROQ_API_KEY)

MODEL_NAME = "llama-3.3-70b-versatile"


def generate_answer(user_query, docs):
    """
    Generate an answer using Groq LLM based on retrieved KB docs.
    """

    # Join retrieved docs
    context = "\n\n".join(docs)

    prompt = f"""
You are an assistant for a credit card company (OneCard).
Answer ONLY using the information in the provided context.

User Question: {user_query}

Context:
{context}

If the answer is not covered by context, say:
"I’m sorry, I don’t have that information in my knowledge base."
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "Answer clearly and concisely."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    # FIX: Groq uses attributes, not dictionary indexing
    return response.choices[0].message.content
