"""Свой дополнительный тест (homework extra).

Проверяет, что guard правильно работает на границе порога
и что при threshold=0 даже самый низкий score пропускается.
"""
from guard import is_relevant


def test_my_boundary_exact_threshold():
    """Если score РОВНО равен порогу — должно считаться релевантным."""
    retrieved = [{"score": 0.15}]
    assert is_relevant(retrieved, 0.15) is True


def test_my_zero_threshold_passes_anything():
    """При пороге 0 любой положительный score проходит."""
    retrieved = [{"score": 0.001}]
    assert is_relevant(retrieved, 0.0) is True


def test_my_multiple_chunks_max_wins():
    """Из нескольких чанков релевантность определяется максимумом."""
    retrieved = [{"score": 0.05}, {"score": 0.5}, {"score": 0.01}]
    assert is_relevant(retrieved, 0.15) is True
