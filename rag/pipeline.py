from pathlib import Path

from rag.logger import logger
from rag.loader import PDFLoader
from rag.cleaner import TextCleaner
from rag.splitter import DocumentSplitter
from rag.embeddings import EmbeddingGenerator
from rag.vectorstore import VectorStore
from rag.retriever import Retriever


def process_pdf(pdf_path: str):
    """
    Processes a single PDF and stores it in ChromaDB.
    """

    cleaner = TextCleaner()
    splitter = DocumentSplitter()
    embedder = EmbeddingGenerator()
    vector_db = VectorStore()

    pdf_file = Path(pdf_path)

    logger.info(f"[1] Loading {pdf_file.name}")

    loader = PDFLoader(pdf_file)
    document = loader.load()

    logger.info(f"Loaded: {document['source']}")

    logger.info(f"Cleaning {document['source']}")

    cleaned_pages = cleaner.clean(document["pages"])

    logger.info(f"Pages Cleaned : {len(cleaned_pages)}")

    logger.info("[3] Splitting Document...")

    chunks = splitter.split(cleaned_pages)

    logger.info(f"Chunks Created : {len(chunks)}")

    logger.info("[4] Creating Embeddings...")

    embeddings = embedder.generate_embeddings(chunks)

    logger.info(f"Embedding Shape : {embeddings.shape}")

    logger.info("[5] Saving into ChromaDB...")

    vector_db.add_documents(
        chunks,
        embeddings,
        document["source"]
    )

    logger.info("Vector Database Updated!")

    logger.info(
        f"{document['source']} processed successfully."
    )


if __name__ == "__main__":

    print("=" * 70)
    print("CITEWISE AI - DOCUMENT PROCESSING PIPELINE")
    print("=" * 70)

    pdf_folder = Path("data/raw_pdfs")
    pdf_files = list(pdf_folder.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            "No PDF files found in data/raw_pdfs/"
        )

    for pdf_file in pdf_files:

        print("\n" + "=" * 70)
        print(f"Processing: {pdf_file.name}")
        print("=" * 70)

        try:
            process_pdf(str(pdf_file))

        except Exception:
            logger.exception(
                f"Failed to process {pdf_file.name}"
            )
            continue

    # ---------------------------------------------------
    # TEST RETRIEVAL
    # ---------------------------------------------------

    print("\n" + "=" * 70)
    print("Testing Retrieval")
    print("=" * 70)

    try:

        retriever = Retriever()

        question = "What is Artificial Intelligence?"

        logger.info(
            f"Running retrieval for question: {question}"
        )

        results = retriever.retrieve(question)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        print("\nQuestion:")
        print(question)

        print("\nTop Retrieved Chunks:\n")

        for i, (doc, metadata) in enumerate(
            zip(documents, metadatas),
            start=1,
        ):

            print("=" * 60)
            print(f"Result {i}")
            print(f"Source : {metadata['source']}")
            print(f"Page   : {metadata['page']}")
            print(f"Chunk  : {metadata['chunk_id']}")
            print("-" * 60)

            print(doc[:300])
            print()

        logger.info("Retrieval test completed successfully.")

    except Exception:

        logger.exception(
            "Retriever failed."
        )


