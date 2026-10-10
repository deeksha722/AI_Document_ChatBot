# AI Document Chatbot using RAG

An AI-powered document question-answering application that allows users to upload PDF documents and ask questions in natural language. The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from documents and generate context-aware answers using a Large Language Model (LLM).

## Overview

Traditional chatbots generate responses from their learned knowledge, which may not contain information from a user's specific documents. This project addresses that limitation by retrieving relevant text from uploaded PDFs and providing it as context to an LLM before generating an answer.

The application combines document processing, text chunking, semantic embeddings, vector search, and LLM-based response generation in a modular Python application.

## Features

- **PDF Document Processing:** Extracts text from uploaded PDF documents.
- **Text Chunking:** Splits extracted text into smaller chunks for efficient retrieval.
- **Semantic Embeddings:** Converts text chunks into numerical vector representations using Sentence Transformers.
- **Vector Database:** Stores and retrieves document chunks using ChromaDB.
- **Context-Aware Question Answering:** Retrieves relevant document content and uses Groq-powered LLM inference to generate answers.
- **Interactive Web Interface:** Provides a user-friendly interface built with Streamlit.
- **Modular Architecture:** Separates document processing, embedding creation, storage, retrieval, answer generation, and UI logic into individual Python modules.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| PyPDF | PDF text extraction |
| Sentence Transformers | Text embedding generation |
| ChromaDB | Vector storage and similarity search |
| Groq API | LLM inference and answer generation |
| python-dotenv | Environment variable management |

## How It Works

1. **Upload:** The user uploads a PDF document.
2. **Extract:** Text is extracted from the PDF.
3. **Chunk:** The extracted text is divided into smaller chunks.
4. **Embed:** Each chunk is converted into an embedding vector.
5. **Store:** The embeddings and associated text are stored in ChromaDB.
6. **Retrieve:** When the user asks a question, semantically relevant chunks are retrieved.
7. **Generate:** The retrieved context and question are sent to the Groq API.
8. **Respond:** The generated answer is displayed in the Streamlit interface.

## Project Structure

```text
AI_Document_ChatBot/
│
├── app.py                  # Main application entry point
├── ui.py                   # Streamlit UI and styling
├── read_pdf.py             # PDF text extraction
├── chunk_text.py           # Text chunking
├── create_embeddings.py    # Embedding configuration
├── store_chunks.py         # ChromaDB storage
├── search_chunks.py        # Relevant chunk retrieval
├── generate_answer.py      # LLM answer generation
├── requirements.txt        # Project dependencies
├── .gitignore              # Excluded files and folders
├── .env                    # Local API key configuration
└── README.md               # Project documentation
```

**Note:** `.env`, virtual environment folders, and generated vector database files should remain local and must not be committed to GitHub.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Document_ChatBot.git
cd AI_Document_ChatBot
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv rag_env
```

Activate it on Windows PowerShell:

```powershell
.\rag_env\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Groq API Key

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own Groq API key. Never commit the `.env` file or expose your API key publicly.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## Learning Outcomes

- Understanding the Retrieval-Augmented Generation (RAG) workflow.
- Working with PDF text extraction and text chunking.
- Generating and using semantic embeddings.
- Performing similarity-based retrieval with a vector database.
- Integrating an LLM API into a Python application.
- Building a modular AI application with Streamlit.

## Future Enhancements

- Support for multiple document formats.
- Improved source references and page-level citations.
- Enhanced conversation memory and retrieval strategies.
- Deployment to a cloud hosting platform.
- Support for multiple PDF documents in a single conversation.

## Security

API credentials are managed through environment variables. Keep `.env` and other sensitive configuration files out of version control.

## Author

**Deeksha Ravikumar**

GitHub: [Add your GitHub profile URL here]https://github.com/deeksha722

---

*This project was developed as a hands-on learning project exploring Retrieval-Augmented Generation, semantic search, vector databases, and LLM integration.*
