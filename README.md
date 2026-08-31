# 🔎 CiteWise AI

### AI-Powered Document Question Answering with Reliable Citations

CiteWise AI is an AI-powered document question-answering system built around a **Retrieval-Augmented Generation (RAG)** workflow.

The project allows users to interact with their documents through natural-language questions and receive AI-generated answers based on the information retrieved from the provided documents, along with relevant citations for better transparency and traceability.

The project was developed as a **capstone project during the Summer Internship Program 2026 in Generative & Agentic AI Systems Development**, organized by the Department of Information Technology, IGDTUW, in association with Sansoftech Services Private Limited.

---

## ✨ Key Features

- 📄 **Document Processing**
  - Process user-provided documents for downstream question answering.

- 🔍 **Retrieval-Augmented Generation**
  - Retrieve relevant information from documents before generating an answer.

- 🤖 **LLM-Powered Responses**
  - Generate natural-language answers using retrieved document context.

- 📚 **Citation Support**
  - Provide supporting source information along with generated responses.

- ✅ **Citation Verification**
  - Includes dedicated functionality for testing and verifying citations.

- 💬 **Interactive User Interface**
  - Frontend interface for interacting with the document question-answering system.

- ⚙️ **Modular Architecture**
  - Separate components for the frontend, backend, RAG pipeline, LLM functionality, and testing.

---

## 🧠 How It Works

The overall workflow of CiteWise AI can be represented as:

```text
                    ┌─────────────────────┐
                    │     User Uploads    │
                    │      Document       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Document Processing │
                    │ & Text Preparation  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   RAG / Retrieval   │
                    │ Relevant Information│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    LLM Generation   │
                    │ Context-based Answer│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Answer + Citations  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   User Interface    │
                    └─────────────────────┘
```

The central idea is to ground the generated response in information retrieved from the user's documents rather than relying only on the model's internal knowledge.

---

## 🏗️ Project Structure

```text
CiteWise-AI/
│
├── backend/
│   └── Backend API and application logic
│
├── frontend/
│   └── User interface and frontend components
│
├── llm/
│   └── LLM-related functionality
│
├── rag/
│   └── Retrieval-Augmented Generation pipeline
│
├── testing_features/
│   └── Citation verification and testing functionality
│
├── tests/
│   └── Project tests
│
├── main.py
│   └── Main application entry point
│
├── requirements.txt
│   └── Python dependencies
│
├── pyproject.toml
│   └── Project configuration and dependencies
│
└── README.md
```

---

## 🛠️ Technology & Concepts

The project focuses on the following areas:

### Generative AI
- Large Language Models (LLMs)
- Prompt-based answer generation
- Context-grounded responses

### Retrieval-Augmented Generation
- Document processing
- Text preparation and retrieval
- Context-aware response generation

### Software Development
- Python
- Backend development
- Frontend development
- Modular project architecture
- Testing and validation

### Responsible AI
- Reducing unsupported/generated information through document grounding
- Citation and source traceability
- Improving transparency of AI-generated answers

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/divishi7/CiteWise-AI-.git
cd CiteWise-AI-
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

If the project requires API keys or other configuration values, create a `.env` file in the appropriate project directory and add the required credentials.

> **Do not commit API keys or other secrets to GitHub.**

### 5. Run the Application

Run the project using the appropriate entry point configured in the repository.

For the backend/API, the project can be started using the project's configured Python application entry point.

---

## 💡 Why CiteWise AI?

Traditional document search often requires users to manually locate and interpret relevant information.

CiteWise AI aims to make this process more interactive by allowing users to **ask questions in natural language** and receive answers based on the information retrieved from their documents.

The addition of citations also makes it easier for users to understand **where the answer came from**, which is particularly important when working with research papers, technical documents, reports, and other information-heavy content.

---

## 🎯 Project Objectives

The primary objectives of CiteWise AI are to:

1. Build an effective document-based question-answering system.
2. Apply Retrieval-Augmented Generation to improve contextual accuracy.
3. Generate answers grounded in user-provided information.
4. Provide citation support for generated responses.
5. Create a modular and maintainable AI application.
6. Explore practical applications of Generative AI and LLM-based systems.

---

## 🔬 Capstone Project

CiteWise AI was developed as the capstone project for the:

**Summer Internship Program 2026**  
**Generative & Agentic AI Systems Development**

Organized by:

**Department of Information Technology**  
**Indira Gandhi Delhi Technical University for Women (IGDTUW)**

In association with:

**Sansoftech Services Private Limited**

**Duration:** June 8, 2026 – July 17, 2026

---
## 🔮 Future Scope

Potential improvements for CiteWise AI include:

- Support for additional document formats
- Improved retrieval and ranking techniques
- More advanced citation verification
- Conversation history and multi-turn document conversations
- Improved evaluation metrics for RAG performance
- Support for multiple documents and knowledge bases
- More robust hallucination detection
- Enhanced user interface and accessibility

---

## 👥 Contributors

This project was developed collaboratively as part of the Summer Internship Program 2026.

Contributors:

- Aashnee Sethi
- Divishi Chaudhary
- Anshul Garg
- Astha Paswan
- Alfia Khatoon

---

## 📌 Repository

**GitHub:**  
https://github.com/divishi7/CiteWise-AI-

---

## 📄 License

This project was developed for educational and internship purposes.

---

### ⭐ If you find this project interesting, consider giving the repository a star!
