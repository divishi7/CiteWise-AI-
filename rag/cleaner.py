import re


class TextCleaner:
    def clean(self, text: str) -> str:
        """
        Cleans extracted PDF text while preserving paragraph structure.
        """

        # Remove extra spaces and tabs (keep newlines)
        text = re.sub(r"[ \t]+", " ", text)

        # Remove trailing spaces before newline
        text = re.sub(r" *\n *", "\n", text)

        # Replace 3 or more blank lines with 2
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove long dotted lines from table of contents
        text = re.sub(r"\.{4,}", "", text)

        # Remove repeated separators
        text = re.sub(r"[-_=]{4,}", "", text)

        # Remove "< Contents |" header
        text = re.sub(r"<\s*Contents.*?\|", "", text)

        # Remove standalone page numbers
        text = re.sub(r"(?m)^\d+\s*$", "", text)

        # Separate words joined with page numbers
        text = re.sub(r"([A-Za-z])(\d+)", r"\1 \2", text)

        # Remove multiple blank lines again after cleaning
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Strip leading/trailing spaces
        text = text.strip()

        return text
    
# from loader import PDFLoader

# if __name__ == "__main__":
#     loader = PDFLoader("data/raw_pdfs/ai notes.pdf")

#     text = loader.load()

#     cleaner = TextCleaner()
#     cleaned_text = cleaner.clean(text)

#     print("========= ORIGINAL =========")
#     print(text[:500])

#     print("\n========= CLEANED =========")
#     print(cleaned_text[:500])