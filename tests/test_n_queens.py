from src.solvers.n_queens import is_safe, solve_n_queens


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

def test_num_of_solutions_for_n_queens():
    for n, num_of_solutions in ((0, 0), (1, 1), (2, 0), (3, 0), (4, 2), (5, 10)):
        assert len(solve_n_queens(n)) == num_of_solutions

def test_n_queens_solution_length():
    for solution in solve_n_queens(4):
        assert len(solution) == 4

def _solution_is_valid(solution):
    if len(solution) <= 1: 
        return True
    sol = solution.copy()
    col = sol.pop()
    if not _solution_is_valid(sol): 
        return False
    return is_safe(sol, len(sol), col)

def test_n_queens_solution_validity():
    for solution in solve_n_queens(4):
        assert _solution_is_valid(solution)