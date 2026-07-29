import chromadb
from chromadb.errors import NotFoundError

from src.config import CHROMA_DB_DIR
from src.rag.embeddings import EmbeddingModel


class Retriever:
    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DB_DIR)
        )

        try:
            self.collection = self.client.get_collection(
                "technical_support"
            )

        except NotFoundError:
            raise RuntimeError(
                "Vector database not found. "
                "Please initialize the vector database before searching."
            )

        self.embedding_model = EmbeddingModel()

    def search(
        self,
        query: str,
        top_k: int = 3,
    ) -> dict:

        query_embedding = self.embedding_model.encode([query])[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        return results