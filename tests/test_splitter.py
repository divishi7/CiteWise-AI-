# -------------------------
# Testing
# -------------------------

from rag.loader import PDFLoader
from rag.cleaner import TextCleaner
from rag.splitter import DocumentSplitter

if __name__ == "__main__":

    loader = PDFLoader("data/raw_pdfs/ai notes.pdf")

    document = loader.load()

    cleaner = TextCleaner()

    cleaned_pages = cleaner.clean(document["pages"])

    splitter = DocumentSplitter()

    chunks = splitter.split(cleaned_pages)

    print("=" * 50)
    print(f"Total Chunks: {len(chunks)}")
    print("=" * 50)

    for i, chunk in enumerate(chunks[:3]):

        print(f"\nChunk {i+1}")
        print(f"Page   : {chunk['page']}")
        print(f"Length : {len(chunk['text'])} characters")
        print("-" * 40)
        print(chunk["text"][:300])