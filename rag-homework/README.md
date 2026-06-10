# RAG Homework

Учебный RAG на TF-IDF + cosine similarity. Корпус: ag_news (HuggingFace, 1200 новостей).
Структура повторяет MaratNotes/rag-tutorial.

## Требования
- Python 3.10+
- uv

## Быстрый старт

```
uv venv --python 3.12
uv sync
uv run python scripts/prepare_data.py
uv run python scripts/build_index.py
uv run streamlit run app/streamlit_app.py
```

Открой localhost:8501

## Проверка

```
uv run pytest tests/ -v
uv run python scripts/check_retrieval.py
uv run python scripts/check_generator.py
```

## Данные
- Источник: ag_news (HuggingFace Datasets)
- Записей: 1200
- Чанков: 1200 (зависит от длины текстов)
- Поле для индексации: text
- Подробнее: doc/dataset.md

## Demo-вопросы

| Вопрос | Результат |
|--------|-----------|
| technology news | ответ найден |
| sports games | ответ найден |
| stock market business | ответ найден |
| Как приготовить борщ? | отказ |

Скриншоты: doc/screenshots/

## Ограничения MVP
- TF-IDF (поиск по словам, не по смыслу)
- Без LLM (ответ extractive)
- Индексируется только text

## Улучшения
См. 02_improvements.md
