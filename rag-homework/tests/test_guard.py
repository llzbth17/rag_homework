from guard import is_relevant


def test_guard_empty():
    assert is_relevant([], 0.15) is False


def test_guard_above():
    assert is_relevant([{"score": 0.4}], 0.15) is True


def test_guard_below():
    assert is_relevant([{"score": 0.05}], 0.15) is False
