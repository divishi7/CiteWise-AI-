import re


class TextCleaner:
    """
    Cleans extracted PDF text while preserving page metadata.
    """

    def clean(self, pages):
        """
        Cleans text for each page separately.

        Args:
            pages: List of dictionaries with
                   {
                       "page": page_number,
                       "text": page_text
                   }

        Returns:
            List of cleaned page dictionaries.
        """

        cleaned_pages = []

        for page in pages:

            text = page["text"]

            # Remove extra spaces and tabs (keep newlines)
            text = re.sub(r"[ \t]+", " ", text)

            # Remove trailing spaces before newline
            text = re.sub(r" *\n *", "\n", text)

            # Replace 3 or more blank lines with 2
            text = re.sub(r"\n{3,}", "\n\n", text)

            # Remove dotted lines (Table of Contents)
            text = re.sub(r"\.{4,}", "", text)

            # Remove repeated separators
            text = re.sub(r"[-_=]{4,}", "", text)

            # Remove "< Contents |"
            text = re.sub(r"<\s*Contents.*?\|", "", text)

            # Remove standalone page numbers
            text = re.sub(r"(?m)^\d+\s*$", "", text)

            # Separate words joined with numbers
            text = re.sub(r"([A-Za-z])(\d+)", r"\1 \2", text)

            # Remove extra blank lines
            text = re.sub(r"\n{3,}", "\n\n", text)

            # Strip leading/trailing whitespace
            text = text.strip()

            cleaned_pages.append(
                {
                    "page": page["page"],
                    "text": text
                }
            )

        return cleaned_pages


# -------------------------------------------------
# Testing
# -------------------------------------------------

from loader import PDFLoader

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