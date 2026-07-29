from src.loaders.pdf_loader import PDFLoader
from src.rag.text_splitter import TextSplitter
from src.rag.embeddings import EmbeddingModel

loader = PDFLoader()
splitter = TextSplitter()
embedding_model = EmbeddingModel()

documents = loader.load("data/manuals/sample_manual.pdf")
chunks = splitter.split(documents)

texts = [chunk.content for chunk in chunks]

embeddings = embedding_model.encode(texts)

print(f"Pages Loaded      : {len(documents)}")
print(f"Chunks Created    : {len(chunks)}")
print(f"Embeddings Created: {len(embeddings)}")

print("\nEmbedding Dimension:", len(embeddings[0]))