import json

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# --------------------------------------------------
# Load Chunks
# --------------------------------------------------

with open("output/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Total Chunks Loaded: {len(chunks)}")

# --------------------------------------------------
# Convert Chunks to LangChain Documents
# --------------------------------------------------

documents = []

for chunk in chunks:

    documents.append(

        Document(

            page_content=chunk["text"],

            metadata={

                "document": chunk["document"],
                "page": chunk["page"],
                "category": chunk["category"],
                "chunk_id": chunk["chunk_id"]

            }

        )

    )

print(f"Total Documents Prepared: {len(documents)}")

# --------------------------------------------------
# Load Embedding Model
# --------------------------------------------------

print("Loading embedding model...")

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

# --------------------------------------------------
# Create Chroma Vector Database
# --------------------------------------------------

print("Creating ChromaDB...")

vector_db = Chroma.from_documents(

    documents=documents,

    embedding=embedding_model,

    persist_directory="vector_db"

)

print("✅ ChromaDB created successfully!")
print(f"Total Indexed Chunks: {len(documents)}")