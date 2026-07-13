import pytest

from src.solvers.sudoku import read_sudoku_file, parse_sudoku, sudoku_is_safe

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