import streamlit as st
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from retriever.hybrid_retriever import hybrid_search

load_dotenv()

# ----------------------------
# Streamlit Config
# ----------------------------
st.set_page_config(
    page_title="US Tax & Legal Assistant",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ US Tax & Legal RAG Assistant")
st.write("Ask questions about US Tax & Legal documents using Hybrid Search.")

# ----------------------------
# Load LLM
# ----------------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# ----------------------------
# User Input
# ----------------------------
question = st.text_input("Enter your legal question")

# ----------------------------
# Search Button
# ----------------------------
if st.button("Search"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Searching documents..."):

        docs = hybrid_search(question)

        if len(docs) == 0:
            st.subheader("📌 Answer")
            st.write("Information not found in the provided documents.")
            st.stop()

    context = ""
    citations = []

    for doc in docs:

        context += f"""
Document: {doc['document']}
Page: {doc['page']}
Category: {doc['category']}

{doc['content']}

--------------------------------------------
"""

        citations.append(
            (
                doc["document"],
                doc["page"],
                doc["source"]
            )
        )

    prompt = f"""
You are an expert US Tax & Legal Assistant.

Answer ONLY using the provided context.

Rules:
1. Never hallucinate.
2. If answer is unavailable, reply:
   Information not found in the provided documents.
3. Keep the answer concise.
4. Give a short summary.

Context:

{context}

Question:

{question}
"""

    with st.spinner("Generating Answer..."):

        response = llm.invoke(prompt)

    # ----------------------------
    # Display Answer
    # ----------------------------

    st.subheader("📌 Answer")
    st.write(response.content)

    # ----------------------------
    # Source Citations
    # ----------------------------

    st.subheader("📚 Source Citations")

    unique = []

    for item in citations:
        if item not in unique:
            unique.append(item)

    for doc, page, source in unique:
        st.write(
            f"**📄 {doc}** | Page **{page}** | *{source}*"
        )

    # ----------------------------
    # Retrieved Documents
    # ----------------------------

    st.subheader("📑 Retrieved Context")

    for i, doc in enumerate(docs, start=1):

        with st.expander(
            f"{i}. {doc['document']} (Page {doc['page']}) - {doc['source']}"
        ):
            st.write(doc["content"])