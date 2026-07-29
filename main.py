from src.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

question = "How do I clear a paper jam?"

answer = rag.ask(question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)