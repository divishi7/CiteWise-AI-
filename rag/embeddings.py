from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer

from config import MODEL_NAME


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


# --------------------------------------------------
# Testing
# --------------------------------------------------

from loader import PDFLoader
from cleaner import TextCleaner
from splitter import DocumentSplitter

if __name__ == "__main__":

    loader = PDFLoader("data/raw_pdfs/ai notes.pdf")
    document = loader.load()

    cleaner = TextCleaner()
    cleaned_pages = cleaner.clean(document["pages"])

    splitter = DocumentSplitter()
    chunks = splitter.split(cleaned_pages)

    embedder = EmbeddingGenerator()
    embeddings = embedder.generate_embeddings(chunks)

    print("=" * 60)
    print(f"Total Chunks : {len(chunks)}")
    print(f"Embedding Shape : {embeddings.shape}")
    print("=" * 60)

    print("\nFirst Chunk\n")
    print(f"Page : {chunks[0]['page']}")
    print(chunks[0]["text"][:250])

    print("\nFirst Embedding (first 10 values)\n")
    print(embeddings[0][:10])