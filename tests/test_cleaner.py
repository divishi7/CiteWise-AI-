from rag.loader import PDFLoader
from rag.cleaner import TextCleaner

loader = PDFLoader("data/raw_pdfs/ai notes.pdf")
text = loader.load()

cleaner = TextCleaner()
clean_text = cleaner.clean(text)

print(clean_text[:1000])