# ⚖️ US Tax & Legal RAG System

A Hybrid Retrieval-Augmented Generation (RAG) system for answering questions from US Tax & Legal documents using ChromaDB, Elasticsearch Cloud, Groq LLM, and Streamlit.

The system combines semantic retrieval with keyword-based search to provide accurate answers along with document-level citations. Elasticsearch Cloud is used for keyword retrieval, while Groq (Llama 3.3 70B) is used for answer generation.

---

# Project Overview

Legal and tax documents are often large, complex, and difficult to search manually. Traditional keyword search frequently misses semantically relevant information, while vector search alone may overlook exact legal terminology.

This project addresses these limitations by implementing a **Hybrid Retrieval-Augmented Generation (Hybrid RAG)** pipeline that combines:

- Semantic Search using ChromaDB
- Keyword Search using Elasticsearch
- Query Expansion
- Cloud-based LLM Inference using Groq

The retrieved documents are passed to the LLM, which generates responses strictly based on the retrieved context while also providing document citations and page references.

---
# Project Highlights

- Hybrid Retrieval using ChromaDB and Elasticsearch Cloud
- Query Expansion for IRS Forms and Publications
- LLM inference using Groq (Llama 3.3 70B)
- Streamlit-based web interface
- Document-level source citations
- 100% Retrieval Accuracy on the Golden Set
- Cloud-based deployment using Elastic Cloud and Groq API
---
# Key Features

- Hybrid Retrieval (Vector Search + Keyword Search)
- ChromaDB Vector Database
- Elasticsearch Cloud Keyword Search
- Query Expansion for IRS Forms and Publications
- Groq LLM (Llama 3.3 70B)
- Streamlit-based User Interface
- Source Citations with Document Name and Page Number
- Golden Set Evaluation
- Retrieval Accuracy Evaluation
- Semantic Faithfulness Evaluation
- Cloud-based Deployment
- Modular Project Structure

---

# System Architecture

![Architecture Diagram](architecture/architecture_diagram.png)

---

# Workflow

```
                           PDF Documents
                                 │
                                 ▼
                        PDF Parsing (PyMuPDF)
                                 │
                                 ▼
                       Text Extraction & Metadata
                                 │
                                 ▼
                         Document Chunking
                                 │
                ┌────────────────┴────────────────┐
                ▼                                 ▼
      Embedding Generation         Elasticsearch cloud
 (BAAI/bge-small-en-v1.5)                Keyword Index
                │                                 │
                ▼                                 ▼
            ChromaDB                      Keyword Search
                │                                 │
                └──────────────┬──────────────────┘
                               ▼
                      Hybrid Retrieval
               (Vector + Keyword + Query Expansion)
                               │
                               ▼
                     Context Construction
                               │
                               ▼
                     Groq (Llama 3.3 70B)
                               │
                               ▼
             Answer Generation with Citations
                               │
                               ▼
                     Streamlit Web Interface
```

---

# Dataset

The project is built on a collection of official US Tax & Legal PDF documents organized into multiple legal categories, including IRS Publications, IRS Forms, Acts, Court Judgements, Internal Revenue Bulletins, and other tax-related resources.

## Categories

- Acts
- Court Judgements
- IRS Forms
- IRS Publications
- Internal Revenue Bulletin
- POV (Point of View)
- Tax Documents

---

# Data Processing Pipeline

Each document passes through the following stages:

1. PDF Parsing
2. Text Extraction
3. Text Cleaning
4. Document Chunking
5. Metadata Extraction
6. Embedding Generation
7. ChromaDB Indexing
8. Elasticsearch Cloud Indexing

---

# Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| LLM | Groq (Llama 3.3 70B) |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Vector Database | ChromaDB |
| Search Engine | Elasticsearch Cloud |
| PDF Parser | PyMuPDF |
| UI | Streamlit |
| Evaluation | Sentence Transformers |
| Deployment | Streamlit Community Cloud |
| Version Control | Git & GitHub |

---

# Project Structure

US-Tax-Legal-RAG/
│
├── architecture/
│   └── architecture_diagram.png
│
├── dataset/
│
├── elasticsearch/
│   └── index_documents.py
│
├── evaluation/
│   ├── evaluate.py
│   ├── evaluation_report.md
│   ├── evaluation_results.csv
│   ├── faithfulness.py
│   └── golden_set.csv
│
├── indexing/
│   └── vector_store.py
│
├── llm/
│   └── legal_assistant.py
│
├── output/                  # Generated after parsing (ignored by Git)
│   ├── legal_documents.json
│   └── chunks.json
│
├── parser/
│   └── pdf_parser.py
│
├── preprocessing/
│   └── chunking.py
│
├── retriever/
│   ├── hybrid_retriever.py
│   └── retriever.py
│
├── vector_db/               # Generated after indexing (ignored by Git)
│
├── app.py
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

