import pytest

from src.solvers.sudoku import read_sudoku_file, parse_sudoku, sudoku_is_safe, solve_sudoku, sudoku_board_is_valid

def test_read_sudoku_file():
    assert read_sudoku_file("examples/sudoku_easy.txt") == (
        "5 3 0 0 7 0 0 0 0\n"
        "6 0 0 1 9 5 0 0 0\n"
        "0 9 8 0 0 0 0 6 0\n"
        "8 0 0 0 6 0 0 0 3\n"
        "4 0 0 8 0 3 0 0 1\n"
        "7 0 0 0 2 0 0 0 6\n"
        "0 6 0 0 0 0 2 8 0\n"
        "0 0 0 4 1 9 0 0 5\n"
        "0 0 0 0 8 0 0 7 9"
    )

def test_parser_valid_input():
    test_board = (
        "5 3 0 0 7 0 0 0 0\n"
        "6 0 0 1 9 5 0 0 0\n"
        "0 9 8 0 0 0 0 6 0\n"
        "8 0 0 0 6 0 0 0 3\n"
        "4 0 0 8 0 3 0 0 1\n"
        "7 0 0 0 2 0 0 0 6\n"
        "0 6 0 0 0 0 2 8 0\n"
        "0 0 0 4 1 9 0 0 5\n"
        "0 0 0 0 8 0 0 7 9"
    )
    assert parse_sudoku(test_board) == [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], 
        [6, 0, 0, 1, 9, 5, 0, 0, 0], 
        [0, 9, 8, 0, 0, 0, 0, 6, 0], 
        [8, 0, 0, 0, 6, 0, 0, 0, 3], 
        [4, 0, 0, 8, 0, 3, 0, 0, 1], 
        [7, 0, 0, 0, 2, 0, 0, 0, 6], 
        [0, 6, 0, 0, 0, 0, 2, 8, 0], 
        [0, 0, 0, 4, 1, 9, 0, 0, 5], 
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

def test_parser_wrong_num_of_rows():
    test_board = (            # 8 rows
        "5 3 0 0 7 0 0 0 0\n"
        "6 0 0 1 9 5 0 0 0\n"
        "0 9 8 0 0 0 0 6 0\n"
        "8 0 0 0 6 0 0 0 3\n"
        "4 0 0 8 0 3 0 0 1\n"
        "7 0 0 0 2 0 0 0 6\n"
        "0 6 0 0 0 0 2 8 0\n"
        "0 0 0 0 8 0 0 7 9"
    )
    with pytest.raises(ValueError):
        parse_sudoku(test_board)

def test_parser_wrong_num_of_cells():
    test_board = (
        "5 3 0 0 7 0 0 0 0\n"
        "6 0 0 1 9 5 0 0 0\n"
        "0 9 8 0 0 0 0 6 0\n"
        "8 0 0 0 6 0 0 0 3\n"
        "4 0 0 8 0 3 0 0\n"   # 8 cells
        "7 0 0 0 2 0 0 0 6\n"
        "0 6 0 0 0 0 2 8 0\n"
        "0 0 0 4 1 9 0 0 5\n"
        "0 0 0 0 8 0 0 7 9"
    )
    with pytest.raises(ValueError):
        parse_sudoku(test_board)

def test_parser_invalid_char():
    test_board = (
        "5 3 0 0 7 0 0 0 0\n"
        "6 0 0 1 9 5 0 0 0\n"
        "0 9 8 0 0 0 0 6 0\n"
        "8 0 0 0 6 0 0 0 3\n"
        "4 0 0 8 * 3 0 0 1\n" # invalid '*' char
        "7 0 0 0 2 0 0 0 6\n"
        "0 6 0 0 0 0 2 8 0\n"
        "0 0 0 4 1 9 0 0 5\n"
        "0 0 0 0 8 0 0 7 9"
    )
    with pytest.raises(ValueError):
        parse_sudoku(test_board)

def test_parser_num_greater_than_9():
    test_board = (
        "5 3 0 0 7 0 0 0 0\n"
        "6 0 0 1 9 5 0 0 0\n"
        "0 9 8 0 0 0 0 6 0\n"
        "8 0 0 0 6 0 0 0 3\n"
        "4 0 0 8 12 3 0 0 1\n" # invalid '12'
        "7 0 0 0 2 0 0 0 6\n"
        "0 6 0 0 0 0 2 8 0\n"
        "0 0 0 4 1 9 0 0 5\n"
        "0 0 0 0 8 0 0 7 9"
    )
    with pytest.raises(ValueError):
        parse_sudoku(test_board)

def test_parser_num_negative():
    test_board = (
        "5 3 0 0 7 0 0 0 0\n"
        "6 0 0 1 9 5 0 0 0\n"
        "0 9 8 0 0 0 0 6 0\n"
        "8 0 0 0 6 0 0 0 3\n"
        "4 0 0 8 -1 3 0 0 1\n" # invalid '-1'
        "7 0 0 0 2 0 0 0 6\n"
        "0 6 0 0 0 0 2 8 0\n"
        "0 0 0 4 1 9 0 0 5\n"
        "0 0 0 0 8 0 0 7 9"
    )
    with pytest.raises(ValueError):
        parse_sudoku(test_board)

