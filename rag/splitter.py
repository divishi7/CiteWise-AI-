from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentSplitter:
    """
    Splits cleaned text into smaller overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = 800,
        chunk_overlap: int = 150,
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split(self, text: str):
        """
        Splits cleaned text into chunks.
        """

        chunks = self.splitter.split_text(text)

        return chunks
    


from loader import PDFLoader
from cleaner import TextCleaner

if __name__ == "__main__":

    loader = PDFLoader("data/raw_pdfs/ai notes.pdf")
    text = loader.load()

    cleaner = TextCleaner()
    clean_text = cleaner.clean(text)

    splitter = DocumentSplitter()

    chunks = splitter.split(clean_text)

    print("=" * 50)
    print(f"Total Chunks: {len(chunks)}")
    print("=" * 50)

    for i, chunk in enumerate(chunks[:3]):
      print(f"\nChunk {i+1}")
      print(f"Length: {len(chunk)} characters")
      print("-" * 40)
      print(chunk[:300])