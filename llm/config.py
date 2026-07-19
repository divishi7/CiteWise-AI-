# File Name: config.py
# Purpose: Initializes the Gemini LLM used throughout the CiteWise AI project.

from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from the .env file
load_dotenv()

# Read the API key from .env
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file.")

# Model name
MODEL = "gemini-flash-latest"

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model=MODEL,
    google_api_key=API_KEY,
    temperature=0.2
)