"""
Central configuration for the CiteWise AI RAG pipeline.
"""

# ==========================
# Embedding Model
# ==========================

MODEL_NAME = "BAAI/bge-small-en-v1.5"

# ==========================
# Text Splitting
# ==========================

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# ==========================
# ChromaDB
# ==========================

VECTOR_DB_PATH = "data/chroma_db"

COLLECTION_NAME = "citewise_documents"

# ==========================
# Retrieval
# ==========================

TOP_K = 3