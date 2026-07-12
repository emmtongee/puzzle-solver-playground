from time import perf_counter

from src.solvers.n_queens import solve_n_queens

def main():
    n = 8

    start = perf_counter()
    solutions, states_checked = solve_n_queens(n)
    runtime = perf_counter() - start

    print("Function: solve_n_queens")
    print(f"N: {n}")
    print(f"Solutions: {len(solutions)}")
    print(f"States checked: {states_checked}")
    print(f"Runtime: {runtime:.6f} seconds")



if __name__ == "__main__":
    main()