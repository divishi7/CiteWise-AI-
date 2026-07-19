# --------------------------------------------------
# Testing
# --------------------------------------------------

from rag.loader import PDFLoader
from rag.cleaner import TextCleaner
from rag.splitter import DocumentSplitter
from rag.embeddings import EmbeddingGenerator

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