from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Same embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

# Existing Vector DB load karo
vector_db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding_model
)

query = input("Enter your legal question: ")

results = vector_db.similarity_search(query, k=5)

print("\n" + "=" * 80)

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 80)
    print("Document :", doc.metadata["document"])
    print("Page     :", doc.metadata["page"])
    print("Category :", doc.metadata["category"])
    print()
    print(doc.page_content[:1000])