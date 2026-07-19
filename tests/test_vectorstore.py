# --------------------------------------------------
# Testing
# --------------------------------------------------

from rag.loader import PDFLoader
from rag.cleaner import TextCleaner
from rag.splitter import DocumentSplitter
from rag.embeddings import EmbeddingGenerator
from rag.vectorstore import VectorStore

if __name__ == "__main__":

    loader = PDFLoader("data/raw_pdfs/ai notes.pdf")
    document = loader.load()

    cleaner = TextCleaner()
    cleaned_pages = cleaner.clean(document["pages"])

    splitter = DocumentSplitter()
    chunks = splitter.split(cleaned_pages)

    embedder = EmbeddingGenerator()
    embeddings = embedder.generate_embeddings(chunks)

    db = VectorStore()

    db.add_documents(
        chunks,
        embeddings,
        document["source"]
    )
    print("\nVectorStore Test Completed Successfully!")