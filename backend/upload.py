from fastapi import APIRouter, UploadFile, File
import shutil
import os

from rag.pipeline import process_pdf

router = APIRouter()

UPLOAD_FOLDER = "backend/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save uploaded PDF
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process PDF using the RAG pipeline
    process_pdf(file_path)

    return {
        "message": "PDF uploaded and processed successfully!",
        "filename": file.filename
    }