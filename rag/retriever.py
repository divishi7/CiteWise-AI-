from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

from rag.config import (
    MODEL_NAME,
    VECTOR_DB_PATH,
    COLLECTION_NAME,
    TOP_K,
)


class Retriever:
    """
    Retrieves the most relevant document chunks from ChromaDB.
    """

    def __init__(self):

        self.client = PersistentClient(
            path=VECTOR_DB_PATH
        )

        self.collection = self.client.get_collection(
            name=COLLECTION_NAME
        )

        self.model = SentenceTransformer(MODEL_NAME)

    def retrieve(self, query: str, top_k: int = TOP_K):
        """
        Retrieve the top-k most relevant chunks.
        """

        # Convert user query into embedding
        query_embedding = self.model.encode(
            query,
            convert_to_numpy=True
        )

        # Search ChromaDB
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k,
            include=["documents", "metadatas", "distances"]
        )

        return results


