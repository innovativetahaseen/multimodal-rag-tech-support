from src.llm.groq_client import GroqClient
from src.rag.retriever import Retriever


class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = GroqClient()

    def ask(
        self,
        question: str,
        image_caption: str | None = None,
    ) -> dict:

        results = self.retriever.search(question)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        context = "\n\n".join(documents)

        answer = self.llm.generate(
            question=question,
            context=context,
            image_caption=image_caption,
        )

        sources = []

        for metadata in metadatas:
            sources.append(
                {
                    "source": metadata.get("source", "Unknown"),
                    "page": metadata.get("page", "Unknown"),
                }
            )

        return {
            "answer": answer,
            "sources": sources,
        }