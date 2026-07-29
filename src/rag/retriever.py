import chromadb

from src.config import CHROMA_DB_DIR
from src.rag.embeddings import EmbeddingModel
from src.rag.setup_vector_db import initialize_vector_database


class Retriever:
    def __init__(self):

        # Initialize the vector database if it doesn't exist
        initialize_vector_database()

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DB_DIR)
        )

        self.collection = self.client.get_collection(
            "technical_support"
        )

        self.embedding_model = EmbeddingModel()

    def search(self, query: str, top_k: int = 3) -> dict:
        """
        Search the vector database and return the top matching documents
        along with their metadata.
        """

        query_embedding = self.embedding_model.encode([query])[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        return results