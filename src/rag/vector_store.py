import chromadb

from src.config import CHROMA_DB_DIR
from src.utils.document import Document


class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))

        self.collection = self.client.get_or_create_collection(
            name="technical_support"
        )

    def add_documents(
        self,
        documents: list[Document],
        embeddings: list[list[float]],
    ):
        ids = [f"doc_{i}" for i in range(len(documents))]

        self.collection.add(
            ids=ids,
            documents=[doc.content for doc in documents],
            embeddings=embeddings,
            metadatas=[
                {
                    "page": doc.page,
                    "source": doc.source,
                }
                for doc in documents
            ],
        )