"""Конфигурация: пути, параметры чанкинга и поиска."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = ROOT / "data" / "raw" / "datasets.json"
PROCESSED_DIR = ROOT / "data" / "processed"
DOCUMENTS_FILE = PROCESSED_DIR / "documents.jsonl"
CHUNKS_FILE = PROCESSED_DIR / "chunks.jsonl"

INDEX_DIR = ROOT / "data" / "index"
TFIDF_VECTORIZER = INDEX_DIR / "vectorizer.joblib"
TFIDF_MATRIX = INDEX_DIR / "matrix.joblib"
CHUNKS_META = INDEX_DIR / "chunks.jsonl"

CHUNK_SIZE = 400
CHUNK_OVERLAP = 50

TOP_K = 5
SCORE_THRESHOLD = 0.15
