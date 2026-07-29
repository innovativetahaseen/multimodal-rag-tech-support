import streamlit as st

from src.loaders.image_loader import ImageLoader
from src.rag.rag_pipeline import RAGPipeline
from src.rag.setup_vector_db import initialize_vector_database

initialize_vector_database()

st.set_page_config(
    page_title="Technical Support Assistant",
    page_icon="🛠️",
    layout="centered",
)
@st.cache_resource
def setup_database():
    initialize_vector_database()


setup_database()

# =====================================================
# Header
# =====================================================

st.title("🛠️ Multi-modal RAG Technical Support Assistant")

st.info(
    "📄 Upload a product image (optional) and ask a question about the product manual.\n\n"
    "The assistant combines image understanding with Retrieval-Augmented Generation (RAG) "
    "to provide grounded technical support responses."
)

# =====================================================
# Inputs
# =====================================================

uploaded_image = st.file_uploader(
    "📤 Upload Product Image",
    type=["png", "jpg", "jpeg"],
)

if uploaded_image:
    st.image(
        uploaded_image,
        width=500,
    )

question = st.text_input(
    "💬 Ask your question",
    placeholder="Example: How do I clear a paper jam?",
)

# =====================================================
# Generate Response
# =====================================================

if question:

    with st.spinner("🔍 Searching the manual and analyzing the image..."):

        image_caption = None

        if uploaded_image:
            image_loader = ImageLoader()
            image_caption = image_loader.generate_caption(uploaded_image)

        rag = RAGPipeline()

        result = rag.ask(
            question=question,
            image_caption=image_caption,
        )

    st.divider()

    with st.container(border=True):

        # -----------------------------
        # Image Analysis
        # -----------------------------
        if image_caption:
            st.subheader("🖼️ Image Analysis")
            st.write(image_caption)
        else:
            st.info(
                "No image uploaded. The response was generated using the product manual only."
            )

        st.divider()

        # -----------------------------
        # Technical Support Answer
        # -----------------------------
        st.subheader("💡 Technical Support Answer")
        st.write(result["answer"])

        st.divider()

        # -----------------------------
        # Source References
        # -----------------------------
        with st.expander("📚 View Source References", expanded=False):

            shown_sources = set()

            for source in result["sources"]:

                key = (source["source"], source["page"])

                if key not in shown_sources:
                    shown_sources.add(key)

                    st.write(
                        f"📄 **{source['source']}** — Page **{source['page']}**"
                    )

# =====================================================
# Footer
# =====================================================

st.markdown("---")

st.caption(
    "Built with **Groq**, **ChromaDB**, **Sentence Transformers**, **BLIP**, and **Streamlit**"
)