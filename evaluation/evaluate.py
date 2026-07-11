import csv
import sys
from pathlib import Path

# -------------------------------------------------
# Add Project Root
# -------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from retriever.hybrid_retriever import hybrid_search

# -------------------------------------------------
# Files
# -------------------------------------------------

GOLDEN_SET = "evaluation/golden_set.csv"
RESULTS_FILE = "evaluation/evaluation_results.csv"

total = 0
correct = 0

results = []

print("=" * 80)
print("Running Golden Set Evaluation...")
print("=" * 80)

# -------------------------------------------------
# Read Golden Set
# -------------------------------------------------

with open(GOLDEN_SET, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        total += 1

        query = row["query"]
        expected_doc = row["source_document"]

        # -----------------------------
        # Hybrid Search
        # -----------------------------

        docs = hybrid_search(query)

        # -----------------------------
        # Get Retrieved Documents
        # -----------------------------

        retrieved_documents = []

        for doc in docs:
            retrieved_documents.append(doc["document"])

        retrieved_doc_string = ", ".join(retrieved_documents)

        # -----------------------------
        # Top-K Evaluation
        # -----------------------------

        if expected_doc in retrieved_documents:
            status = "Correct"
            correct += 1
        else:
            status = "Incorrect"

        # -----------------------------
        # Save Result
        # -----------------------------

        results.append({

            "Query": query,
            "Expected": expected_doc,
            "Retrieved": retrieved_doc_string,
            "Status": status

        })

        # -----------------------------
        # Console Output
        # -----------------------------

        print("\n" + "-" * 80)

        print(f"Question : {total}")
        print(f"Query    : {query}")

        print(f"\nExpected Document:")
        print(f"   {expected_doc}")

        print(f"\nRetrieved Documents:")

        for doc in retrieved_documents:
            print(f"   - {doc}")

        print(f"\nStatus : {status}")

# -------------------------------------------------
# Save CSV
# -------------------------------------------------

with open(RESULTS_FILE, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(

        file,

        fieldnames=[

            "Query",
            "Expected",
            "Retrieved",
            "Status"

        ]

    )

    writer.writeheader()

    writer.writerows(results)

# -------------------------------------------------
# Accuracy
# -------------------------------------------------

accuracy = (correct / total * 100) if total else 0

print("\n" + "=" * 80)
print("Evaluation Completed")
print("=" * 80)

print(f"Total Questions      : {total}")
print(f"Correct Retrieval    : {correct}")
print(f"Retrieval Accuracy   : {accuracy:.2f}%")

print("\nResults saved to:")
print("evaluation/evaluation_results.csv")