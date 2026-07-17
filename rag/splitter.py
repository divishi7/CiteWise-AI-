from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.config import CHUNK_SIZE, CHUNK_OVERLAP


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


