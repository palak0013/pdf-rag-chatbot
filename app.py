import os
import shutil
import streamlit as st
from dotenv import load_dotenv

from utils.loader import load_pdfs_from_folder
from utils.splitter import split_text
from utils.vectorstore import create_vectorstore
from utils.rag import rag_pipeline

from models import client

load_dotenv()

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI-Powered PDF Chatbot")
st.caption("Upload PDFs and ask questions based only on their contents.")

# ---------------- SESSION STATE ---------------- #

if "retriever" not in st.session_state:
    st.session_state.retriever = None

# ---------------- SIDEBAR ---------------- #

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF(s)",
    type="pdf",
    accept_multiple_files=True
)

show_sources = st.sidebar.checkbox(
    "Show Sources",
    value=True
)

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.retriever = None
    st.rerun()

# ---------------- PROCESS PDFs ---------------- #

if st.sidebar.button("📥 Process PDFs"):

    if not uploaded_files:
        st.sidebar.warning("Please upload at least one PDF.")
        st.stop()

    with st.spinner("Processing PDFs..."):
        os.makedirs("temp_pdfs", exist_ok=True)
        for filename in os.listdir("temp_pdfs"):
           file_path = os.path.join("temp_pdfs", filename)

           if os.path.isfile(file_path):
                os.remove(file_path)

        for file in uploaded_files:

            with open(
                os.path.join("temp_pdfs", file.name),
                "wb"
            ) as f:

                f.write(file.getbuffer())

        docs = load_pdfs_from_folder("temp_pdfs")

        chunks = split_text(docs)

        vectorstore = create_vectorstore(chunks)

        st.session_state.retriever = vectorstore.as_retriever(
            search_kwargs={"k":4}
        )

    st.sidebar.success("PDFs processed successfully ✅")
    
query = st.text_input(
    "💬 Ask a question about your PDFs"
)

if query:

    if st.session_state.retriever is None:

        st.warning("Please process PDFs first.")

    else:

        with st.spinner("Generating answer..."):

            answer, docs = rag_pipeline(
                query=query,
                retriever=st.session_state.retriever,
                client=client
            )

        st.markdown(answer)

        if show_sources:

            with st.expander("📚 Retrieved Sources"):

                for i, doc in enumerate(docs, start=1):

                    st.markdown(f"### Chunk {i}")

                    st.write(doc.page_content[:700])

                    st.divider()