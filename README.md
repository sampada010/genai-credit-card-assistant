# 💳 GenAI Credit Card Assistant

A Chat + Voice AI assistant for handling customer queries about credit cards.
Supports RAG-based information retrieval, mock API actions, and voice queries using Groq Whisper.

## 🛠️ Local Setup Instructions (Super Simple)
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/<your-username>/<repo-name>.git
cd credit-card
```

### 2️⃣ Create & activate a virtual environment
```sh
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Add your API key

Create a file named .env in the project root:
```sh
GROQ_API_KEY=your_groq_api_key_here
```

### 5️⃣ Build the Knowledge Base (RAG DB)

This creates the vector database from knowledge_base.md.
```sh
python bot_ai/build_kb.py
```

### 6️⃣ Start the Streamlit UI
```sh
streamlit run ui/chat_ui_modern.py
```

Then open:
```sh
👉 http://localhost:8501
```
