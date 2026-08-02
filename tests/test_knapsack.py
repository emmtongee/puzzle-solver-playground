import pytest
from src.solvers.knapsack import knapsack_problem_is_valid, number_power_set, solve_knapsack

def test_knapsack_problem_is_valid():
    # valid
    items = [(2, 3), (3, 4), (4, 5), (5, 8)]
    capacity = 7
    assert knapsack_problem_is_valid(items, capacity)

    # negative weight
    items = [(2, 3), (-3, 4), (4, 5), (5, 8)]
    capacity = 7
    assert not knapsack_problem_is_valid(items, capacity)

    # negative value
    items = [(2, 3), (3, 4), (4, 5), (5, -8)]
    capacity = 7
    assert not knapsack_problem_is_valid(items, capacity)

    # negative capacity
    items = [(2, 3), (3, 4), (4, 5), (5, 8)]
    capacity = -4
    assert not knapsack_problem_is_valid(items, capacity)
    
def test_number_power_set_with_zero_items():
    assert number_power_set(0) == [set()]

def test_number_power_set_returns_subsets_in_binary_order():
    assert number_power_set(3) == [set(), {0}, {1}, {0, 1}, {2}, {0, 2}, {1, 2}, {0, 1, 2}]

def test_solve_normal_problem():
    items = [(2, 3), (3, 4), (4, 5), (5, 8)]
    original_items = items.copy()
    capacity = 7
    assert solve_knapsack(items, capacity) == (11, {0, 3})
    assert items == original_items

def test_solve_empty_items():
    items = []
    capacity = 2
    assert solve_knapsack(items, capacity) == (0, set())

def test_solve_no_fitting_items():
    items = [(2, 3), (3, 4), (4, 5), (5, 8)]
    capacity = 1
    assert solve_knapsack(items, capacity) == (0, set())

def test_solve_tiebreaking():
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 7
    assert solve_knapsack(items, capacity) == (9, {1, 2})

def test_solve_duplicate_items():
    items = [(2, 3), (2, 3), (4, 5), (5, 6)]
    capacity = 4
    assert solve_knapsack(items, capacity) == (6, {0, 1})

def test_solve_zero_weight():
    items = [(0, 3), (3, 4), (4, 5), (5, 8)]
    capacity = 4
    assert solve_knapsack(items, capacity) == (8, {0, 2})

def test_solve_zero_value():
    items = [(2, 3), (3, 4), (4, 0), (5, 8)]
    capacity = 4
    assert solve_knapsack(items, capacity) == (4, {1})

def test_solve_zero_capacity():
    # without zero-weight items
    items = [(2, 3), (3, 4), (4, 5), (5, 8)]
    capacity = 0
    assert solve_knapsack(items, capacity) == (0, set())

    # with zero-weight zero-value items
    items = [(0, 0), (3, 4), (4, 5), (5, 8)]
    capacity = 0
    assert solve_knapsack(items, capacity) == (0, set())

    # with zero-weight nonzero-value items
    items = [(2, 3), (3, 4), (0, 5), (5, 8)]
    capacity = 0
    assert solve_knapsack(items, capacity) == (5, {2})

def test_solve_negative_input():
    # negative weight
    items = [(2, 3), (-3, 4), (4, 5), (5, 8)]
    capacity = 7
    with pytest.raises(ValueError):
        solve_knapsack(items, capacity)

    # negative value
    items = [(2, 3), (3, 4), (4, -5), (5, 8)]
    capacity = 7
    with pytest.raises(ValueError):
        solve_knapsack(items, capacity)

    # negative capacity
    items = [(2, 3), (3, 4), (4, 5), (5, 8)]
    capacity = -7
    with pytest.raises(ValueError):
        solve_knapsack(items, capacity)