import fitz  # PyMuPDF
from pathlib import Path

from src.utils.document import Document


class PDFLoader:
    def load(self, pdf_path: str) -> list[Document]:
        pdf = fitz.open(pdf_path)

        documents = []

        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text = page.get_text().strip()

            if text:
                documents.append(
                    Document(
                        content=text,
                        page=page_num + 1,
                        source=Path(pdf_path).name,
                    )
                )

        pdf.close()
        return documents