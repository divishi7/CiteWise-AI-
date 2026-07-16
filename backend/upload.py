from fastapi import APIRouter, UploadFile, File
import shutil
import os
import fitz
from rag.vectordb import collection
from rag.splitter import split_text

router = APIRouter()

UPLOAD_FOLDER = "backend/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pdf = fitz.open(file_path)
    page = pdf.load_page(0)
    text = page.get_text()
    chunks = split_text(text)
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            ids=[f"{file.filename}_{i}"]
        )
        
    pdf.close()
    print(text[:500])

    return {
        "message": "PDF uploaded successfully!",
        "filename": file.filename,
        "text": text[:500]
    }