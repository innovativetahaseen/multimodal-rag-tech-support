from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    _model = None

    def __init__(self):
        if EmbeddingModel._model is None:
            EmbeddingModel._model = SentenceTransformer("all-MiniLM-L6-v2")

        self.model = EmbeddingModel._model

    def encode(self, texts: list[str]) -> list[list[float]]:
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True,
        )

        return embeddings.tolist()