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


# input file path, output board string
def read_sudoku_file(path):

    with open(path) as f:
        return f.read()


# input board string, output board 2D list
def parse_sudoku(board_str):

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


# Checks whether a value can occupy a coordinate while ignoring only the value currently at that coordinate
def sudoku_is_safe(board, row, col, num):

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