from src.loaders.pdf_loader import PDFLoader
from src.rag.text_splitter import TextSplitter

loader = PDFLoader()
splitter = TextSplitter()

documents = loader.load("data/manuals/sample_manual.pdf")
chunks = splitter.split(documents)

print(f"Pages Loaded : {len(documents)}")
print(f"Chunks Created : {len(chunks)}")

print("\nFirst Chunk\n")
print("-" * 50)
print(chunks[0].content)
print("-" * 50)