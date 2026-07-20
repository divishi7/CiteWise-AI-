import json
from fastapi import APIRouter
from pydantic import BaseModel

from rag.retriever import Retriever
from backend.gemini_service import generate_answer

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    retriever = Retriever()

    results = retriever.retrieve(request.question)

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

with open("testing_features/latest_run.json", "w") as f:
    json.dump({"chunks": results["documents"][0], "answer": answer}, f)