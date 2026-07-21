from fastapi import APIRouter
from pydantic import BaseModel

from rag.retriever import Retriever
from backend.gemini_service import generate_answer

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):
    print("=== /chat endpoint hit ===")
    print("Question:", request.question)

    retriever = Retriever()

    results = retriever.retrieve(request.question)
    print("Retriever output:", results)

    if not results["documents"] or not results["documents"][0]:
        print("No documents found.")
        return {
            "message": "No relevant information found.",
            "results": []
        }

    context = "\n\n".join(results["documents"][0])
    print("Context length:", len(context))

    print("Calling Gemini...")
    answer = generate_answer(
        context=context,
        question=request.question
    )

    print("Gemini answer:", answer)

    return {
        "message": "Answer generated successfully.",
        "answer": answer,
        "context": results["documents"][0]
    }