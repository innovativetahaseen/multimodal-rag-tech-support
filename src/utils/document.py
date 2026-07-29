from dataclasses import dataclass


@dataclass
class Document:
    content: str
    page: int
    source: str