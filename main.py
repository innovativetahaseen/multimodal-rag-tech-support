from src.llm.groq_client import GroqClient
from src.rag.retriever import Retriever

retriever = Retriever()
llm = GroqClient()

question = "How do I clear a paper jam?"

results = retriever.search(question)

context = "\n\n".join(results["documents"][0])

answer = llm.generate(question, context)

print("\nAnswer:\n")
print(answer)