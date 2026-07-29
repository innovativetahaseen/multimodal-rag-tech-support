from pathlib import Path
import os

from dotenv import load_dotenv

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env
load_dotenv(BASE_DIR / ".env")

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Model Configuration
MODEL_NAME = "llama-3.3-70b-versatile"

# Data Directories
MANUALS_DIR = BASE_DIR / "data" / "manuals"
IMAGES_DIR = BASE_DIR / "data" / "images"

# Vector Database
CHROMA_DB_DIR = BASE_DIR / "chroma_db"

# Text Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200