"""
Record raw work counts and five runtime measurements for each solver and input size. 
Do not expect the two work metrics to have identical meanings: one counts subsets and the other counts DP states.
"""

from time import perf_counter

from src.solvers.knapsack import (
    solve_knapsack,
    dynamic_solve_knapsack
)

print("Knapsack Comparison\n-----------------------------")

# 1st column: low-weight low-value
# 2nd column: low-weight high-value
# 3rd column: high-weight low-value
# 4th column: high-weight high-value
items = [
    (3, 2), (4, 6), (7, 5), (8, 8),
    (2, 1), (3, 5), (6, 5), (9, 10),
    (1, 1), (2, 5), (5, 6), (7, 9),
    (2, 2), (4, 7), (6, 6), (10, 12)
]
num_of_items_list = (4, 8, 12, 16)
capacity = 20

for num_of_items in num_of_items_list:

    bruteforce_runtime_list = []
    bruteforce_subset_counts = []
    bruteforce_solution = None

    for _ in range(5):
        start = perf_counter()
        bruteforce_solution, subsets_checked = solve_knapsack(items[:num_of_items], capacity)
        bruteforce_runtime_list.append(perf_counter() - start)
        bruteforce_subset_counts.append(subsets_checked)

    bruteforce_counts_are_deterministic = len(set(bruteforce_subset_counts)) == 1
    bruteforce_formatted_runtime_list = [f"{runtime:.6f}" for runtime in bruteforce_runtime_list]

    dynamic_runtime_list = []
    dynamic_state_counts = []
    dynamic_solution = None

    for _ in range(5):
        start = perf_counter()
        dynamic_solution, states_calculated = dynamic_solve_knapsack(items[:num_of_items], capacity)
        dynamic_runtime_list.append(perf_counter() - start)
        dynamic_state_counts.append(states_calculated)

    dynamic_counts_are_deterministic = len(set(dynamic_state_counts)) == 1
    dynamic_formatted_runtime_list = [f"{runtime:.6f}" for runtime in dynamic_runtime_list]

    print(f"Number of items: {num_of_items}")
    print()
    print("Brute Force Solver")
    print(f"Subsets checked: {bruteforce_subset_counts}")
    print(f"Subset checks deterministic: {bruteforce_counts_are_deterministic}")
    print(f"Runtimes in seconds: {bruteforce_formatted_runtime_list}")
    print(f"Solution returned: {bruteforce_solution is not None}")
    print()
    print("Dynamic Programming Solver")
    print(f"States calculated: {dynamic_state_counts}")
    print(f"State counts deterministic: {dynamic_counts_are_deterministic}")
    print(f"Runtimes in seconds: {dynamic_formatted_runtime_list}")
    print(f"Solution returned: {dynamic_solution is not None}")
    print()
    print(f"Brute Force and DP solutions equal: {bruteforce_solution == dynamic_solution}")
    print("-----------------------------")