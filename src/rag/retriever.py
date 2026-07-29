import chromadb

from src.config import CHROMA_DB_DIR
from src.rag.embeddings import EmbeddingModel


class Retriever:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))
        self.collection = self.client.get_collection("technical_support")
        self.embedding_model = EmbeddingModel()

    def search(self, query: str, top_k: int = 3):
        query_embedding = self.embedding_model.encode([query])[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        return results