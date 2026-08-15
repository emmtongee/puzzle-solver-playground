"""
A Knapsack problem is represented by:
- items: a list of all items, where each item is a tuple (weight, value); and
- capacity: the maximum capacity of the knapsack
Weight, value and capacity are integers.

e.g.
items: [(3, 4), (2, 3), (1, 1)]
capacity: 5

Non-integer and malformed inputs are outside the supported contract.

Binary sum: sum of 2 to the power of the elements
e.g. the binary sum of {0,2} is 2^0+2^2 = 5
"""

def knapsack_problem_is_valid(
    items: list[tuple[int, int]],
    capacity: int,
) -> bool:
    """
    Validate the problem.
    If any of the following is true, return False:
    - one of the items has negative weight or value
    - the capacity is negative
    """
    if capacity < 0:
        return False
    for weight, value in items:
        if weight < 0:
            return False
        if value < 0:
            return False
    return True

def number_power_set(num: int) -> list[set[int]]:
    """
    Return a list of all subsets of the set {0, 1, 2, ..., num - 1}, 
    in the ascending order of the binary sum.
    e.g. number_power_set(3) -> [{}, {0}, {1}, {0,1}, {2}, {0,2}, {1,2}, {0,1,2}]
    """
    output_list: list[set[int]] = []
    def recurse(n, number_set):

        # every number has now been either excluded or included
        if n == -1:
            output_list.append(number_set.copy())
            return

        # explore subsets excluding n first
        # every such subset has a smaller binary sum than
        # every subset containing n, because:
        # 2**n > 2**(n - 1) + 2**(n - 2) + ... + 1
        recurse(n - 1, number_set)
        number_set.add(n)
        recurse(n - 1, number_set)
        number_set.remove(n)

    recurse(num - 1, set())
    return output_list

def solve_knapsack(
    items: list[tuple[int, int]],
    capacity: int,
) -> tuple[tuple[int, set[int]], int]:
    """
    Solve the Knapsack problem, 
    i.e. select the items such that the total weight does not exceed the capacity and the total value is maximized.
    Return the maximum total value and a set of indices of selected items, 
    along with the number of subsets of items evaluated, including the empty subset.

    If two or more combinations produce the same maximum total value, 
    the combination whose index set has the least binary sum is selected.
    Do not modify the input.
    """

    # validation
    if not knapsack_problem_is_valid(items, capacity):
        raise ValueError("Input is invalid")
    
    max_total_value = -1
    max_total_value_indices = set()
    subsets_checked = 0

    for indices in number_power_set(len(items)):
        subsets_checked += 1
        total_value = 0
        total_weight = 0
        for index in indices:
            weight, value = items[index]
            total_weight += weight
            total_value += value
        if total_weight <= capacity and total_value > max_total_value:
            max_total_value = total_value
            max_total_value_indices = indices

    return (max_total_value, max_total_value_indices), subsets_checked

def dynamic_solve_knapsack(
    items: list[tuple[int, int]],
    capacity: int,
) -> tuple[tuple[int, set[int]], int]:
    """
    Solve the Knapsack problem using bottom-up dynamic programming.
    Return the maximum total value and a set of indices of selected items,
    along with the number of non-initial table states calculated.
    Initialization states are excluded.

    If two or more combinations produce the same maximum total value, 
    the combination whose index set has the least binary sum is selected.
    Do not modify the input.
    """

    # validation
    if not knapsack_problem_is_valid(items, capacity):
        raise ValueError("Input is invalid")
    
    # construct the DP table and its first row
    # each cell contains the max total value and the corresponding index set
    # the first 0 items always have value 0
    dp_table: list[list[tuple[int, set[int]]]] = [
        [(0, set()) for _ in range(capacity + 1)]
    ]
    states_calculated = 0

    for num_of_items in range(1, len(items) + 1):

        dp_table.append([])

        for allowed_capacity in range(capacity + 1):

            states_calculated += 1

            # if current item is excluded:
            # best value = best value with all previous items and same capacity
            prev_cell_if_item_excluded = dp_table[num_of_items - 1][allowed_capacity]
            max_total_value_if_item_excluded = prev_cell_if_item_excluded[0]

            current_item_weight, current_item_value = items[num_of_items - 1]

            remaining_capacity = allowed_capacity - current_item_weight
            if remaining_capacity >= 0:

                # if current item is included:
                # best value = best value with all previous items and remaining capacity + current item value
                prev_cell_if_item_included = dp_table[num_of_items - 1][remaining_capacity]
                max_total_value_if_item_included = prev_cell_if_item_included[0] + current_item_value

                # on equal values, exclude the current item, because
                # its binary value > binary sum of all earlier item indices:
                # 2**n > 2**(n - 1) + 2**(n - 2) + ... + 1
                if max_total_value_if_item_excluded >= max_total_value_if_item_included:
                    index_set = prev_cell_if_item_excluded[1].copy()
                    next_cell = (max_total_value_if_item_excluded, index_set)
                else:
                    index_set = prev_cell_if_item_included[1].copy()
                    index_set.add(num_of_items - 1)
                    next_cell = (max_total_value_if_item_included, index_set)

            else:
                # current item does not fit, so it must be excluded
                index_set = prev_cell_if_item_excluded[1].copy()
                next_cell = (max_total_value_if_item_excluded, index_set)

            dp_table[num_of_items].append(next_cell)

    return dp_table[len(items)][capacity], states_calculated