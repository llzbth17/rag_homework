import pytest

from chunking import chunk_documents
from retrieval import build_tfidf, search


@pytest.fixture(scope="module")
def index():
    docs = [
        {"doc_id": "1", "title": "Ипотека", "text": "Закрытие ипотечной сделки финальный этап получения ипотеки.", "source": "s"},
        {"doc_id": "2", "title": "Кредит", "text": "Студенческий кредит используется для оплаты обучения.", "source": "s"},
        {"doc_id": "3", "title": "Банк", "text": "Wells Fargo предлагает услуги закрытия счёта клиентам.", "source": "s"},
    ]
    chunks = chunk_documents(docs, 200, 20)
    vectorizer, matrix = build_tfidf(chunks)
    return vectorizer, matrix, chunks


def test_search_top_k(index):
    v, m, c = index
    assert len(search("ипотека", v, m, c, top_k=3)) == 3


def test_search_relevance(index):
    v, m, c = index
    results = search("закрытие ипотечной сделки", v, m, c, top_k=3)
    assert results[0]["doc_id"] == "1"
    assert results[0]["score"] > 0.1


def test_search_empty(index):
    v, m, c = index
    assert search("", v, m, c, top_k=3) == []
