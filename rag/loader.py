import fitz  # PyMuPDF
from pathlib import Path


class PDFLoader:
    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

    def load(self):
        """
        Reads all pages from a PDF and returns
        each page separately along with its page number.
        """

        if not self.pdf_path.exists():
            raise FileNotFoundError(f"{self.pdf_path} not found.")

        document = fitz.open(self.pdf_path)

        pages = []

        for page_num, page in enumerate(document, start=1):

            pages.append(
                {
                    "page": page_num,
                    "text": page.get_text()
                }
            )

        document.close()

        return {
            "pages": pages,
            "source": self.pdf_path.name
        }


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
    
#For testing purposes 
# if __name__ == "__main__":
#     loader = PDFLoader("data/raw_pdfs/ai notes.pdf")
#     document = loader.load()

#     print(document["text"][:1000])
#     print(document["source"])