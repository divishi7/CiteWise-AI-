from fastapi import APIRouter, UploadFile, File
from typing import List
import shutil
import os

from chromadb import PersistentClient

from rag.pipeline import process_pdf
from rag.config import VECTOR_DB_PATH, COLLECTION_NAME

router = APIRouter()

UPLOAD_FOLDER = "backend/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_pdf(files: List[UploadFile] = File(...)):

    # -----------------------------
    # Clear old ChromaDB data
    # -----------------------------
    client = PersistentClient(path=VECTOR_DB_PATH)
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    try:
        collection.delete(where={})
        print("Old vectors cleared successfully.")
    except Exception as e:
        print("Error clearing vectors:", e)

    processed_files = []

    # -----------------------------
    # Save and process PDFs
    # -----------------------------
    for file in files:

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        # Save uploaded PDF
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Process PDF
        process_pdf(file_path)

        processed_files.append(file.filename)

    return {
        "message": "All PDFs uploaded successfully!",
        "files": processed_files
    }