---

# Installation

## Prerequisites

Before running the project, make sure the following software is installed:

- Python 3.11 or later
- Internet Connection
- Elastic Cloud Account
- Groq API Key
- Git
- Visual Studio Code (Recommended)

---

# How to Run the Project

Follow the steps below to set up and run the project from scratch.

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/100rabh-creator/US-Tax-Legal-RAG.git
cd US-Tax-Legal-RAG
```

If you are using the ZIP version, simply extract the project and open the project folder.

---

## Step 2: Create a Virtual Environment

```bash
python3 -m venv .venv
```

---

## Step 3: Activate the Virtual Environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## Step 4: Install Required Packages

Install all required Python dependencies.

```bash
pip install -r requirements.txt
```

If you're using **GitHub Codespaces**, make sure Python **3.11** is selected before installing the dependencies.

You can verify your Python version using:

```bash
python3 --version
```

Expected output:

```text
Python 3.11.x
```

---

---
## Step 5: Configure Environment Variables

Create a `.env` file in the project root.

```env
ELASTIC_CLOUD_ID=YOUR_ELASTIC_CLOUD_ID
ELASTIC_API_KEY=YOUR_ELASTIC_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

> **Note:** The `.env` file is excluded from version control. Use the provided `.env.example` file as a reference.

---


## Step 6: Parse PDF Documents

Extract text and metadata from all US Tax & Legal PDF documents.

```bash
python parser/pdf_parser.py
```

Output:

```
output/legal_documents.json
```

---

## Step 7: Create Text Chunks

Split parsed documents into chunks with metadata.

```bash
python preprocessing/chunking.py
```

Output:

```
output/chunks.json
```

---

## Step 8: Create the ChromaDB Vector Database

Generate embeddings and create the vector database.

```bash
python indexing/vector_store.py
```

Output:

```
vector_db/
```

---

## Step 9: Index Documents into Elasticsearch Cloud

Upload all parsed documents into Elasticsearch Cloud.

```bash
python elasticsearch/index_documents.py
```

> **Note:** Before running this script, configure the following variables inside your `.env` file:

```env
ELASTIC_CLOUD_ID=YOUR_ELASTIC_CLOUD_ID
ELASTIC_API_KEY=YOUR_ELASTIC_API_KEY
```

---

## Step 10: Test Hybrid Retrieval

Run the Hybrid Retriever.

```bash
python retriever/hybrid_retriever.py
```

Example Query:

```
What is Section 179?
```

Expected Output:

- Semantic Search Results
- Keyword Search Results
- Hybrid Search Results

---

## Step 11: Run the Legal Assistant

The project uses **Groq (Llama 3.3 70B)** as the Large Language Model.

Example Query:

```
What is Section 179?
```

Expected Response:

```
Answer

Section 179 allows businesses to immediately deduct the cost of qualifying business property instead of depreciating it over multiple years, subject to IRS rules and limitations.

Summary

Section 179 provides an immediate tax deduction for eligible business assets.

Source Citations

Document: p946.pdf
Page: 16

Document: p463.pdf
Page: 2
```

---

## Step 12: Launch the Streamlit Application

Run:

```bash
streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false
```

Open your browser.

```
http://localhost:8501
```

You can now:

- Ask legal and tax related questions
- Retrieve relevant legal documents
- Generate context-aware answers
- View document citations
- Explore Hybrid Retrieval results

---

# Evaluation

The project includes an evaluation pipeline for measuring retrieval quality.

---

## Retrieval Accuracy

Run:

```bash
python evaluation/evaluate.py
```

Output:

- Total Questions
- Correct Retrievals
- Retrieval Accuracy
- evaluation_results.csv

---

## Semantic Faithfulness

Run:

```bash
python evaluation/faithfulness.py
```

Output:

- Faithful Answers
- Needs Review
- Not Faithful
- Overall Faithfulness Score

# Expected Project Workflow

