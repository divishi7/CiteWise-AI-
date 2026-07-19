# --------------------------------------------------
# Testing
# --------------------------------------------------
from rag.retriever import Retriever
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