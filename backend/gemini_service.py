import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_answer(context: str, question: str):
    prompt = f"""
You are an AI assistant for question answering over documents.

Use ONLY the context below to answer the user's question.

If the answer is not present in the context, reply:
"I couldn't find the answer in the uploaded document."

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text