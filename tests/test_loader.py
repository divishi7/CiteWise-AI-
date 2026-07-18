from rag.loader import PDFLoader
# --------------------------
# Testing
# --------------------------

if __name__ == "__main__":

    loader = PDFLoader("data/raw_pdfs/ai notes.pdf")

    document = loader.load()

    print(f"Source: {document['source']}")
    print(f"Total Pages: {len(document['pages'])}")

    print("\nFirst Page:\n")
    print(document["pages"][0]["text"][:500])