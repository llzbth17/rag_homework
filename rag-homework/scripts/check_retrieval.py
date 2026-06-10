import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))

from retrieval import load_index, search

QUERIES = [
    "technology news",
    "sports games",
    "stock market business",
    "world politics",
    "Как приготовить борщ?",
]


def main():
    vectorizer, matrix, chunks = load_index()
    for q in QUERIES:
        print(f"\n=== {q} ===")
        results = search(q, vectorizer, matrix, chunks, top_k=3)
        for r in results:
            print(f"  doc_id={r['doc_id']} score={r['score']:.3f} | {r['text'][:80]}...")


if __name__ == "__main__":
    main()
