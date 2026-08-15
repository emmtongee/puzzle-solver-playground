import pytest
from src.solvers.knapsack import (
    knapsack_problem_is_valid, 
    number_power_set, 
    solve_knapsack, 
    dynamic_solve_knapsack
)

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
    solution, subsets_checked = solve_knapsack(items, capacity)
    assert solution == (11, {0, 3})
    assert items == original_items
    assert subsets_checked > 0
    assert type(subsets_checked) is int

def test_dynamic_solve_normal_problem():
    items = [(2, 3), (3, 4), (4, 5), (5, 8)]
    original_items = items.copy()
    capacity = 7
    solution, states_calculated = dynamic_solve_knapsack(items, capacity)
    assert solution == (11, {0, 3})
    assert items == original_items
    assert states_calculated > 0
    assert type(states_calculated) is int

def test_solve_empty_items():
    items = []
    capacity = 2
    assert solve_knapsack(items, capacity) == ((0, set()), 1)

def test_dynamic_solve_empty_items():
    items = []
    capacity = 2
    assert dynamic_solve_knapsack(items, capacity) == ((0, set()), 0)

@pytest.mark.parametrize(
    "solver",
    [solve_knapsack, dynamic_solve_knapsack],
    ids=["brute-force", "dynamic-programming"],
)
def test_solve_no_fitting_items(solver):
    items = [(2, 3), (3, 4), (4, 5), (5, 8)]
    capacity = 1
    assert solver(items, capacity)[0] == (0, set())

@pytest.mark.parametrize(
    "solver",
    [solve_knapsack, dynamic_solve_knapsack],
    ids=["brute-force", "dynamic-programming"],
)
def test_solve_tiebreaking(solver):
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 7
    assert solver(items, capacity)[0] == (9, {1, 2})

@pytest.mark.parametrize(
    "solver",
    [solve_knapsack, dynamic_solve_knapsack],
    ids=["brute-force", "dynamic-programming"],
)
def test_solve_duplicate_items(solver):
    items = [(2, 3), (2, 3), (4, 5), (5, 6)]
    capacity = 4
    assert solver(items, capacity)[0] == (6, {0, 1})

@pytest.mark.parametrize(
    "solver",
    [solve_knapsack, dynamic_solve_knapsack],
    ids=["brute-force", "dynamic-programming"],
)
def test_solve_zero_weight(solver):
    items = [(0, 3), (3, 4), (4, 5), (5, 8)]
    capacity = 4
    assert solver(items, capacity)[0] == (8, {0, 2})

@pytest.mark.parametrize(
    "solver",
    [solve_knapsack, dynamic_solve_knapsack],
    ids=["brute-force", "dynamic-programming"],
)
def test_solve_zero_value(solver):
    items = [(2, 3), (3, 4), (4, 0), (5, 8)]
    capacity = 4
    assert solver(items, capacity)[0] == (4, {1})

@pytest.mark.parametrize(
    "solver",
    [solve_knapsack, dynamic_solve_knapsack],
    ids=["brute-force", "dynamic-programming"],
)
def test_solve_zero_capacity(solver):
    # without zero-weight items
    items = [(2, 3), (3, 4), (4, 5), (5, 8)]
    capacity = 0
    assert solver(items, capacity)[0] == (0, set())

    # with zero-weight zero-value items
    items = [(0, 0), (3, 4), (4, 5), (5, 8)]
    capacity = 0
    assert solver(items, capacity)[0] == (0, set())

    # with zero-weight nonzero-value items
    items = [(2, 3), (3, 4), (0, 5), (5, 8)]
    capacity = 0
    assert solver(items, capacity)[0] == (5, {2})

@pytest.mark.parametrize(
    "solver",
    [solve_knapsack, dynamic_solve_knapsack],
    ids=["brute-force", "dynamic-programming"],
)
def test_solve_negative_input(solver):
    # negative weight
    items = [(2, 3), (-3, 4), (4, 5), (5, 8)]
    capacity = 7
    with pytest.raises(ValueError):
        solver(items, capacity)

    # negative value
    items = [(2, 3), (3, 4), (4, -5), (5, 8)]
    capacity = 7
    with pytest.raises(ValueError):
        solver(items, capacity)

    # negative capacity
    items = [(2, 3), (3, 4), (4, 5), (5, 8)]
    capacity = -7
    with pytest.raises(ValueError):
        solver(items, capacity)

def test_both_solvers_produce_same_output_for_same_input():
    for items, capacity in (
        ([(2, 3), (3, 4), (4, 5), (5, 8)], 7),  # normal optimum
        ([(2, 3), (3, 4), (4, 5), (5, 6)], 7),  # tied optima
        ([(2, 3), (2, 3), (4, 5), (5, 6)], 4),  # duplicate items
        ([(0, 3), (3, 4), (4, 5), (5, 8)], 4)   # zero-weight item
    ):
        assert solve_knapsack(items, capacity)[0] == dynamic_solve_knapsack(items, capacity)[0]