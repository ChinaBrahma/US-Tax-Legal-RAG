# System Architecture

# US Tax & Legal Hybrid RAG System

## Overview

The US Tax & Legal Hybrid RAG System is designed to answer user queries from official US Tax and Legal documents using a combination of semantic search, keyword search, and Large Language Models (LLMs).

Instead of relying only on an LLM, the system first retrieves the most relevant information from a curated document collection and then generates responses using only the retrieved context. This approach improves factual accuracy and reduces hallucinations.

---

# High-Level Architecture

```
                   User Question
                         │
                         ▼
                 Streamlit Web UI
                         │
                         ▼
                Hybrid Retrieval Engine
            ┌────────────┴────────────┐
            ▼                         ▼
     ChromaDB (Semantic)     Elasticsearch Cloud
            ▼                         ▼
        Retrieved Documents & Metadata
                     │
                     ▼
              Context Construction
                     │
                     ▼
          Groq (Llama 3.3 70B)
                     │
                     ▼
         Answer with Source Citations
```

---

# Components

## 1. PDF Parser

The parser extracts text from all PDF documents using **PyMuPDF**.

For every page, the following information is extracted:

- Document Name
- Category
- Page Number
- Text Content

The extracted data is stored as structured JSON for further processing.

---

## 2. Document Chunking

Large legal documents are divided into smaller overlapping chunks.

Chunking helps improve retrieval quality while preserving important legal context.

Each chunk stores:

- Chunk ID
- Document Name
- Category
- Page Number
- Text Content

---

## 3. ChromaDB

ChromaDB stores vector embeddings generated using the **BAAI/bge-small-en-v1.5** embedding model.

It is responsible for semantic similarity search.

Semantic search retrieves relevant information even when the user's wording differs from the original document.

---

## 4. Elasticsearch Cloud

Elasticsearch Cloud provides keyword-based retrieval.

It indexes:

- Document Name
- Category
- Page Number
- Content

Keyword search is especially useful for:

- IRS Forms
- IRS Publications
- Section Numbers
- Legal Terminology

---

## 5. Hybrid Retrieval

Hybrid Retrieval combines results from:

- ChromaDB (Semantic Search)
- Elasticsearch Cloud (Keyword Search)

The combined results improve retrieval accuracy by leveraging the strengths of both search techniques.

---

## 6. Query Expansion

Frequently used legal terms are expanded before retrieval.

Examples include:

- Form W-4
- Form W-9
- Publication 463
- Publication 946
- Section 179

Query expansion improves search accuracy for common legal references.

---

## 7. Groq LLM

The retrieved document context is passed to **Groq (Llama 3.3 70B)**.

The model is instructed to:

- Answer only from retrieved documents.
- Avoid hallucinations.
- Return concise responses.
- Provide document citations.

---

## 8. Streamlit Interface

The Streamlit application provides a simple interface where users can:

- Enter legal questions
- Retrieve relevant documents
- View generated answers
- View supporting document citations

---

# System Workflow

1. User submits a legal question.
2. The query is expanded if required.
3. Semantic search retrieves documents from ChromaDB.
4. Keyword search retrieves documents from Elasticsearch Cloud.
5. Hybrid Retrieval merges both result sets.
6. Retrieved context is passed to Groq Llama 3.3.
7. The generated answer is displayed along with source citations.

---

# Technologies Used

- Python
- LangChain
- ChromaDB
- Elasticsearch Cloud
- Groq
- Streamlit
- PyMuPDF
- Hugging Face Embeddings

---

# Advantages

- Hybrid Retrieval improves search accuracy.
- Semantic and keyword search complement each other.
- Groq provides fast LLM inference.
- Elasticsearch Cloud removes the need for local search infrastructure.
- Source citations improve answer transparency and explainability.

---

# Future Enhancements

- Cross-Encoder Re-ranking
- Reciprocal Rank Fusion (RRF)
- Graph RAG
- Conversation Memory
- FastAPI REST API
- User Authentication
- Multi-turn Question Answering
- Advanced Evaluation Metrics