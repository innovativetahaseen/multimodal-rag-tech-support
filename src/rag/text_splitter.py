from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import CHUNK_SIZE, CHUNK_OVERLAP
from src.utils.document import Document


class TextSplitter:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )

    def split(self, documents: list[Document]) -> list[Document]:
        chunks = []

        for document in documents:
            split_texts = self.splitter.split_text(document.content)

            for text in split_texts:
                chunks.append(
                    Document(
                        content=text,
                        page=document.page,
                        source=document.source,
                    )
                )

        return chunks