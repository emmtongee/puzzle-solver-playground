import pytest

from src.solvers.sudoku import read_sudoku_file, parse_sudoku, solve_sudoku, sudoku_get_cell_candidates, sudoku_select_mrv_cell


def test_solve_contradictory_board():
    board = [
        [4, 8, 0, 0, 5, 0, 0, 2, 3], # 5th col 5 contradicts with 5 below
        [0, 5, 0, 0, 0, 0, 0, 6, 7],
        [0, 6, 0, 9, 0, 7, 4, 0, 1], 
        [1, 0, 9, 0, 0, 0, 3, 4, 0],
        [7, 3, 0, 0, 0, 0, 1, 8, 9], 
        [0, 0, 0, 1, 9, 0, 0, 0, 6],
        [2, 0, 0, 4, 5, 9, 0, 0, 0], # 5th col 5
        [0, 9, 8, 2, 0, 0, 7, 3, 4],
        [0, 1, 4, 7, 3, 8, 0, 0, 0]
    ]
    with pytest.raises(ValueError):
        solve_sudoku(board)

def test_solve_one_empty_cell():
    board = [
        [4, 8, 7, 6, 1, 5, 9, 2, 3], 
        [9, 5, 1, 3, 2, 4, 8, 6, 7], 
        [3, 6, 2, 9, 8, 7, 4, 5, 1], 
        [1, 2, 9, 8, 7, 6, 3, 4, 5], 
        [7, 3, 6, 5, 0, 2, 1, 8, 9], # solve 5th col 0
        [8, 4, 5, 1, 9, 3, 2, 7, 6], 
        [2, 7, 3, 4, 5, 9, 6, 1, 8], 
        [5, 9, 8, 2, 6, 1, 7, 3, 4], 
        [6, 1, 4, 7, 3, 8, 5, 9, 2]
    ]
    solved_board, candidates_checked = solve_sudoku(board)

    assert solved_board[4][4] == 4
    assert candidates_checked > 0

def test_solve_unsolvable_board():
    board = [
        [4, 8, 1, 0, 0, 0, 0, 2, 3], 
        [0, 5, 0, 0, 0, 0, 0, 6, 7],
        [0, 6, 0, 9, 0, 7, 4, 0, 1], 
        [1, 0, 9, 0, 0, 0, 3, 4, 0],
        [7, 3, 0, 0, 0, 0, 1, 8, 9], 
        [0, 0, 0, 1, 9, 0, 0, 0, 6],
        [2, 0, 0, 4, 5, 9, 0, 0, 0], 
        [0, 9, 8, 2, 0, 0, 7, 3, 4],
        [0, 1, 4, 7, 3, 8, 0, 0, 0]
    ]
    solved_board, candidates_checked = solve_sudoku(board)
    assert solved_board is None
    assert candidates_checked > 0

def test_solve_already_complete_board():
    board = [
        [4, 8, 7, 6, 1, 5, 9, 2, 3], 
        [9, 5, 1, 3, 2, 4, 8, 6, 7], 
        [3, 6, 2, 9, 8, 7, 4, 5, 1], 
        [1, 2, 9, 8, 7, 6, 3, 4, 5], 
        [7, 3, 6, 5, 4, 2, 1, 8, 9], 
        [8, 4, 5, 1, 9, 3, 2, 7, 6], 
        [2, 7, 3, 4, 5, 9, 6, 1, 8], 
        [5, 9, 8, 2, 6, 1, 7, 3, 4], 
        [6, 1, 4, 7, 3, 8, 5, 9, 2]
    ]
    solved_board, candidates_checked = solve_sudoku(board)
    assert solved_board == board
    assert candidates_checked == 0

def test_solve_easy_board():
    board = parse_sudoku(read_sudoku_file("examples/sudoku_easy.txt"))
    original_board = [row.copy() for row in board]
    solved_board, candidates_checked = solve_sudoku(board)

    assert board == original_board

    expected_solution_board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2], 
        [6, 7, 2, 1, 9, 5, 3, 4, 8], 
        [1, 9, 8, 3, 4, 2, 5, 6, 7], 
        [8, 5, 9, 7, 6, 1, 4, 2, 3], 
        [4, 2, 6, 8, 5, 3, 7, 9, 1], 
        [7, 1, 3, 9, 2, 4, 8, 5, 6], 
        [9, 6, 1, 5, 3, 7, 2, 8, 4], 
        [2, 8, 7, 4, 1, 9, 6, 3, 5], 
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    assert solved_board == expected_solution_board
    assert candidates_checked > 0
    assert type(candidates_checked) is int

