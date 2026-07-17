"""
N-Queens board representation:
For n*n board, a list of n integers such that the i th integer represents the column position of the queen on the i-th row.
Indexes are zero-based.

e.g. [2,0,3,1] means there are 4 queens at (0,2), (1,0), (2,3), (3,1), or:
. . Q .
Q . . .
. . . Q
. Q . .
"""


def n_queens_is_safe(board, row, col):
    """
    Return True if a queen can be placed at (row, col)
    without attacking any existing queens.

    board[i] represents the column of the queen in row i.
    """
    for prev_row, prev_col in enumerate(board):
        if prev_col == col: return False
        if abs(row - prev_row) == abs(col - prev_col): return False
    return True

def solve_n_queens(n):
    """
    Return a list containing all solutions for a n*n board, 
    and the number of times the algorithm considers a queen placement.
    """
    if n < 0:
        raise ValueError("solve_n_queens() does not accept negative integers")
    if n == 0: 
        return [], 0

    solutions = []
    board = []

    def backtrack(row):
        states_checked = 0

        if row == n:
            solutions.append(board.copy())
            return 0
        
        for col in range(n):
            states_checked += 1
            if n_queens_is_safe(board, row, col):
                board.append(col)
                states_checked += backtrack(row+1)
                board.pop()

        return states_checked

    states_checked = backtrack(0)
    return solutions, states_checked