import chromadb
from chromadb import PersistentClient

PERSIST_DIR = "chroma_store"
COLLECTION_NAME = "onecard_kb"


# ---------------------------------
# Connect to Chroma using NEW API
# ---------------------------------
def connect_chroma():
    """
    Uses new Chroma PersistentClient (no legacy configs).
    """
    client = PersistentClient(path=PERSIST_DIR)
    return client


client = connect_chroma()


# Try loading the collection (create if missing)
try:
    collection = client.get_collection(COLLECTION_NAME)
except Exception:
    collection = client.create_collection(name=COLLECTION_NAME)


# ---------------------------------
# Search Function
# ---------------------------------
def retrieve(query: str, k: int = 3) -> list[str]:
    """
    Returns a clean list of KB text strings.
    """

    try:
        results = collection.query(
            query_texts=[query],
            n_results=k
        )

        docs = results.get("documents", [[]])[0]

        # Ensure clean strings only
        docs = [d.strip() for d in docs if isinstance(d, str)]

        if not docs:
            return ["No relevant information found in the KB."]

        return docs

    except Exception as e:
        return [f"Retrieval error: {str(e)}"]
