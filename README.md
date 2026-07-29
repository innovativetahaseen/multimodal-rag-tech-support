# 🛠️ Multi-modal RAG Technical Support Assistant

An AI-powered **Multi-modal Retrieval-Augmented Generation (RAG)** application that assists users in troubleshooting technical issues using **product manuals** and **product images**.

The application combines **semantic document retrieval**, **image understanding**, and **Large Language Models (LLMs)** to generate grounded, context-aware technical support responses.

---

## 🚀 Features

- 📄 Extracts knowledge from PDF product manuals
- ✂️ Splits manuals into semantic text chunks
- 🧠 Generates embeddings using Sentence Transformers
- 🗄️ Stores embeddings in ChromaDB
- 🔍 Performs semantic similarity search
- 🖼️ Analyzes uploaded product images using BLIP Image Captioning
- 🤖 Generates grounded responses using Groq LLM
- 📚 Displays source references with manual page numbers
- 🌐 Interactive Streamlit web interface

---

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
              Streamlit Interface
                      │
         ┌────────────┴────────────┐
         │                         │
         ▼                         ▼
  Product Image             User Question
         │                         │
         ▼                         ▼
 BLIP Image Captioning      Semantic Retrieval
                                   │
                                   ▼
                              ChromaDB
                                   │
                                   ▼
                        Relevant Manual Chunks
                                   │
                                   ▼
                         Groq Large Language Model
                                   │
                                   ▼
                        Grounded Technical Response
                                   │
                                   ▼
                          Source References
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Frontend | Streamlit |
| LLM | Groq |
| Embedding Model | Sentence Transformers |
| Vector Database | ChromaDB |
| Image Captioning | BLIP |
| PDF Processing | PyPDFLoader (LangChain Community) |
| Retrieval | Semantic Search |
| Environment | Python Virtual Environment |

---

## 📂 Project Structure

```text
multimodal-rag-tech-support/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── data/
│   ├── manuals/
│   └── images/
│
├── chroma_db/
│
└── src/
    ├── config.py
    ├── llm/
    │   └── groq_client.py
    ├── loaders/
    │   ├── pdf_loader.py
    │   └── image_loader.py
    ├── rag/
    │   ├── embeddings.py
    │   ├── retriever.py
    │   ├── text_splitter.py
    │   ├── vector_store.py
    │   └── rag_pipeline.py
    └── utils/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/innovativetahaseen/multimodal-rag-tech-support.git
```

### 2. Navigate to the project

```bash
cd multimodal-rag-tech-support
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

### 7. Run the application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Load the product manual.
2. Split the manual into semantic chunks.
3. Generate vector embeddings.
4. Store embeddings in ChromaDB.
5. Upload an optional product image.
6. Generate an image caption using BLIP.
7. Retrieve relevant manual sections using semantic search.
8. Combine retrieved context and image caption.
9. Generate a grounded response using Groq.
10. Display source references.

---

## 💡 Example Workflow

**Question**

> How do I clear a paper jam?

**Response**

- Retrieves relevant manual pages.
- Uses image context (if provided).
- Generates step-by-step troubleshooting instructions.
- Displays source page references.

---

## 📸 Screenshots

> Add screenshots here after uploading them to GitHub.

### Home Page

```
images/home.png
```

### Image Upload

```
images/upload.png
```

### Generated Answer

```
images/answer.png
```

### Source References

```
images/sources.png
```

---

## 🎯 Future Improvements

- Multi-document support
- Conversational memory
- OCR for scanned manuals
- Image similarity retrieval
- Citation highlighting
- Response streaming
- User authentication
- Cloud deployment

---

## 👨‍💻 Author

**Tahaseen Khan**

AI & Machine Learning Engineer

GitHub: https://github.com/innovativetahaseen

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, consider giving it a star!