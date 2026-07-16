from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

from config import (
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


# --------------------------------------------------
# Testing
# --------------------------------------------------

if __name__ == "__main__":

    retriever = Retriever()

    question = "What is Artificial Intelligence?"

    results = retriever.retrieve(question)

    print("=" * 60)
    print("Question:")
    print(question)

    print("\nTop Retrieved Chunks:\n")

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for i, (doc, metadata, distance) in enumerate(
        zip(documents, metadatas, distances),
        start=1
    ):

        print("=" * 60)
        print(f"Result {i}")
        print(f"Source   : {metadata['source']}")
        print(f"Page     : {metadata['page']}")
        print(f"Chunk ID : {metadata['chunk_id']}")
        print(f"Distance : {distance:.4f}")
        print("-" * 60)
        print(doc[:300])
        print()