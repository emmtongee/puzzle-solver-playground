# board: [2, 4] -> queens at row 0 col 2, row 1 col 4
def is_safe(board, row, col):

    """
    Return True if a queen can be placed at (row, col)
    without attacking any existing queens.

    board[i] represents the column of the queen in row i.
    """
    for prev_row, prev_col in enumerate(board):
        if prev_col == col: return False
        if abs(row - prev_row) == abs(col - prev_col): return False
    return True