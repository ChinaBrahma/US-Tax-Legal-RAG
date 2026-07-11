import json
from elasticsearch import Elasticsearch, helpers

# ----------------------------
# Connect to Elasticsearch
# ----------------------------
es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "legal_documents"

# ----------------------------
# Delete old index (if exists)
# ----------------------------
if es.indices.exists(index=INDEX_NAME):
    es.indices.delete(index=INDEX_NAME)
    print("🗑️ Old index deleted.")

# ----------------------------
# Create new index
# ----------------------------
mapping = {
    "mappings": {
        "properties": {
            "document": {
                "type": "keyword"
            },
            "category": {
                "type": "keyword"
            },
            "page": {
                "type": "integer"
            },
            "chunk_id": {
                "type": "keyword"
            },
            "content": {
                "type": "text"
            }
        }
    }
}

es.indices.create(index=INDEX_NAME, body=mapping)

print("✅ Index created.")

# ----------------------------
# Load chunks.json
# ----------------------------
with open("output/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"📄 Loaded {len(chunks)} chunks.")

# ----------------------------
# Prepare bulk indexing
# ----------------------------
actions = []

for chunk in chunks:

    action = {
        "_index": INDEX_NAME,
        "_source": {
            "document": chunk["document"],
            "category": chunk["category"],
            "page": chunk["page"],
            "chunk_id": chunk["chunk_id"],
            "content": chunk["text"]   # <-- IMPORTANT
        }
    }

    actions.append(action)

# ----------------------------
# Upload to Elasticsearch
# ----------------------------
print("⬆️ Uploading documents...")

helpers.bulk(es, actions)

print("🎉 All documents indexed successfully!")
print(f"Total Indexed Chunks: {len(actions)}")