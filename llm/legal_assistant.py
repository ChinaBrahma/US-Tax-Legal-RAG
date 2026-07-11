import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from retriever.hybrid_retriever import hybrid_search
from langchain_ollama import ChatOllama

# -------------------------------
# Load Ollama Model
# -------------------------------
llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)

# -------------------------------
# User Question
# -------------------------------
question = input("\nEnter your legal question: ")

# -------------------------------
# Hybrid Search
# -------------------------------
retrieved_docs = hybrid_search(question)

# -------------------------------
# Build Context
# -------------------------------
context = ""
citations = []

for doc in retrieved_docs:

    document_name = doc["document"]
    page_number = doc["page"]
    category = doc["category"]
    source = doc["source"]

    citations.append(
        f"Document: {document_name} | Page: {page_number} | {source}"
    )

    context += f"""
===================================================
DOCUMENT NAME : {document_name}
PAGE NUMBER   : {page_number}
CATEGORY      : {category}
SOURCE        : {source}

CONTENT:
{doc["content"]}

===================================================

"""

# -------------------------------
# Prompt
# -------------------------------
prompt = f"""
You are an expert US Tax & Legal Assistant.

Answer ONLY using the supplied context.

Rules:

1. Never use outside knowledge.
2. Never hallucinate.
3. If the answer is not available in the context, reply exactly:
   Information not found in the provided documents.
4. Give a concise legal answer.
5. Give a short summary.
6. Do NOT invent citations.

Context:

{context}

Question:

{question}

Return the response in this format:

Answer:
<answer>

Summary:
<2-3 line summary>
"""

# -------------------------------
# Generate Answer
# -------------------------------
print("\nSearching using Hybrid Search...")
print("Generating Answer...\n")

response = llm.invoke(prompt)

# -------------------------------
# Print Answer
# -------------------------------
print("=" * 90)
print("LEGAL ANSWER")
print("=" * 90)
print(response.content)

# -------------------------------
# Print Citations
# -------------------------------
print("\n")
print("=" * 90)
print("SOURCE CITATIONS")
print("=" * 90)

unique = []

for citation in citations:
    if citation not in unique:
        unique.append(citation)

for citation in unique:
    print("•", citation)

print("=" * 90)