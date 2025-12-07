import chromadb
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
import tqdm
import json

PERSIST_DIR = "chroma_store"
COLLECTION_NAME = "onecard_kb"
KB_FILE = "knowledge_base.md"


def load_kb():
    with open(KB_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    sections = [s.strip() for s in content.split("\n\n") if s.strip()]
    return sections


def main():

    print("📄 Loading KB...")
    sections = load_kb()

    model = SentenceTransformer("all-MiniLM-L6-v2")

    client = PersistentClient(path=PERSIST_DIR)

    try:
        collection = client.get_collection(COLLECTION_NAME)
        print("Using existing collection.")
    except Exception:
        collection = client.create_collection(name=COLLECTION_NAME)
        print("Created new collection.")

    print("✨ Embedding...")
    embeddings = model.encode(sections)

    print("📥 Uploading to Chroma...")
    ids = [f"doc_{i}" for i in range(len(sections))]

    collection.upsert(
        ids=ids,
        documents=sections,
        embeddings=embeddings
    )

    print("🚀 KB ready!")


if __name__ == "__main__":
    main()
