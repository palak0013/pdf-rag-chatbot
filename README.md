# AI-Powered PDF RAG Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions based on their content.

The application processes uploaded documents, splits the extracted text into chunks, generates vector embeddings, stores them in ChromaDB, retrieves relevant context for a user query, and uses Google Gemini to generate a context-aware response.

The application also displays the retrieved source chunks, providing transparency into the context used to generate each answer.

## Live Demo

[Try the AI-Powered PDF RAG Chatbot](https://pdf-rag-chatbot1.streamlit.app/)

## GitHub Repository

[View Source Code](https://github.com/palak0013/pdf-rag-chatbot)

---

## Features

- Upload one or multiple PDF documents
- Extract text from PDF files
- Split documents into smaller chunks
- Generate vector embeddings
- Store embeddings using ChromaDB
- Perform semantic similarity search
- Retrieve relevant document chunks
- Generate answers using Google Gemini
- Display retrieved source chunks
- Interactive Streamlit interface
- Environment-based API key management
- Modular RAG pipeline using LangChain

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core application development |
| Streamlit | Web interface and application deployment |
| LangChain | RAG pipeline and document processing |
| ChromaDB | Vector database and similarity search |
| PyPDF | PDF text extraction |
| Google Gemini | Large Language Model for answer generation |
| python-dotenv | Environment variable management |

---

## Project Structure

```text
PDF-RAG/
│
├── utils/
│   ├── loader.py          # Loads and extracts text from PDFs
│   ├── splitter.py        # Splits documents into text chunks
│   ├── vectorstore.py     # Creates embeddings and manages ChromaDB
│   └── rag.py             # Retrieval and LLM-based answer generation
│
├── app.py                 # Main Streamlit application
├── models.py              # Model and API configuration
│
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignored files
└── .env.example           # Environment   variable template

```
---

## RAG Pipeline

```text
                 PDF Upload
                     │
                     ▼
             ┌───────────────┐
             │ PDF Extraction│
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │ Text Splitting│
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   Embeddings  │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   ChromaDB    │
             │ Vector Store  │
             └───────┬───────┘
                     │
                User Question
                     │
                     ▼
             ┌───────────────┐
             │Semantic Search│
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │Relevant Chunks│
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │ Google Gemini │
             └───────┬───────┘
                     │
                     ▼
               Final Answer

```
----

## How it works

### 1. PDF Upload

Users can upload one or multiple PDF documents through the Streamlit interface.

### 2. Document Loading

The application extracts text from the uploaded PDF files using a PDF document loader.

### 3. Text Splitting

The extracted text is divided into smaller chunks to improve retrieval efficiency and provide relevant context to the language model.

### 4. Embedding Generation

The document chunks are converted into vector representations that capture their semantic meaning.

### 5. Vector Storage

The generated embeddings are stored in ChromaDB.

### 6. Query Processing

When a user asks a question, the query is processed and used to search the vector database.

### 7. Context Retrieval

ChromaDB performs similarity search and retrieves the most relevant document chunks.

### 8. Answer Generation

The retrieved context and user query are passed to Google Gemini to generate the final answer.

### 9. Source Transparency

The application displays the retrieved source chunks so users can inspect the context used to generate the response.

---
## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/palak0013/pdf-rag-chatbot.git
cd pdf-rag
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

Do not commit the `.env` file to GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the application at:

```text
http://localhost:8501
```

### 6. Use the Application

1. Upload your PDF.
2. Click **Process PDFs**.
3. Ask questions about the PDF.
4. View the answer and retrieved sources.



## Use Cases

This application can be used for:

- Research papers
- Study materials
- Technical documentation
- Academic documents
- Reports
- Resumes
- Books and manuals
- Company documents

---