```
Dataset
      │
      ▼
PDF Parser (PyMuPDF)
      │
      ▼
legal_documents.json
      │
      ▼
Chunking
      │
      ▼
chunks.json
      │
      ├──────────────┐
      ▼              ▼
Vector Store   Elasticsearch Cloud
      │              │
      ▼              ▼
 ChromaDB     Keyword Search
        \          /
         \        /
          ▼      ▼
      Hybrid Retrieval
             │
             ▼
      Groq (Llama 3.3)
             │
             ▼
        Streamlit UI
```

---

# Hybrid Retrieval Pipeline

The system combines **semantic search** with **keyword search** for improved retrieval accuracy.

## Semantic Search

Semantic retrieval is performed using:

- ChromaDB
- BAAI/bge-small-en-v1.5 Embeddings

This retrieves documents that are semantically related even if exact keywords are absent.

---

## Keyword Search

Keyword retrieval is performed using **Elasticsearch Cloud**.

Indexed Fields:

- Document
- Category
- Content
- Page Number

This is particularly useful for IRS Forms, Publications and legal terminology.

---

## Query Expansion

Common legal queries are automatically expanded.

Examples:

| User Query | Expanded Query |
|------------|----------------|
| Form W-4 | IRS Form W-4 Employee Withholding Certificate |
| Form W-9 | IRS Form W-9 Request for Taxpayer Identification Number |
| Form 4562 | IRS Form 4562 Depreciation and Amortization |
| Publication 463 | IRS Publication 463 Travel Gift and Car Expenses |
| Publication 527 | IRS Publication 527 Residential Rental Property |
| Publication 550 | IRS Publication 550 Investment Income and Expenses |
| Publication 946 | IRS Publication 946 Depreciation |
| Section 179 | IRS Section 179 Deduction |

Query Expansion improves retrieval quality for IRS forms and publications.

---

# Future Improvements

- Cross Encoder Re-ranking
- Reciprocal Rank Fusion (RRF)
- Graph RAG
- Metadata-aware Retrieval
- Better Embedding Models
- Incremental Indexing
- REST API using FastAPI
- LLM-as-a-Judge Evaluation
- User Authentication
- Conversation Memory
- Multi-turn Question Answering

---

# Troubleshooting

## ChromaDB Missing

```bash
python indexing/vector_store.py
```

---

## Elasticsearch Cloud Connection Error

Verify:

```text
ELASTIC_CLOUD_ID
ELASTIC_API_KEY
```

inside your `.env` file.

---

## Groq API Error

Verify:

```text
GROQ_API_KEY
```

inside your `.env` file.

---

## ModuleNotFoundError

Run:

```bash
pip install -r requirements.txt
```

---

# Performance Summary

| Component | Status |
|-----------|--------|
| PDF Parsing | ✅ |
| Chunking | ✅ |
| ChromaDB | ✅ |
| Elasticsearch Cloud | ✅ |
| Hybrid Retrieval | ✅ |
| Query Expansion | ✅ |
| Groq LLM | ✅ |
| Streamlit UI | ✅ |
| Source Citations | ✅ |
| Golden Set Evaluation | ✅ |
| Retrieval Accuracy | **100%** |
| Semantic Faithfulness | **50%** |

---

# Author

**Saurabh Raj**

Master of Computer Applications (MCA)  
National Institute of Technology (NIT) Jamshedpur

GitHub: https://github.com/100rabh-creator

---

# Acknowledgements

This project demonstrates a Hybrid Retrieval-Augmented Generation (Hybrid RAG) system for US Tax & Legal question answering.

Technologies used:

- Python
- LangChain
- ChromaDB
- Elasticsearch Cloud
- Groq
- Streamlit
- Hugging Face Transformers
- Sentence Transformers
- PyMuPDF

# Deployment

The application is designed for deployment on **Streamlit Community Cloud**.

## Required Deployment Secrets

Configure the following secrets in your Streamlit Cloud application:

```env
ELASTIC_CLOUD_ID=YOUR_ELASTIC_CLOUD_ID
ELASTIC_API_KEY=YOUR_ELASTIC_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

### Deployment Architecture

The deployed application uses:

- **Elasticsearch Cloud** for keyword-based retrieval
- **ChromaDB** for semantic vector search
- **Groq (Llama 3.3 70B)** for answer generation
- **Streamlit Community Cloud** for the web interface

> **Note:** Never commit your `.env` file or API keys to GitHub. Use `.env.example` as a template for local development.

---

⭐ Feel free to explore, extend, or build upon this project for learning and research purposes.
