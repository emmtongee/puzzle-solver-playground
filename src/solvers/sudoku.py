"""
Sudoku board representation:
A 2D list of 9x9 integers from 0-9, 
where 0 represents an empty cell and 1-9 represents cells filled with the corresponding numbers.
Indexes are zero-based.

e.g.
[
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    ...
]

Candidate-check count:
The number of candidate values tested for validity at a cell during the search.

A candidate check is one call to sudoku_is_safe during the search.
"""


def read_sudoku_file(path: str) -> str:
    """
    Read the text file with path and return the content as a string.
    """
    with open(path) as f:
        return f.read()

def parse_sudoku(board_str: str) -> list[list[int]]:
    """
    Parse the string representing a board and return a 2D list.
    Raise ValueError if:
    - the board has more than or less than 9 rows
    - one of the rows has more than or less than 9 cells
    - one of the cells is not an integer from 0 to 9
    """

    line_list = board_str.strip().split('\n')
    if len(line_list) != 9:
        raise ValueError("Board has less than or more than 9 rows")
    output_list = []
    for i in range(9):
        line_string = line_list[i].split()
        for cell in line_string:
            if cell not in '0123456789' or len(cell) != 1:
                raise ValueError("Each cell must be a single digit from 0 to 9")
        line = list(map(int, line_string))
        if len(line) != 9:
            raise ValueError(f"Row {i} has less than or more than 9 cells")
        output_list.append(line)
        
    return output_list

def sudoku_is_safe(
    board: list[list[int]],
    row: int,
    col: int,
    num: int,
) -> bool:
    """
    Check whether a value can occupy a cell with coordinates (row, col) without conflict, 
    while ignoring only the value currently at that coordinate.
    Raise ValueError if num is not an integer from 1 to 9.
    """
    # num not from 1-9
    if num not in range(1,10):
        raise ValueError("num not from 1 to 9")

    # row conflict
    for current_col in range(9):
        if board[row][current_col] == num and current_col != col:
            return False
    
    # column conflict
    for current_row in range(9):
        if board[current_row][col] == num and current_row != row:
            return False
        
    # box conflict
    box_row, box_col = row//3, col//3
    box_index_arr = ((0,1,2),(3,4,5),(6,7,8)) # cells in same tuple are in same box

    for current_row in box_index_arr[box_row]:
        for current_col in box_index_arr[box_col]:
            if board[current_row][current_col] == num and not(current_row == row and current_col == col):
                return False
    
    return True

def sudoku_board_is_valid(board: list[list[int]]) -> bool:
    """
    Check whether all existing non-zero cells (clues) are mutually consistent.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0 and not sudoku_is_safe(board, row, col, board[row][col]):
                return False
    return True

def solve_sudoku(board: list[list[int]]) -> tuple[list[list[int]] | None, int]:
    '''
    Validate the initial clues and raise ValueError if clues contradict each other.
    Solve and return a copy of the board, along with the candidate-check count.
    If no solution exists, return None as the board together with the count.
    Do not modify the input.
    Already complete board is returned as its copy.
    '''
    
    if not sudoku_board_is_valid(board):
        raise ValueError("Clues contradict each other")
    
    board_copy = [row.copy() for row in board]
    
    def backtrack(board, row, col, candidates_checked):
        if row == 9:
            return board, candidates_checked
        elif col == 9:
            return backtrack(board, row+1, 0, candidates_checked)
        elif board[row][col] != 0:
            return backtrack(board, row, col+1, candidates_checked)
        else:
            for num in range(1,10):
                candidates_checked += 1
                if sudoku_is_safe(board, row, col, num):
                    board[row][col] = num
                    result, candidates_checked = backtrack(board, row, col+1, candidates_checked)
                    if result is not None:
                        return result, candidates_checked
                    board[row][col] = 0
            return None, candidates_checked

    return backtrack(board_copy, 0, 0, 0)

def sudoku_get_cell_candidates(
    board: list[list[int]],
    row: int,
    col: int,
) -> tuple[list[int], int]:
    """
    For the empty cell at (row, col),
    return a list of its valid candidates in ascending order, and the candidate-check count.
    The board is not modified.
    Assume the board is valid and the specified cell is empty. 
    """
    valid_candidates = []
    candidates_checked = 0
    for candidate in range(1, 10):
        candidates_checked += 1
        if sudoku_is_safe(board, row, col, candidate):
            valid_candidates.append(candidate)
    return valid_candidates, candidates_checked


def sudoku_select_mrv_cell(
    board: list[list[int]],
) -> tuple[int | None, int | None, list[int] | None, int]:
    """
    Select the empty cell with the fewest legal candidates.
    Ties are resolved in row-major order (from top to bottom, then from left to right).

    Return (None, None, None, 0) if the board has no empty cells. 
    Otherwise, return the selected row, column, candidates, and total candidate-check count during selection.
    An empty candidate list indicates a dead-end board state.

    The board is assumed to be valid and is not modified.
    """
    target_row, target_col = None, None
    target_candidate_num = 10 # at most 9 candidates
    target_candidate_list = None
    candidates_checked = 0

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                current_candidate_list, candidate_increment = (
                    sudoku_get_cell_candidates(board, row, col)
                )
                current_candidate_num = len(current_candidate_list)
                candidates_checked += candidate_increment

                if current_candidate_num < target_candidate_num:
                    (target_row, target_col) = (row, col)
                    target_candidate_num = current_candidate_num
                    target_candidate_list = current_candidate_list

                    if current_candidate_num == 0:
                        return (row, col, [], candidates_checked)

    if target_row is None:
        return None, None, None, 0
    return target_row, target_col, target_candidate_list, candidates_checked

def mrv_solve_sudoku(board: list[list[int]]) -> tuple[list[list[int]] | None, int]:
    """
    Validate the initial clues and raise ValueError if clues contradict each other.
    Solve and return a copy of the board, along with the candidate-check count.
    If no solution exists, return None as the board together with the count.
    Use MRV algorithm.
    Do not modify the input.
    Already complete board is returned as its copy.
    """
    
    if not sudoku_board_is_valid(board):
        raise ValueError("Clues contradict each other")
    
    board_copy = [row.copy() for row in board]
    
    def backtrack(board, candidates_checked):
        row, col, candidate_list, check_count = sudoku_select_mrv_cell(board)
        candidates_checked += check_count
        if row is None:
            return board, candidates_checked
        assert candidate_list is not None
        if candidate_list == []:
            return None, candidates_checked
        for candidate in candidate_list:
            board[row][col] = candidate
            result, candidates_checked = backtrack(board, candidates_checked)
            if result is not None:
                return result, candidates_checked
            board[row][col] = 0
        return None, candidates_checked

    return backtrack(board_copy, 0)