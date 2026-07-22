import re

def clean_chunk(text):
    """Removes extra spaces/newlines and stray page numbers from a text chunk."""
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'\bPage \d+\b', '', text)    
    return text.strip()

def clean_markdown(text):
    """Strips markdown formatting (bullets, bold, headers) that interferes with sentence splitting."""
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  
    text = re.sub(r'^\s*[\*\-]\s+', '', text, flags=re.MULTILINE) 
    text = re.sub(r'\s+', ' ', text)        
    return text.strip()

def split_into_claims(answer_text):
    """Cleans markdown, then splits a paragraph into a list of individual sentences."""
    cleaned = clean_markdown(answer_text)
    sentences = re.split(r'(?<=[.!?])\s+', cleaned)
    return [s.strip() for s in sentences if s.strip() and len(s.strip()) > 3]
