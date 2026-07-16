from fastapi import APIRouter
from pydantic import BaseModel
from rag.vectordb import collection

router = APIRouter()


class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
async def chat(request: ChatRequest):
    print(collection.count())

    results = collection.query(
        query_texts=[request.question],
        n_results=3
    )

   if not results["documents"] or not results["documents"][0]:
    return {
        "message": "No relevant information found.",
        "results": []
    }

    return {
        "message": "Relevant information retrieved successfully.",
        "results": results["documents"][0]
    }
    