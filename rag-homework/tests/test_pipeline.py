from chunking import chunk_documents
from retrieval import build_tfidf, search
from generator import generate_answer


def test_end_to_end():
    docs = [
        {"doc_id": "1", "title": "Ипотека", "text": "Закрытие ипотечной сделки финальный этап. Подписываются документы.", "source": "s"},
        {"doc_id": "2", "title": "Кредит", "text": "Студенческий кредит для оплаты обучения, возвращается после окончания.", "source": "s"},
        {"doc_id": "3", "title": "Банк", "text": "Wells Fargo закрытие счёта требует погасить долги.", "source": "s"},
    ]
    chunks = chunk_documents(docs, 200, 20)
    v, m = build_tfidf(chunks)

    results = search("закрытие ипотечной сделки", v, m, chunks, top_k=3)
    assert results[0]["doc_id"] == "1"

    answer = generate_answer("закрытие ипотечной сделки", results, 0.1)
    assert answer["refused"] is False

    negative = search("Как приготовить борщ?", v, m, chunks, top_k=3)
    refused = generate_answer("Как приготовить борщ?", negative, 0.15)
    assert refused["refused"] is True
