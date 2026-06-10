# Реализация

## Этапы
1. prepare_data.py — создаёт data/raw/datasets.json
2. build_index.py — режет на чанки, строит TF-IDF, сохраняет
3. check_retrieval.py — проверка поиска
4. check_generator.py — проверка ответа
5. streamlit_app.py — UI

## Команды
```
uv sync
uv run python scripts/prepare_data.py
uv run python scripts/build_index.py
uv run pytest tests/ -v
uv run streamlit run app/streamlit_app.py
```
