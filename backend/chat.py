from fastapi import APIRouter
from pydantic import BaseModel
from rag.vectordb import collection
from backend.gemini_service import generate_answer

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    results = collection.query(
        query_texts=[request.question],
        n_results=3
    )
   
    if not results["documents"] or not results["documents"][0]:
        return {
            "message": "No relevant information found.",
            "results": []
        }

    context = "\n\n".join(results["documents"][0])

    answer = generate_answer(
        context=context,
        question=request.question
    )

    return {
        "message": "Answer generated successfully.",
        "answer": answer,
        "context": results["documents"][0]
    }