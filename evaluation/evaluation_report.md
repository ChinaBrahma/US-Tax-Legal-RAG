# US Tax & Legal RAG System

# Evaluation Report

---

# 1. Project Overview

This project implements a Hybrid Retrieval-Augmented Generation (RAG) system for the US Tax & Legal domain. The objective is to enable users to ask legal and tax-related questions in natural language and receive accurate answers generated only from official legal documents along with document-level citations.

The system combines semantic retrieval using ChromaDB with keyword-based retrieval using Elasticsearch to improve search accuracy and provide reliable responses.

---

# 2. System Architecture

The following architecture illustrates the complete workflow of the Hybrid RAG system.

![Architecture Diagram](../architecture/architecture_diagram.png)

The workflow consists of:

- PDF Document Collection
- PDF Parsing and Text Extraction
- Text Preprocessing
- Document Chunking
- Embedding Generation using BAAI/bge-small-en-v1.5
- ChromaDB Vector Indexing
- Elasticsearch Keyword Indexing
- Hybrid Retrieval (Vector Search + Keyword Search + Query Expansion)
- Context Generation
- Answer Generation using Llama 3.2 (Ollama)
- Streamlit User Interface
- Source Citation Generation

---

# 3. Dataset

The system processes approximately **100 US Tax & Legal PDF documents** organized into the following categories:

- Acts
- Court Judgements
- IRS Forms
- IRS Publications
- Internal Revenue Bulletin
- POV (Point of View)
- Tax Documents

Each document passes through the following pipeline:

- PDF Parsing
- Text Extraction
- Text Cleaning
- Chunk Generation
- Metadata Extraction
- Embedding Generation
- ChromaDB Indexing
- Elasticsearch Indexing

---

# 4. Retrieval Pipeline

The implemented Hybrid Retrieval pipeline consists of:

- ChromaDB Semantic Search
- Elasticsearch Keyword Search
- Query Expansion
- Hybrid Search
- Duplicate Removal
- Context Builder
- Source Citation Generation

The retrieved context is passed to the locally running **Llama 3.2** model through **Ollama** for answer generation.

---

# 5. Evaluation Method

A Golden Set containing **10 representative legal questions** was created for evaluation.

For every query:

1. Hybrid Search retrieves the most relevant documents.
2. Retrieved documents are compared with the expected source document.
3. Retrieval is considered correct if the expected document appears within the retrieved results.
4. Generated answers are further evaluated using Semantic Faithfulness.

---

# 6. Retrieval Accuracy

## Evaluation Results

- Total Questions: **10**
- Correct Retrievals: **10**
- Incorrect Retrievals: **0**

## Retrieval Accuracy

**100%**

The Hybrid Retrieval pipeline successfully retrieved the expected source document for every query in the Golden Set.

---

# 7. Semantic Faithfulness

Semantic Faithfulness was evaluated by comparing generated answers with the corresponding ground-truth answers using Sentence Transformers.

### Embedding Model

- all-MiniLM-L6-v2

### Evaluation Results

- Faithful Answers: **5**
- Needs Review: **4**
- Not Faithful: **1**

## Semantic Faithfulness

**50%**

This evaluation measures semantic similarity rather than factual correctness judged by another LLM.

---

# 8. Observations

## Strengths

- Hybrid Retrieval significantly improved search quality compared to Vector Search alone.
- Elasticsearch improved exact legal keyword matching.
- ChromaDB retrieved semantically relevant legal information.
- Query Expansion improved retrieval for IRS Forms and IRS Publications.
- Source citations include both document names and page numbers.
- The complete system runs locally using Ollama without requiring external LLM APIs.
- The final Hybrid Retrieval pipeline achieved **100% Retrieval Accuracy** on the Golden Set.

## Current Limitations

- Faithfulness evaluation currently relies on semantic similarity instead of an LLM-as-a-Judge framework.
- Retrieval ranking can be further improved using reranking models.
- Graph-based relationships between legal documents have not yet been implemented.

---

# 9. Future Improvements

The following enhancements can further improve the system:

- Cross-Encoder Re-ranking
- Reciprocal Rank Fusion (RRF)
- Larger Embedding Model (BAAI/bge-base-en-v1.5)
- Graph RAG
- Metadata-aware Retrieval
- LLM-as-a-Judge Faithfulness Evaluation
- REST API using FastAPI

---

# 10. Final Evaluation Summary

| Metric | Result |
|---------|--------|
| Retrieval Method | Hybrid Search |
| Vector Database | ChromaDB |
| Keyword Search | Elasticsearch |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| LLM | Llama 3.2 (Ollama) |
| User Interface | Streamlit |
| Total Questions | 10 |
| Correct Retrievals | 10 |
| Retrieval Accuracy | **100%** |
| Semantic Faithfulness | **50%** |

---

# 11. Conclusion

The developed Hybrid RAG system successfully retrieves and answers questions from US Tax & Legal documents using a combination of semantic and keyword-based retrieval techniques.

The final system achieved **100% Retrieval Accuracy** on the Golden Set while generating answers with document-level citations for verification. The project demonstrates a practical implementation of a Hybrid Retrieval-Augmented Generation pipeline using **ChromaDB**, **Elasticsearch**, **Ollama**, and **Streamlit**.

Future improvements such as reranking models, Graph RAG, and LLM-based faithfulness evaluation can further improve answer quality and retrieval performance.