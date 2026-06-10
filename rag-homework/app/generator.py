"""Demo-генератор: собирает ответ из найденных чанков, без LLM."""
from guard import is_relevant, REFUSAL_MESSAGE


def generate_answer(query, retrieved, score_threshold=0.15):
    if not is_relevant(retrieved, score_threshold):
        return {"answer": REFUSAL_MESSAGE, "sources": [], "refused": True}

    relevant = [r for r in retrieved if r["score"] >= score_threshold]
    parts = []
    for i, r in enumerate(relevant[:3], 1):
        snippet = r["text"][:500]
        title = r.get("title", "")
        head = f"[{i}] {title}" if title else f"[{i}]"
        parts.append(f"{head}\n{snippet}")
    answer = "\n\n".join(parts)
    return {"answer": answer, "sources": retrieved, "refused": False}