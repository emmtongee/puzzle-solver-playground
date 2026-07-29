from time import perf_counter

from src.solvers.sudoku import (
    parse_sudoku, 
    read_sudoku_file, 
    sudoku_board_is_valid, 
    solve_sudoku, 
    mrv_solve_sudoku
)

def sudoku_board_is_complete_and_valid(board):
    if board is None:
        return False
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return False
    return sudoku_board_is_valid(board)

print("Sudoku Comparison\n-----------------------------")

easy_board = parse_sudoku(read_sudoku_file("examples/sudoku_easy.txt"))
hard_board = parse_sudoku(read_sudoku_file("examples/sudoku_hard.txt"))

for difficulty, board in (("Easy", easy_board), ("Hard", hard_board)):

    naive_runtime_list = []
    naive_candidate_check_counts = []
    naive_solution = None

    for _ in range(5):
        start = perf_counter()
        naive_solution, candidates_checked = solve_sudoku(board)
        naive_runtime_list.append(perf_counter() - start)
        naive_candidate_check_counts.append(candidates_checked)

    naive_counts_are_deterministic = len(set(naive_candidate_check_counts)) == 1
    naive_formatted_runtime_list = [f"{runtime:.6f}" for runtime in naive_runtime_list]

    mrv_runtime_list = []
    mrv_candidate_check_counts = []
    mrv_solution = None

    for _ in range(5):
        start = perf_counter()
        mrv_solution, candidates_checked = mrv_solve_sudoku(board)
        mrv_runtime_list.append(perf_counter() - start)
        mrv_candidate_check_counts.append(candidates_checked)

    mrv_counts_are_deterministic = len(set(mrv_candidate_check_counts)) == 1
    mrv_formatted_runtime_list = [f"{runtime:.6f}" for runtime in mrv_runtime_list]

    print(f"Board: {difficulty}")
    print()
    print("Naive Solver")
    print(f"Candidate checks: {naive_candidate_check_counts}")
    print(f"Candidate checks deterministic: {naive_counts_are_deterministic}")
    print(f"Runtimes in seconds: {naive_formatted_runtime_list}")
    print(f"Solution returned: {naive_solution is not None}")
    print(f"Solution valid: {sudoku_board_is_complete_and_valid(naive_solution)}")
    print()
    print("MRV Solver")
    print(f"Candidate checks: {mrv_candidate_check_counts}")
    print(f"Candidate checks deterministic: {mrv_counts_are_deterministic}")
    print(f"Runtimes in seconds: {mrv_formatted_runtime_list}")
    print(f"Solution returned: {mrv_solution is not None}")
    print(f"Solution valid: {sudoku_board_is_complete_and_valid(mrv_solution)}")
    print()
    print(f"Naive and MRV solutions equal: {naive_solution == mrv_solution}")
    print("-----------------------------")