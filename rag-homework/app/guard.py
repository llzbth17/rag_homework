"""Правила релевантности и отказы."""

REFUSAL_MESSAGE = "В источниках нет информации для ответа на этот вопрос."


def is_relevant(retrieved: list[dict], score_threshold: float = 0.15) -> bool:
    if not retrieved:
        return False
    return max(r["score"] for r in retrieved) >= score_threshold
