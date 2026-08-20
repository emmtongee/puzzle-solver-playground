from time import perf_counter

from src.solvers.n_queens import solve_n_queens
from src.solvers.sudoku import solve_sudoku, read_sudoku_file, parse_sudoku
from src.solvers.knapsack import dynamic_solve_knapsack
from src.utils.display import format_sudoku_board


def n_queens_demo():
    print("-----------------------------")

    n = 8

    start = perf_counter()
    solutions, states_checked = solve_n_queens(n)
    runtime = perf_counter() - start

    print("Function: solve_n_queens")
    print(f"N: {n}")
    print(f"Solutions: {len(solutions)}")
    print(f"States checked: {states_checked}")
    print(f"Runtime: {runtime:.6f} seconds")

    print("-----------------------------")

def sudoku_demo():
    print("-----------------------------")

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

    print("-----------------------------")

def knapsack_demo():
    print("-----------------------------")

    items = [(3, 4), (2, 3), (1, 1)]
    capacity = 5

    start = perf_counter()
    solution, states_calculated = dynamic_solve_knapsack(items, capacity)
    runtime = perf_counter() - start
    maximum_value, selected_items = solution

    print(f"Items: {items}")
    print(f"Capacity: {capacity}")
    print(f"Maximum value: {maximum_value}")
    print("Selected items:")
    for index in sorted(selected_items):
        weight, value = items[index]
        print(f"Item {index + 1}: weight {weight}, value {value}")
    print(f"States calculated: {states_calculated}")
    print(f"Runtime: {runtime:.6f} seconds")

    print("-----------------------------")


MENU_MESSAGE = (
    "1. N-Queens\n"
    "2. Sudoku\n"
    "3. Knapsack\n"
    "4. Exit"
)


def main():
    while True:
        print(MENU_MESSAGE)
        choice = input("Choose one: ").strip()

        if choice == "1":
            n_queens_demo()
        elif choice == "2":
            sudoku_demo()
        elif choice == "3":
            knapsack_demo()
        elif choice == "4":
            return
        else:
            print("Error: invalid choice")


if __name__ == "__main__":
    main()