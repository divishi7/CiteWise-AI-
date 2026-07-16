from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.upload import router as upload_router
from backend.chat import router as chat_router
app = FastAPI(
    title="CiteWise AI Backend",
    version="1.0.0",
    description="Backend API for CiteWise AI"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CiteWise AI Backend!",
        "status": "Running"
    }

app.include_router(upload_router)
app.include_router(chat_router)
