#cleaning of text
import re

def clean_chunk(text):
    text = re.sub(r'\s+', ' ', text)           # collapse multiple spaces/newlines into one space
    text = re.sub(r'\bPage \d+\b', '', text)    # remove things like "Page 3"
    return text.strip()

#splitting the answers to check
def split_into_claims(answer_text):
    sentences = re.split(r'(?<=[.!?])\s+', answer_text)   # split on sentence-ending punctuation
    return [s.strip() for s in sentences if s.strip()]
