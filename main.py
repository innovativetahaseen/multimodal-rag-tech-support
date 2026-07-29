from src.loaders.pdf_loader import PDFLoader
from src.rag.text_splitter import TextSplitter
from src.rag.embeddings import EmbeddingModel
from src.rag.vector_store import VectorStore

loader = PDFLoader()
splitter = TextSplitter()
embedding_model = EmbeddingModel()
vector_store = VectorStore()

documents = loader.load("data/manuals/sample_manual.pdf")
chunks = splitter.split(documents)

texts = [chunk.content for chunk in chunks]
embeddings = embedding_model.encode(texts)

vector_store.add_documents(chunks, embeddings)

print("✅ Documents stored successfully in ChromaDB!")
print(f"Stored {len(chunks)} chunks.")