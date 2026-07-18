def format_n_queens_board(solution):
    rows = []

    for queen_col in solution:
        row = ["."] * len(solution)
        row[queen_col] = "Q"
        rows.append(" ".join(row))

    return "\n".join(rows)

def format_sudoku_board(board):
    rows = []

    for row_index, row in enumerate(board):
        box_strings = []
        cell_strings = []

        for i in range(9):
            # replace numbers with strings
            cell_strings.append('.' if row[i] == 0 else str(row[i]))

            # join cells in the same box
            if i % 3 == 2:
                box_strings.append(" ".join(cell_strings))
                cell_strings = []
            
        rows.append(" | ".join(box_strings))

        # add separator after rows 3 and 6
        if row_index in (2, 5): 
            rows.append("------+-------+------")

    return "\n".join(rows)