def test_get_cell_candidates_returns_ascending_legal_values():
    board = [
        [4, 8, 1, 0, 0, 0, 0, 2, 3], 
        [0, 5, 0, 0, 0, 0, 0, 6, 7],
        [0, 6, 0, 9, 0, 7, 4, 0, 1], 
        [1, 0, 9, 0, 0, 0, 3, 4, 0],
        [7, 3, 0, 0, 0, 0, 1, 8, 9], 
        [0, 0, 0, 1, 9, 0, 0, 0, 6],
        [2, 0, 0, 4, 5, 9, 0, 0, 0], 
        [0, 9, 8, 2, 0, 0, 7, 3, 4],
        [0, 1, 4, 7, 3, 8, 0, 0, 0]
    ]
    original_board = [board[i].copy() for i in range(9)]
    candidates = sudoku_get_cell_candidates(board, 2, 4)
    assert candidates == [2, 8]
    assert board == original_board

def test_select_mrv_cell_returns_unique_minimum():
    board = [
        [8, 0, 0, 0, 7, 4, 3, 0, 5],
        [0, 0, 7, 2, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 8, 0, 0], 
        [0, 0, 5, 8, 9, 0, 0, 0, 0],
        [4, 0, 9, 3, 0, 7, 5, 0, 8],
        [0, 0, 0, 0, 4, 5, 9, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 3, 2, 0],
        [3, 0, 2, 7, 5, 0, 0, 0, 4]
    ]
    original_board = [board[i].copy() for i in range(9)]
    cell, candidates = sudoku_select_mrv_cell(board)
    assert cell == (0, 2)
    assert candidates == [1]
    assert board == original_board

def test_select_mrv_cell_breaks_ties_by_row_major_order():
    board = [
        [8, 0, 0, 0, 7, 4, 0, 0, 5],
        [0, 0, 7, 2, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 8, 0, 0], 
        [0, 0, 5, 8, 9, 0, 0, 0, 0],
        [4, 0, 0, 3, 0, 7, 5, 0, 8],
        [0, 0, 0, 0, 4, 5, 9, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 3, 2, 0],
        [3, 0, 2, 7, 5, 0, 0, 0, 4]
    ]
    # (4, 2) and later cells share the minimum candidate count (2);
    # row-major tie-breaking must select (4, 2).
    cell, candidates = sudoku_select_mrv_cell(board)
    assert cell == (4, 2)
    assert candidates == [1, 9]

def test_select_mrv_cell_returns_none_for_complete_board():
    board = [
        [4, 8, 7, 6, 1, 5, 9, 2, 3], 
        [9, 5, 1, 3, 2, 4, 8, 6, 7], 
        [3, 6, 2, 9, 8, 7, 4, 5, 1], 
        [1, 2, 9, 8, 7, 6, 3, 4, 5], 
        [7, 3, 6, 5, 4, 2, 1, 8, 9], 
        [8, 4, 5, 1, 9, 3, 2, 7, 6], 
        [2, 7, 3, 4, 5, 9, 6, 1, 8], 
        [5, 9, 8, 2, 6, 1, 7, 3, 4], 
        [6, 1, 4, 7, 3, 8, 5, 9, 2]
    ]
    assert sudoku_select_mrv_cell(board) is None

def test_select_mrv_cell_returns_empty_candidates_for_dead_end():
    board = [
        [8, 0, 0, 0, 7, 4, 3, 0, 5],
        [0, 0, 7, 2, 6, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 8, 0, 0], 
        [0, 0, 5, 8, 9, 2, 0, 0, 0],
        [4, 1, 9, 3, 0, 7, 5, 0, 8],
        [0, 0, 0, 0, 4, 5, 9, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 3, 2, 0],
        [3, 0, 2, 7, 5, 0, 0, 0, 4]
    ]
    assert sudoku_select_mrv_cell(board) == ((4, 4), [])