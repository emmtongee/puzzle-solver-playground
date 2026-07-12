import pytest

from src.solvers.n_queens import n_queens_is_safe, solve_n_queens
from src.utils.display import format_n_queens_board


def test_same_column_is_unsafe():
    assert not n_queens_is_safe([1], 1, 1)

def test_diagonal_down_right_is_unsafe():
    assert not n_queens_is_safe([1], 1, 2)

def test_diagonal_down_left_is_unsafe():
    assert not n_queens_is_safe([2], 1, 1)

def test_safe_position_returns_true():
    assert n_queens_is_safe([1], 1, 3)

def test_safe_with_multiple_previous_queens():
    assert n_queens_is_safe([1, 3], 2, 0)

def test_num_of_solutions_for_n_queens():
    for n, num_of_solutions in ((0, 0), (1, 1), (2, 0), (3, 0), (4, 2), (5, 10)):
        assert len(solve_n_queens(n)[0]) == num_of_solutions

def test_n_queens_solution_length():
    for solution in solve_n_queens(4)[0]:
        assert len(solution) == 4

def _solution_is_valid(solution):
    if len(solution) <= 1: 
        return True
    sol = solution.copy()
    col = sol.pop()
    if not _solution_is_valid(sol): 
        return False
    return n_queens_is_safe(sol, len(sol), col)

def test_n_queens_solution_validity():
    for solution in solve_n_queens(4)[0]:
        assert _solution_is_valid(solution)

def test_negative_n_raises_value_error():
    with pytest.raises(ValueError):
        solve_n_queens(-1)

def test_states_checked_is_int():
    for i in range(5):
        assert type(solve_n_queens(i)[1]) is int

def test_states_checked_is_positive():
    for i in (1,4):
        assert solve_n_queens(i)[1] > 0

def test_display_format():
    assert format_n_queens_board([1, 3, 0, 2]) == (
        ". Q . .\n"
        ". . . Q\n"
        "Q . . .\n"
        ". . Q ."
    )