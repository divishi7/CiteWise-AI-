from pathlib import Path

from loader import PDFLoader
from cleaner import TextCleaner
from splitter import DocumentSplitter
from embeddings import EmbeddingGenerator
from vectorstore import VectorStore
from retriever import Retriever


if __name__ == "__main__":

    print("=" * 70)
    print("CITEWISE AI - DOCUMENT PROCESSING PIPELINE")
    print("=" * 70)

    # ---------------------------------------------------
    # Initialize reusable objects (only once)
    # ---------------------------------------------------

    cleaner = TextCleaner()
    splitter = DocumentSplitter()
    embedder = EmbeddingGenerator()
    vector_db = VectorStore()

    # ---------------------------------------------------
    # Find all PDFs
    # ---------------------------------------------------

    pdf_folder = Path("data/raw_pdfs")

    pdf_files = list(pdf_folder.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            "No PDF files found in data/raw_pdfs/"
        )

    # ---------------------------------------------------
    # Process every PDF
    # ---------------------------------------------------

    for pdf_file in pdf_files:

        print("\n" + "=" * 70)
        print(f"Processing: {pdf_file.name}")
        print("=" * 70)

        # STEP 1 : LOAD

        print("[1] Loading PDF...")

        loader = PDFLoader(pdf_file)

        document = loader.load()

        print(f"Loaded: {document['source']}")

        # STEP 2 : CLEAN

        print("[2] Cleaning Pages...")

        cleaned_pages = cleaner.clean(document["pages"])

        print(f"Pages Cleaned : {len(cleaned_pages)}")

        # STEP 3 : SPLIT

        print("[3] Splitting Document...")

        chunks = splitter.split(cleaned_pages)

        print(f"Chunks Created : {len(chunks)}")

        # STEP 4 : EMBEDDINGS

        print("[4] Creating Embeddings...")

        embeddings = embedder.generate_embeddings(chunks)

        print(f"Embedding Shape : {embeddings.shape}")

        # STEP 5 : STORE

        print("[5] Saving into ChromaDB...")

        vector_db.add_documents(
            chunks,
            embeddings,
            document["source"]
        )

        print("Vector Database Updated!")

    # ---------------------------------------------------
    # TEST RETRIEVAL
    # ---------------------------------------------------

    print("\n" + "=" * 70)
    print("Testing Retrieval")
    print("=" * 70)

    retriever = Retriever()

    question = "What is Artificial Intelligence?"

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


