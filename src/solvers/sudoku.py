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
"""


def read_sudoku_file(path):
    """
    Read the text file with path and return the content as a string.
    """
    with open(path) as f:
        return f.read()

def parse_sudoku(board_str):
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

def sudoku_is_safe(board, row, col, num):
    """
    Check whether a value can occupy a cell with coordinates (row, col) without conflict, 
    while ignoring only the value currently at that coordinate.
    Raise ValueError if num is not an integer from 1 to 9.
    """
    # num not from 1-9
    if num not in range(1,10):
        raise ValueError("num not from 1 to 9")

    # row conflict
    for i in range(9):
        if board[row][i] == num and i != col:
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

def sudoku_board_is_valid(board):
    """
    Check whether all existing non-zero cells (clues) are mutually consistent.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0 and not sudoku_is_safe(board, row, col, board[row][col]):
                return False
    return True

def solve_sudoku(board):
    '''
    Validate the initial clues and raise ValueError if clues contradict each other.
    Solve and return a copy of the board, along with the number of times the algorithm considers a number placement.
    Return None board if no solution exists.
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
                    if result:
                        return result, candidates_checked
                    board[row][col] = 0
            return None, candidates_checked

    return backtrack(board_copy, 0, 0, 0)

def sudoku_get_cell_candidates(board, row, col):
    """
    Return a list of valid candidates in ascending order, for the empty cell at (row, col).
    The board is not modified.
    Assume the board is valid and the specified cell is empty. 
    """
    valid_candidates = []
    for candidate in range(1, 10):
        if sudoku_is_safe(board, row, col, candidate):
            valid_candidates.append(candidate)
    return valid_candidates


def sudoku_select_mrv_cell(board):
    """
    Select the empty cell with the fewest legal candidates.
    Ties are resolved in row-major order (from top to bottom, then from left to right).

    Return None if the board has no empty cells. 
    Otherwise, return ((row, col), candidates). 
    An empty candidate list indicates a dead-end board state.

    The board is assumed to be valid and is not modified.
    """
    target_cell = None
    target_candidate_num = 10 # at most 9 candidates
    target_candidate_list = None

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                current_candidate_list = sudoku_get_cell_candidates(board, row, col)
                current_candidate_num = len(current_candidate_list)
                if current_candidate_num < target_candidate_num:
                    target_cell = (row, col)
                    target_candidate_num = current_candidate_num
                    target_candidate_list = current_candidate_list

                    if current_candidate_num == 0:
                        return (target_cell, [])

    if target_cell is None:
        return None
    return (target_cell, target_candidate_list)