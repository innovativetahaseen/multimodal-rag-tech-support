from src.rag.retriever import Retriever

retriever = Retriever()

query = "How do I clear a paper jam?"

results = retriever.search(query)

print("\nTop Results:\n")

for i, document in enumerate(results["documents"][0], start=1):
    metadata = results["metadatas"][0][i - 1]

    print(f"Result {i}")
    print(f"Source : {metadata['source']}")
    print(f"Page   : {metadata['page']}")
    print(document[:300])
    print("-" * 60)