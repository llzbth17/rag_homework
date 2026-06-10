"""Нарезка текстов на чанки."""
import re


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def chunk_text(text: str, chunk_size: int = 400, overlap: int = 50) -> list[str]:
    if not text or not text.strip():
        return []
    if chunk_size <= 0:
        raise ValueError("chunk_size должен быть > 0")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap должен быть в [0, chunk_size)")

    words = normalize(text).split()
    if len(words) <= chunk_size:
        return [" ".join(words)]

    chunks = []
    step = chunk_size - overlap
    for i in range(0, len(words), step):
        piece = words[i : i + chunk_size]
        if not piece:
            break
        chunks.append(" ".join(piece))
        if i + chunk_size >= len(words):
            break
    return chunks


def chunk_documents(docs: list[dict], chunk_size: int = 400, overlap: int = 50) -> list[dict]:
    result = []
    for doc in docs:
        pieces = chunk_text(doc.get("text", ""), chunk_size, overlap)
        for i, piece in enumerate(pieces):
            result.append({
                "doc_id": str(doc["doc_id"]),
                "chunk_id": f"{doc['doc_id']}_{i}",
                "text": piece,
                "title": doc.get("title", ""),
                "source": doc.get("source", ""),
            })
    return result
