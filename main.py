from src.loaders.pdf_loader import PDFLoader

loader = PDFLoader()

documents = loader.load("data/manuals/sample_manual.pdf")

print(f"Pages Loaded: {len(documents)}")

if documents:
    print(f"Source: {documents[0].source}")
    print(f"Page: {documents[0].page}")
    print(documents[0].content[:300])