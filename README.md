# CiteWise AI

CiteWise AI is an AI-powered research assistant built using Retrieval-Augmented Generation (RAG). It enables users to upload one or multiple PDF documents, retrieve relevant information from the uploaded documents, and generate context-aware answers using Google's Gemini models. The project also includes citation verification and conflict detection modules to evaluate the reliability of generated responses.

---

# Table of Contents

- Features
- Tech Stack
- Project Structure
- Installation & Setup
- Usage
- Testing
- Contributors
- Licence

---

## Features

- Upload and process one or multiple PDF documents
- PDF text extraction and preprocessing
- Text chunking for efficient retrieval
- Vector embeddings with ChromaDB
- Retrieval-Augmented Generation (RAG)
- AI-generated answers using Google Gemini
- Citation verification
- Conflict detection
- FastAPI backend
- React frontend

---

## Tech Stack

### Frontend
- React
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn

### AI & RAG
- Google Gemini
- LangChain
- ChromaDB
- Sentence Transformers

### Utilities
- PyMuPDF
- python-dotenv
- pytest

---

## Project Structure

```text
CiteWise-AI/
│
├── backend/
├── frontend/
├── rag/
├── llm/
├── tests/
├── testing_features/
├── logs/
├── data/
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Installation & Setup

Active Development Branch: integration

### 1. Clone the repository

```bash
git clone https://github.com/divishi7/CiteWise-AI-
cd CiteWise-AI-
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root and add:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4. Install frontend dependencies

```bash
cd frontend
npm install
cd ..
```

### 5. Start the backend

```bash
uvicorn backend.main:app --reload
```

### 6. Start the frontend

Open a **new terminal** and run:

```bash
cd frontend
npm start
```

### 7. (Optional) Run the verification test suite

```bash
cd testing_features
pytest -v
```

---

## Usage

1. Open the application in your browser:

   ```
   http://localhost:3000
   ```

2. Upload one or more PDF documents.

3. Enter a question related to the uploaded document(s).

4. The system retrieves relevant document chunks and generates an answer using Google's Gemini model.

5. Citation verification and conflict detection are performed internally on the generated response.

---

## View the Verification Report

To inspect citation verification and conflict detection results, run:

```bash
cd testing_features
python run_pipeline_demo.py
```

This command reads the latest request stored in `latest_run.json` and generates a detailed verification report, including citation accuracy, per-claim verification, and detected conflicts.

---

## Testing

The project includes test modules for validating components of the RAG pipeline, including document loading, text splitting, embeddings, retrieval, and vector storage.

---

## Contributors

- Alfia Khatoon
- Divishi Chaudhary
- Astha Paswan
- Aashnee Sethi
- Anshul Garg

---
## License

Developed for educational and academic purposes.
