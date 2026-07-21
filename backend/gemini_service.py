import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API key from .env
API_KEY = os.getenv("API_KEY")

print("API Key Loaded:", API_KEY is not None)

if not API_KEY:
    raise ValueError("API_KEY not found in .env file")

# Initialize Gemini client
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
        model="gemini-flash-latest",
        contents=prompt,
    )

    return response.text