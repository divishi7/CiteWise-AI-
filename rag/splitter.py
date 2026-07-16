from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_SIZE, CHUNK_OVERLAP


class DocumentSplitter:
    """
    Splits cleaned document pages into smaller overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        chunk_overlap: int = CHUNK_OVERLAP,
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

    def split(self, pages):
        """
        Splits every page separately and preserves page numbers.

        Args:
            pages: List of dictionaries
                   [
                       {
                           "page": 1,
                           "text": "..."
                       }
                   ]

        Returns:
            List of dictionaries

            [
                {
                    "page": 1,
                    "text": "chunk..."
                }
            ]
        """

        all_chunks = []

        for page in pages:

            page_number = page["page"]
            page_text = page["text"]

            chunks = self.splitter.split_text(page_text)

            for chunk in chunks:

                all_chunks.append(
                    {
                        "page": page_number,
                        "text": chunk
                    }
                )

        return all_chunks


# -------------------------
# Testing
# -------------------------

from loader import PDFLoader
from cleaner import TextCleaner

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