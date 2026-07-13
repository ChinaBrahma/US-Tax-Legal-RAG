from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

load_dotenv()
# ----------------------------------------------------
# Load Embedding Model
# ----------------------------------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

# ----------------------------------------------------
# Load ChromaDB
# ----------------------------------------------------

vector_db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding_model
)

# ----------------------------------------------------
# Connect Elasticsearch
# ----------------------------------------------------

es = Elasticsearch(
    cloud_id=os.getenv("ELASTIC_CLOUD_ID"),
    api_key=os.getenv("ELASTIC_API_KEY")
)

INDEX_NAME = "legal_documents"

# ----------------------------------------------------
# Query Expansion
# ----------------------------------------------------

QUERY_ALIASES = {

    "form w-4":
        "IRS Form W-4 Employee Withholding Certificate",

    "form w-9":
        "IRS Form W-9 Request for Taxpayer Identification Number",

    "form 4562":
        "IRS Form 4562 Depreciation and Amortization",

    "publication 463":
        "IRS Publication 463 Travel Gift and Car Expenses",

    "publication 527":
        "IRS Publication 527 Residential Rental Property",

    "publication 550":
        "IRS Publication 550 Investment Income and Expenses",

    "publication 946":
        "IRS Publication 946 Depreciation",

    "section 179":
        "IRS Section 179 Deduction Internal Revenue Code"
}


def expand_query(query):

    q = query.lower()

    for key, value in QUERY_ALIASES.items():

        if key in q:
            return value

    return query


# ----------------------------------------------------
# Hybrid Search
# ----------------------------------------------------

def hybrid_search(query, vector_k=5, keyword_k=5):

    expanded_query = expand_query(query)

    results = []

    # --------------------------------------------
    # Vector Search
    # --------------------------------------------

    vector_docs = vector_db.similarity_search(
        expanded_query,
        k=vector_k
    )

    for rank, doc in enumerate(vector_docs):

        results.append({

            "document": doc.metadata["document"],
            "page": doc.metadata["page"],
            "category": doc.metadata["category"],
            "content": doc.page_content,
            "source": "Vector Search",
            "score": 100 - rank

        })

    # --------------------------------------------
    # Elasticsearch Keyword Search
    # --------------------------------------------

    response = es.search(

        index=INDEX_NAME,

        body={

            "size": keyword_k,

            "query": {

                "multi_match": {

                    "query": expanded_query,

                    "fields": [

                        "document^5",
                        "category^2",
                        "content^3"

                    ],

                    "type": "best_fields"

                }

            }

        }

    )

    for hit in response["hits"]["hits"]:

        src = hit["_source"]

        results.append({

            "document": src["document"],
            "page": src["page"],
            "category": src["category"],
            "content": src["content"],
            "source": "Keyword Search",

            # Elasticsearch score ko zyada importance
            "score": hit["_score"] * 1000

        })

    # --------------------------------------------
    # Remove Duplicates
    # --------------------------------------------

    unique = {}

    for r in results:

        key = (r["document"], r["page"])

        if key not in unique:

            unique[key] = r

        else:

            if r["score"] > unique[key]["score"]:
                unique[key] = r

    # --------------------------------------------
    # Sort by Score
    # --------------------------------------------

    final_results = sorted(

        unique.values(),

        key=lambda x: x["score"],

        reverse=True

    )

    return final_results


# ----------------------------------------------------
# Testing
# ----------------------------------------------------

if __name__ == "__main__":

    question = input("\nEnter Question: ")

    docs = hybrid_search(question)

    print("\n")

    for i, doc in enumerate(docs, start=1):

        print("=" * 80)

        print(f"Result {i}")

        print(f"Source    : {doc['source']}")
        print(f"Document  : {doc['document']}")
        print(f"Page      : {doc['page']}")
        print(f"Category  : {doc['category']}")

        print("-" * 80)

        print(doc["content"][:700])