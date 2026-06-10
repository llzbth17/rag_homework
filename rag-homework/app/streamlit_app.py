"""Streamlit UI."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st

from config import TOP_K, SCORE_THRESHOLD
from retrieval import load_index, search
from generator import generate_answer


st.set_page_config(page_title="RAG Homework", page_icon="🔎", layout="wide")


@st.cache_resource
def get_index():
    return load_index()


st.title("RAG Homework — TF-IDF")
st.caption("Учебный RAG на корпусе ag_news (1200 новостей)")

with st.sidebar:
    st.header("Параметры")
    top_k = st.slider("top_k", 1, 10, TOP_K)
    threshold = st.slider("Порог отказа (cosine)", 0.0, 1.0, SCORE_THRESHOLD, 0.01)
    st.markdown("---")
    st.header("Demo-запросы")
    st.markdown(
        "- technology news\n"
        "- sports games\n"
        "- stock market business\n"
        "- Как приготовить борщ? (отказ)"
    )

try:
    vectorizer, matrix, chunks = get_index()
    st.success(f"Индекс загружен: {len(chunks)} чанков")
except FileNotFoundError as e:
    st.error(str(e))
    st.stop()

query = st.text_input("Задай вопрос:")

if st.button("Спросить", type="primary") and query:
    with st.spinner("Ищу..."):
        retrieved = search(query, vectorizer, matrix, chunks, top_k=top_k)
        result = generate_answer(query, retrieved, score_threshold=threshold)

    st.subheader("Ответ")
    if result["refused"]:
        st.warning(result["answer"])
    else:
        st.write(result["answer"])

    st.subheader("Источники")
    if not result["sources"]:
        st.info("Релевантных источников не найдено.")
    else:
        for i, src in enumerate(result["sources"], 1):
            label = f"[{i}] doc_id={src['doc_id']} | chunk_id={src['chunk_id']} | score={src['score']:.3f}"
            with st.expander(label):
                if src.get("title"):
                    st.markdown(f"**{src['title']}**")
                st.write(src["text"])
                if src.get("source"):
                    st.caption(f"Источник: {src['source']}")
