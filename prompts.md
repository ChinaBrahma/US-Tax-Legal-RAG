# Prompts Used During Development

This document contains representative prompts used during the development of the **US Tax & Legal Hybrid RAG System**. The prompts were used for planning, implementation, debugging, optimization, deployment, and documentation.

---

# Phase 1 - Project Planning

## Prompt 1

Design a production-ready Hybrid RAG system for answering questions from US Tax and Legal PDF documents. Suggest the overall architecture, folder structure, and technology stack.

---

## Prompt 2

Explain the complete workflow of a Hybrid Retrieval-Augmented Generation (RAG) system from document ingestion to answer generation.

---

## Prompt 3

Compare Vector Search, Keyword Search, and Hybrid Search. Which approach is better for legal documents and why?

---

## Prompt 4

Suggest a scalable folder structure for a Python-based Hybrid RAG project using LangChain, ChromaDB, Elasticsearch, and Streamlit.

---

## Prompt 5

List all technologies required for building a production-ready legal document assistant.

---

# Phase 2 - Dataset Collection

## Prompt 6

Suggest reliable public sources for downloading official US Tax and Legal PDF documents.

---

## Prompt 7

How should IRS Publications, IRS Forms, Acts, Court Judgements, and Internal Revenue Bulletins be organized for efficient retrieval?

---

## Prompt 8

What metadata should be extracted from legal documents to improve document retrieval?

---

## Prompt 9

Explain the advantages of separating datasets into categories before indexing.

---

## Prompt 10

Suggest the best directory structure for storing thousands of legal PDF files.

---

# Phase 3 - PDF Parsing

## Prompt 11

Write a Python script using PyMuPDF to extract text from PDF files while preserving page numbers.

---

## Prompt 12

How can document name, category, and page number be stored together with extracted text?

---

## Prompt 13

How should parsing errors be handled while processing multiple PDF documents?

---

## Prompt 14

Generate a JSON structure suitable for storing parsed legal documents.

---

## Prompt 15

Explain why metadata is important in Retrieval-Augmented Generation systems.

---

# Phase 4 - Document Chunking

## Prompt 16

Split long legal documents into overlapping chunks while preserving metadata.

---

## Prompt 17

What is the ideal chunk size and overlap for legal documents?

---

## Prompt 18

Explain the advantages and disadvantages of large and small chunk sizes.

---

## Prompt 19

Write a preprocessing pipeline for chunking parsed legal documents.

---

## Prompt 20

How can chunk IDs be generated uniquely for every document?

---

# Phase 5 - Embeddings & ChromaDB

## Prompt 21

Generate embeddings using the BAAI/bge-small-en-v1.5 embedding model.

---

## Prompt 22

Create a ChromaDB vector database from document chunks.

---

## Prompt 23

How should embeddings be stored efficiently for fast semantic search?

---

## Prompt 24

Explain how semantic similarity search works inside ChromaDB.

---

## Prompt 25

How can duplicate embeddings be avoided during indexing?

---

# Phase 6 - Elasticsearch Cloud

## Prompt 26

Create an Elasticsearch indexing pipeline using bulk indexing.

---

## Prompt 27

How should legal document metadata be mapped inside Elasticsearch?

---

## Prompt 28

Modify the project to use Elasticsearch Cloud instead of a locally hosted Elasticsearch server.

---

## Prompt 29

How can Cloud ID and API Key be loaded securely using environment variables?

---

## Prompt 30

Explain the difference between Elasticsearch Cloud and local Elasticsearch deployment.

---

# Phase 7 - Hybrid Retrieval

## Prompt 31

Combine semantic search results from ChromaDB with keyword search results from Elasticsearch Cloud.

---

## Prompt 32

Write a Hybrid Retrieval function that merges vector search and keyword search results.

---

## Prompt 33

How can duplicate documents be removed after combining retrieval results?

---

## Prompt 34

Implement query expansion for IRS Forms and Publications.

---

## Prompt 35

Explain how query expansion improves retrieval quality.

---

# Phase 8 - LLM Integration

## Prompt 36

Integrate Groq Llama 3.3 70B with LangChain.

---

## Prompt 37

Generate answers only from the retrieved document context.

---

## Prompt 38

How can hallucinations be reduced in Retrieval-Augmented Generation systems?

---

## Prompt 39

Write a prompt template that forces the model to answer only from retrieved documents.

---

## Prompt 40

How should document citations be displayed with generated answers?

---

# Phase 9 - Streamlit Application

## Prompt 41

Create a professional Streamlit interface for the legal assistant.

---

## Prompt 42

Display retrieved documents together with generated answers.

---

## Prompt 43

Add document citations and page numbers to the Streamlit interface.

---

## Prompt 44

Improve the Streamlit UI for better user experience.

---

## Prompt 45

Display loading indicators while searching and generating answers.

---

# Phase 10 - Debugging

## Prompt 46

Fix ModuleNotFoundError issues related to LangChain packages.

---

## Prompt 47

Resolve Elasticsearch Cloud connection issues.

---

## Prompt 48

Debug ChromaDB loading errors.

---

## Prompt 49

Fix Groq API integration issues.

---

## Prompt 50

Resolve dependency conflicts in requirements.txt.

---

# Phase 11 - Documentation & Deployment

## Prompt 51

Write a professional README for the project.

---

## Prompt 52

Prepare installation instructions for GitHub users.

---

## Prompt 53

Create deployment instructions for Streamlit Community Cloud.

---

## Prompt 54

Generate an architecture document explaining the Hybrid RAG pipeline.

---

## Prompt 55

Create a troubleshooting guide for common project issues.

---

## Prompt 56

Document the evaluation pipeline used in the project.

---

## Prompt 57

Prepare a Golden Set for retrieval evaluation.

---

## Prompt 58

Explain retrieval accuracy and semantic faithfulness metrics.

---

## Prompt 59

Review the project structure and suggest improvements.

---

## Prompt 60

Review the complete project before submission and suggest final improvements for deployment, documentation, and code quality.

---

# Note

The prompts listed above represent the major AI-assisted interactions used throughout the development of this project. AI assistance was primarily used for architecture planning, implementation guidance, debugging, documentation, and optimization, while the final integration, testing, validation, and deployment were completed manually.