def test_same_num_in_same_row_is_unsafe():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], # 8th cell -> 5, conflict with 5 on the left
        [6, 0, 0, 1, 9, 5, 0, 0, 0], 
        [0, 9, 8, 0, 0, 0, 0, 6, 0], 
        [8, 0, 0, 0, 6, 0, 0, 0, 3], 
        [4, 0, 0, 8, 0, 3, 0, 0, 1], 
        [7, 0, 0, 0, 2, 0, 0, 0, 6], 
        [0, 6, 0, 0, 0, 0, 2, 8, 0], 
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]  
    ]
    assert not sudoku_is_safe(board, 0, 7, 5)

def test_same_num_in_same_col_is_unsafe():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], 
        [6, 0, 0, 1, 9, 5, 0, 0, 0], 
        [0, 9, 8, 0, 0, 0, 0, 6, 0], 
        [8, 0, 0, 0, 6, 0, 0, 0, 3], 
        [4, 0, 0, 8, 0, 3, 0, 0, 1], 
        [7, 0, 0, 0, 2, 0, 0, 0, 6], 
        [0, 6, 0, 0, 0, 0, 2, 8, 0], 
        [0, 0, 0, 4, 1, 9, 0, 0, 5], # 3rd cell -> 8, conflict with 8 above
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    assert not sudoku_is_safe(board, 7, 2, 8)

def test_same_num_in_same_box_is_unsafe():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], 
        [6, 0, 0, 1, 9, 5, 0, 0, 0], 
        [0, 9, 8, 0, 0, 0, 0, 6, 0], 
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1], 
        [7, 0, 0, 0, 2, 0, 0, 0, 6], # 4th -> 3, conflict with 3 in same box
        [0, 6, 0, 0, 0, 0, 2, 8, 0], 
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    assert not sudoku_is_safe(board, 5, 3, 3)

def test_num_in_safe_position():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], 
        [6, 0, 0, 1, 9, 5, 0, 0, 0], # 8th -> 2, safe
        [0, 9, 8, 0, 0, 0, 0, 6, 0], 
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1], 
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0], 
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    assert sudoku_is_safe(board, 1, 7, 2)

def test_replace_cell_with_same_num():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], 
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0], 
        [8, 0, 0, 0, 6, 0, 0, 0, 3], # 5th -> 6, which is the same
        [4, 0, 0, 8, 0, 3, 0, 0, 1], 
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0], 
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    assert sudoku_is_safe(board, 3, 4, 6)

def test_replace_cell_with_conflict_num():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], 
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0], 
        [8, 0, 0, 0, 6, 0, 0, 0, 3], # 5th -> 9, conflict with 9 above
        [4, 0, 0, 8, 0, 3, 0, 0, 1], 
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0], 
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    assert not sudoku_is_safe(board, 3, 4, 9)

def test_contradictory_board():
    board = [
        [4, 8, 0, 0, 5, 0, 0, 2, 3], # 5th col 5 contradicts with 5 below
        [0, 5, 0, 0, 0, 0, 0, 6, 7],
        [0, 6, 0, 9, 0, 7, 4, 0, 1], 
        [1, 0, 9, 0, 0, 0, 3, 4, 0],
        [7, 3, 0, 0, 0, 0, 1, 8, 9], 
        [0, 0, 0, 1, 9, 0, 0, 0, 6],
        [2, 0, 0, 4, 5, 9, 0, 0, 0], 
        [0, 9, 8, 2, 0, 0, 7, 3, 4],
        [0, 1, 4, 7, 3, 8, 0, 0, 0]
    ]
    with pytest.raises(ValueError):
        solve_sudoku(board)

def test_solvable_board():
    board = [
        [4, 8, 0, 0, 0, 0, 0, 2, 3], 
        [0, 5, 0, 0, 0, 0, 0, 6, 7],
        [0, 6, 0, 9, 0, 7, 4, 0, 1], 
        [1, 0, 9, 0, 0, 0, 3, 4, 0],
        [7, 3, 0, 0, 0, 0, 1, 8, 9], 
        [0, 0, 0, 1, 9, 0, 0, 0, 6],
        [2, 0, 0, 4, 5, 9, 0, 0, 0], 
        [0, 9, 8, 2, 0, 0, 7, 3, 4],
        [0, 1, 4, 7, 3, 8, 0, 0, 0]
    ]
    assert solve_sudoku(board) is not None

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
    assert solve_sudoku(board)[4][4] == 4

def test_unsolvable_board():
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
    assert solve_sudoku(board) is None

def test_already_complete_board():
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
    assert solve_sudoku(board) == board

def test_solve_easy_board():
    board = parse_sudoku(read_sudoku_file("examples/sudoku_easy.txt"))
    original_board = [row.copy() for row in board]
    solved_board = solve_sudoku(board)

    assert solved_board is not None
    assert sudoku_board_is_valid(solved_board)
    assert all(0 not in row for row in solved_board)
    assert board == original_board

    for row in range(9):
        for col in range(9):
            if original_board[row][col] != 0:
                assert solved_board[row][col] == original_board[row][col]