# -------------------------------------------------
# Testing
# -------------------------------------------------

from rag.loader import PDFLoader
from rag.cleaner import TextCleaner

if __name__ == "__main__":

    loader = PDFLoader("data/raw_pdfs/ai notes.pdf")

    document = loader.load()

    cleaner = TextCleaner()

    cleaned_pages = cleaner.clean(document["pages"])

    print("=" * 50)
    print("SOURCE :", document["source"])
    print("=" * 50)

    print("\nFIRST PAGE (ORIGINAL)\n")
    print(document["pages"][0]["text"][:500])

    print("\nFIRST PAGE (CLEANED)\n")
    print(cleaned_pages[0]["text"][:500])

    print("\nPage Number:", cleaned_pages[0]["page"])