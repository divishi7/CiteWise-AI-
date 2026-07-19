from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer

from rag.config import MODEL_NAME


class EmbeddingGenerator:
    """
    Generates vector embeddings for document chunks.
    """

    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)

    def generate_embeddings(self, chunks: List[dict]) -> np.ndarray:
        """
        Generates embeddings for document chunks.

        Args:
            chunks: List of dictionaries
            [
                {
                    "page": 1,
                    "text": "..."
                }
            ]

        Returns:
            NumPy array containing embeddings.
        """

        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True,
        )

        return embeddings


