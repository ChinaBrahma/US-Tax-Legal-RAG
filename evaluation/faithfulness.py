import csv
import sys
from pathlib import Path

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from retriever.hybrid_retriever import hybrid_search
from langchain_ollama import ChatOllama

# -------------------------
# Embedding Model
# -------------------------

embedder = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------
# LLM
# -------------------------

llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)

GOLDEN_SET = "evaluation/golden_set.csv"

total = 0
faithful = 0

print("=" * 80)
print("Running Semantic Faithfulness Evaluation")
print("=" * 80)

with open(GOLDEN_SET, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        total += 1

        query = row["query"]
        expected = row["ground_truth"]

        docs = hybrid_search(query)

        context = ""

        for doc in docs[:5]:
            context += doc["content"] + "\n\n"

        prompt = f"""
Answer ONLY from the provided context.

Context:
{context}

Question:
{query}
"""

        answer = llm.invoke(prompt).content.strip()

        expected_embedding = embedder.encode(
            expected,
            convert_to_tensor=True
        )

        answer_embedding = embedder.encode(
            answer,
            convert_to_tensor=True
        )

        similarity = cos_sim(
            expected_embedding,
            answer_embedding
        ).item()

        if similarity >= 0.80:
            status = "Faithful"
            faithful += 1
        elif similarity >= 0.60:
            status = "Needs Review"
        else:
            status = "Not Faithful"

        print("\n" + "-" * 80)
        print("Question   :", query)
        print("Similarity :", round(similarity, 3))
        print("Status     :", status)

score = faithful / total * 100

print("\n" + "=" * 80)
print("Semantic Faithfulness Score")
print("=" * 80)

print(f"Faithful Answers : {faithful}")
print(f"Total Questions  : {total}")
print(f"Faithfulness     : {score:.2f}%")