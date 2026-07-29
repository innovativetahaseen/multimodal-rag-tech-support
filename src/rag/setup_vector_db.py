from pathlib import Path

import chromadb

from src.config import CHROMA_DB_DIR
from src.loaders.pdf_loader import PDFLoader
from src.rag.embeddings import EmbeddingModel
from src.rag.text_splitter import TextSplitter
from src.rag.vector_store import VectorStore


def initialize_vector_database():

    client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))

    try:
        client.get_collection("technical_support")
        print("Vector database already exists.")
        return

    except Exception:
        print("Creating vector database...")

    pdf_path = Path("data/manuals/sample_manual.pdf")

    loader = PDFLoader()
    documents = loader.load(str(pdf_path))

    splitter = TextSplitter()
    chunks = splitter.split(documents)

    embedding_model = EmbeddingModel()
    embeddings = embedding_model.encode(
        [chunk.content for chunk in chunks]
    )

    vector_store = VectorStore()
    vector_store.add_documents(
        chunks,
        embeddings,
    )

    print("Vector database created successfully.")