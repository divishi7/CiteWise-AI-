from chromadb import PersistentClient

from rag.config import VECTOR_DB_PATH, COLLECTION_NAME


class VectorStore:
    """
    Stores document embeddings inside ChromaDB.
    """

    def __init__(self):

        self.client = PersistentClient(
            path=VECTOR_DB_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    def remove_document(self, source: str):
        """
        Removes all chunks belonging to a document before
        inserting the latest version.
        """

        existing = self.collection.get(
            where={"source": source}
        )

        if existing["ids"]:

            self.collection.delete(
                ids=existing["ids"]
            )

            print(
                f"Removed {len(existing['ids'])} old chunks from '{source}'."
            )

    def add_documents(self, chunks, embeddings, source):
        """
        Stores document chunks and embeddings in ChromaDB.
        """

        # Remove previous version if it already exists
        self.remove_document(source)

        ids = []
        documents = []
        metadatas = []

        for i, chunk in enumerate(chunks):

            ids.append(f"{source}_chunk_{i}")

            documents.append(chunk["text"])

            metadatas.append(
                {
                    "chunk_id": i,
                    "page": chunk["page"],
                    "source": source
                }
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

        print(f"{len(chunks)} chunks stored successfully.")


