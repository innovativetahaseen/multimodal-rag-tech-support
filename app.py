import streamlit as st

from src.rag.rag_pipeline import RAGPipeline
from src.loaders.image_loader import ImageLoader

st.set_page_config(
    page_title="Technical Support Assistant",
    page_icon="🛠️",
)

st.title("🛠️ Multi-modal RAG Technical Support")

st.write("Ask questions about the product manual.")

uploaded_image = st.file_uploader(
    "Upload a product image (optional)",
    type=["png", "jpg", "jpeg"],
)

if uploaded_image:
    st.image(
    uploaded_image,
    width="stretch",
)

    image_loader = ImageLoader()

    caption = image_loader.generate_caption(uploaded_image)

    st.subheader("Image Caption")

    st.write(caption)

question = st.text_input("Enter your question")

if question:
    with st.spinner("Searching manual..."):

        image_caption = None

        if uploaded_image:
            image_loader = ImageLoader()

            image_caption = image_loader.generate_caption(uploaded_image)

            st.subheader("Image Caption")
            st.write(image_caption)

        rag = RAGPipeline()

        answer = rag.ask(
            question=question,
            image_caption=image_caption,
        )

    st.subheader("Answer")
    st.write(answer)