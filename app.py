import streamlit as st

from src.rag.rag_pipeline import RAGPipeline

st.set_page_config(
    page_title="Technical Support Assistant",
    page_icon="🛠️",
)

st.title("🛠️ Multi-modal RAG Technical Support")

st.write("Ask questions about the product manual.")

question = st.text_input("Enter your question")

if question:
    with st.spinner("Searching manual..."):
        rag = RAGPipeline()
        answer = rag.ask(question)

    st.subheader("Answer")
    st.write(answer)