import json
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load parser output
with open("output/legal_documents.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

print(f"Total Pages Loaded: {len(documents)}")

# Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = []

for doc in documents:

    text = doc["text"]

    split_chunks = text_splitter.split_text(text)

    for i, chunk in enumerate(split_chunks):

        chunks.append({
            "document": doc["document"],
            "category": doc["category"],
            "page": doc["page"],
            "chunk_id": f"{doc['document']}_{doc['page']}_{i}",
            "text": chunk
        })

print(f"Total Chunks Created: {len(chunks)}")

os.makedirs("output", exist_ok=True)

with open("output/chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=4, ensure_ascii=False)

print("chunks.json saved successfully.")