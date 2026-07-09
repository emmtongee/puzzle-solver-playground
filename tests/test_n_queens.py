from src.solvers.n_queens import is_safe


def test_same_column_is_unsafe():
    assert not is_safe([1], 1, 1)

def test_diagonal_down_right_is_unsafe():
    assert not is_safe([1], 1, 2)

def test_diagonal_down_left_is_unsafe():
    assert not is_safe([2], 1, 1)

def test_safe_position_returns_true():
    assert is_safe([1], 1, 3)

def test_safe_with_multiple_previous_queens():
    assert is_safe([1, 3], 2, 0)