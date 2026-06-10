"""Сборка индекса: ingest -> chunk -> TF-IDF -> save."""
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))

from config import (
    RAW_DATA, DOCUMENTS_FILE, CHUNKS_FILE,
    CHUNK_SIZE, CHUNK_OVERLAP,
)
from chunking import chunk_documents
from retrieval import build_tfidf, save_index


def load_raw():
    if not RAW_DATA.exists():
        raise FileNotFoundError(
            f"Нет {RAW_DATA}. Запусти: uv run python scripts/prepare_data.py"
        )
    with open(RAW_DATA, "r", encoding="utf-8") as f:
        return json.load(f)


def save_jsonl(items, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")


def main():
    print("1/4 Загружаю данные...")
    docs = load_raw()
    print(f"   Документов: {len(docs)}")
    save_jsonl(docs, DOCUMENTS_FILE)

    print("2/4 Нарезаю на чанки...")
    chunks = chunk_documents(docs, CHUNK_SIZE, CHUNK_OVERLAP)
    print(f"   Чанков: {len(chunks)}")
    save_jsonl(chunks, CHUNKS_FILE)

    print("3/4 Строю TF-IDF...")
    vectorizer, matrix = build_tfidf(chunks)
    print(f"   Словарь: {len(vectorizer.vocabulary_)} токенов")
    print(f"   Матрица: {matrix.shape}")

    print("4/4 Сохраняю индекс...")
    save_index(vectorizer, matrix, chunks)
    print("Готово! Индекс в data/index/")


if __name__ == "__main__":
    main()
