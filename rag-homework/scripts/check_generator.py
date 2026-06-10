import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))

from config import TOP_K, SCORE_THRESHOLD
from retrieval import load_index, search
from generator import generate_answer

QUERIES = [
    "technology news",
    "sports games",
    "stock market business",
    "Как приготовить борщ?",
]


def main():
    vectorizer, matrix, chunks = load_index()
    for q in QUERIES:
        print(f"\n=== {q} ===")
        retrieved = search(q, vectorizer, matrix, chunks, top_k=TOP_K)
        result = generate_answer(q, retrieved, SCORE_THRESHOLD)
        print(f"REFUSED: {result['refused']}")
        print(f"ANSWER:\n{result['answer'][:400]}")


if __name__ == "__main__":
    main()
