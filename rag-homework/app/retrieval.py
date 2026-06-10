"""TF-IDF индекс + cosine top-k поиск."""
import json

import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from config import TFIDF_VECTORIZER, TFIDF_MATRIX, CHUNKS_META


def build_tfidf(chunks):
    texts = [c["text"] for c in chunks]
    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        min_df=1,
        max_df=0.95,
    )
    matrix = vectorizer.fit_transform(texts)
    return vectorizer, matrix


def save_index(vectorizer, matrix, chunks):
    TFIDF_VECTORIZER.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(vectorizer, TFIDF_VECTORIZER)
    joblib.dump(matrix, TFIDF_MATRIX)
    with open(CHUNKS_META, "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")


def load_index():
    if not TFIDF_VECTORIZER.exists():
        raise FileNotFoundError(
            "Индекс не найден. Запусти: uv run python scripts/build_index.py"
        )
    vectorizer = joblib.load(TFIDF_VECTORIZER)
    matrix = joblib.load(TFIDF_MATRIX)
    chunks = []
    with open(CHUNKS_META, "r", encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))
    return vectorizer, matrix, chunks


def search(query, vectorizer, matrix, chunks, top_k=5):
    if not query or not query.strip():
        return []
    q_vec = vectorizer.transform([query])
    sims = cosine_similarity(q_vec, matrix)[0]
    top_idx = np.argsort(sims)[::-1][:top_k]
    results = []
    for idx in top_idx:
        chunk = chunks[idx].copy()
        chunk["score"] = float(sims[idx])
        results.append(chunk)
    return results
