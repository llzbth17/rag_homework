# 03. Архитектура

Pipeline:
raw json -> ingest -> chunking -> TF-IDF -> joblib
query -> transform -> cosine_similarity -> top_k -> guard -> ответ

## Модули
- app/config.py
- app/chunking.py
- app/retrieval.py
- app/generator.py
- app/guard.py
- app/streamlit_app.py

## Параметры
- chunk_size = 400 слов
- overlap = 50
- top_k = 5
- score_threshold = 0.15
