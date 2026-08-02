from collections import defaultdict

from fastapi import APIRouter
from pydantic import BaseModel

from rag.retriever import Retriever
from backend.gemini_service import (
    generate_answer,
    generate_cross_analysis,
)

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    retriever = Retriever()

    results = retriever.retrieve(request.question)

    print("\n========== RETRIEVAL RESULTS ==========\n")
    print("Documents:")
    print(results["documents"][0])

    print("\nMetadata:")
    print(results["metadatas"][0])

    print("\n=======================================\n")

    if not results["documents"] or not results["documents"][0]:
        return {
            "message": "No relevant information found.",
            "results": []
        }

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = "\n\n".join(documents)

    try:
        answer = generate_answer(
            context=context,
            question=request.question
        )
    except Exception as e:
        print("Answer Error:", e)
        answer = "Failed to generate answer."

    grouped_context = defaultdict(list)

    for doc, meta in zip(documents, metadatas):
        grouped_context[meta["source"]].append({
            "page": meta["page"],
            "text": doc
        })

    if len(grouped_context) >= 2:
        try:
            cross_analysis = generate_cross_analysis(grouped_context)
        except Exception as e:
            print("Cross Analysis Error:", e)
            cross_analysis = "Cross analysis unavailable."
    else:
        cross_analysis = "Only one document contributed."

    import json

    with open("testing_features/latest_run.json", "w") as f:
        json.dump({"chunks": documents, "answer": answer}, f)

    return {
        "message": "Answer generated successfully.",
        "answer": answer,
        "context": documents,
        "sources": metadatas,
        "cross_analysis": cross_analysis
    }
