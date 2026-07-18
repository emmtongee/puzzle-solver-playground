from time import perf_counter

from src.solvers.n_queens import solve_n_queens
from src.solvers.sudoku import solve_sudoku, read_sudoku_file, parse_sudoku
from src.utils.display import format_sudoku_board

def main():
    choice = int(input("n-queen (1) or sudoku (2): "))
    if choice == 1:

        n = 8

        start = perf_counter()
        solutions, states_checked = solve_n_queens(n)
        runtime = perf_counter() - start

        print("Function: solve_n_queens")
        print(f"N: {n}")
        print(f"Solutions: {len(solutions)}")
        print(f"States checked: {states_checked}")
        print(f"Runtime: {runtime:.6f} seconds")
    
    elif choice == 2:
    
        easy_board = parse_sudoku(read_sudoku_file("examples/sudoku_easy.txt"))
        hard_board = parse_sudoku(read_sudoku_file("examples/sudoku_hard.txt"))

        start = perf_counter()
        solved_board, candidates_checked = solve_sudoku(easy_board)
        runtime = perf_counter() - start

        print("Function: solve_sudoku")
        print(f"Board: Easy\n{format_sudoku_board(easy_board)}")
        print(f"Solved board: \n{format_sudoku_board(solved_board)}")
        print(f"Candidates checked: {candidates_checked}")
        print(f"Runtime: {runtime:.6f} seconds")

        print("-----------------------------")

        start = perf_counter()
        solved_board, candidates_checked = solve_sudoku(hard_board)
        runtime = perf_counter() - start

        print("Function: solve_sudoku")
        print(f"Board: Hard\n{format_sudoku_board(hard_board)}")
        print(f"Solved board: \n{format_sudoku_board(solved_board)}")
        print(f"Candidates checked: {candidates_checked}")
        print(f"Runtime: {runtime:.6f} seconds")



if __name__ == "__main__":
    main()