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

def knapsack_problem_is_valid(items, capacity):
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

def number_power_set(num):
    """
    Return a list of all subsets of the set {0, 1, 2, ..., num - 1}, 
    in the ascending order of the binary sum.
    e.g. number_power_set(3) -> [{}, {0}, {1}, {0,1}, {2}, {0,2}, {1,2}, {0,1,2}]
    """
    output_list = []
    def recurse(index, number_set):
        if index == -1:
            output_list.append(number_set.copy())
            return
        recurse(index - 1, number_set)
        number_set.add(index)
        recurse(index - 1, number_set)
        number_set.remove(index)
    recurse(num - 1, set())
    return output_list

def solve_knapsack(items, capacity):
    """
    Solve the Knapsack problem, 
    i.e. select the items such that the total weight does not exceed the capacity and the total value is maximum.
    Return the maximum total value and a set of indices of selected items.

    If two or more combinations produce the same maximum total value, 
    the combination whose index set has the least binary sum is selected.
    Do not modify the input.
    """

    if not knapsack_problem_is_valid(items, capacity):
        raise ValueError("Input is invalid")
    
    max_total_value = -1
    max_total_value_indices = None

    for indices in number_power_set(len(items)):
        total_value = 0
        total_weight = 0
        for index in indices:
            weight, value = items[index]
            total_weight += weight
            total_value += value
        if total_weight <= capacity and total_value > max_total_value:
            max_total_value = total_value
            max_total_value_indices = indices

    return max_total_value, max_total_value_indices