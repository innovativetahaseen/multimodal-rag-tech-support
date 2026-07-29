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
    ) -> str:

        results = self.retriever.search(question)

        context = "\n\n".join(results["documents"][0])

        answer = self.llm.generate(
            question=question,
            context=context,
            image_caption=image_caption,
        )

        return answer