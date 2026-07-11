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

def solve_n_queens(n):
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
            if is_safe(board, row, col):
                board.append(col)
                states_checked += backtrack(row+1)
                board.pop()

        return states_checked

    states_checked = backtrack(0)
    return solutions, states_checked