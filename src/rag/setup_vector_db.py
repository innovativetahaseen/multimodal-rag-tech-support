from pathlib import Path

import chromadb

from src.config import CHROMA_DB_DIR
from src.loaders.pdf_loader import PDFLoader
from src.rag.embeddings import EmbeddingModel
from src.rag.text_splitter import TextSplitter
from src.rag.vector_store import VectorStore


def initialize_vector_database():

    client = chromadb.PersistentClient(
        path=str(CHROMA_DB_DIR)
    )

    # Check whether the collection already exists
    collections = client.list_collections()

    for collection in collections:
        if collection.name == "technical_support":
            print("Vector database already exists.")
            return

    print("Creating vector database...")

    pdf_path = Path("data/manuals/sample_manual.pdf")

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF not found: {pdf_path}"
        )

    # Load PDF
    loader = PDFLoader()
    documents = loader.load(str(pdf_path))

    # Split into chunks
    splitter = TextSplitter()
    chunks = splitter.split(documents)

    # Generate embeddings
    embedding_model = EmbeddingModel()
    embeddings = embedding_model.encode(
        [chunk.content for chunk in chunks]
    )

    # Store in ChromaDB
    vector_store = VectorStore()
    vector_store.add_documents(
        documents=chunks,
        embeddings=embeddings,
    )

    print("Vector database created successfully.")