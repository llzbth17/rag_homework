from chunking import chunk_text, chunk_documents


def test_chunk_short_text():
    chunks = chunk_text("Короткий текст.", 400, 50)
    assert len(chunks) == 1


def test_chunk_overlap():
    words = [f"w{i}" for i in range(1000)]
    text = " ".join(words)
    chunks = chunk_text(text, 100, 20)
    assert len(chunks) > 1
    assert chunks[0].split()[-20:] == chunks[1].split()[:20]


def test_chunk_empty():
    assert chunk_text("", 100, 10) == []


def test_chunk_documents_ids():
    docs = [{"doc_id": "A", "title": "t", "text": " ".join(["w"] * 500), "source": "s"}]
    chunks = chunk_documents(docs, 100, 20)
    assert all(c["chunk_id"].startswith("A_") for c in chunks)
