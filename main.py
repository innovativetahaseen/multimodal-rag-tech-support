from src.config import (
    MODEL_NAME,
    MANUALS_DIR,
    IMAGES_DIR,
    CHROMA_DB_DIR,
    GROQ_API_KEY,
)

print("Configuration Loaded Successfully")
print(f"Model: {MODEL_NAME}")
print(f"Manuals: {MANUALS_DIR}")
print(f"Images: {IMAGES_DIR}")
print(f"ChromaDB: {CHROMA_DB_DIR}")

if GROQ_API_KEY:
    print("Groq API Key Loaded")
else:
    print("Groq API Key Not Found")