from generator import generate_answer


def test_refusal_on_empty():
    r = generate_answer("q", [], 0.15)
    assert r["refused"] is True


def test_refusal_on_low_score():
    retrieved = [{"doc_id": "1", "chunk_id": "1_0", "text": "x", "title": "", "source": "", "score": 0.05}]
    assert generate_answer("q", retrieved, 0.15)["refused"] is True


def test_answer_high_score():
    retrieved = [{"doc_id": "1", "chunk_id": "1_0", "text": "Ипотека закрытие.", "title": "Ипотека", "source": "s", "score": 0.5}]
    r = generate_answer("ипотека", retrieved, 0.15)
    assert r["refused"] is False
    assert "Ипотека закрытие" in r["answer"]
