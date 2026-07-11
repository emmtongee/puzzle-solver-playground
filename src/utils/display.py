def format_n_queens_board(solution):
    rows = []

    for queen_col in solution:
        row = ["."] * len(solution)
        row[queen_col] = "Q"
        rows.append(" ".join(row))

    return "\n".join(rows)