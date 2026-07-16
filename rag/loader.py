import fitz  # PyMuPDF
from pathlib import Path
class PDFLoader:
    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

    def load(self):
        """
        Reads all pages from a PDF and returns the combined text.
        """

        if not self.pdf_path.exists():
            raise FileNotFoundError(f"{self.pdf_path} not found.")

        document = fitz.open(self.pdf_path)

        text = ""

        for page in document:
            text += page.get_text()
        

        document.close()

        return text
    
#For testing purposes 
# if __name__ == "__main__":
#     loader = PDFLoader("data/raw_pdfs/ai notes.pdf")
#     text = loader.load()
#     print(text[:1000])