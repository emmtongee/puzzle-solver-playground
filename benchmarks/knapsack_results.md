# Knapsack Comparison Results

Each solver is called five times for each input size, using a fixed capacity of 20. The results are as follows:

```text
Knapsack Comparison
-----------------------------
Number of items: 4

Brute Force Solver
Subsets checked: [16, 16, 16, 16, 16]
Subset checks deterministic: True
Runtimes in seconds: ['0.000012', '0.000007', '0.000005', '0.000005', '0.000004']
Solution returned: True

Dynamic Programming Solver
States calculated: [84, 84, 84, 84, 84]
State counts deterministic: True
Runtimes in seconds: ['0.000025', '0.000018', '0.000017', '0.000016', '0.000016']
Solution returned: True

Brute Force and DP solutions equal: True
-----------------------------
Number of items: 8

Brute Force Solver
Subsets checked: [256, 256, 256, 256, 256]
Subset checks deterministic: True
Runtimes in seconds: ['0.000097', '0.000204', '0.000096', '0.000097', '0.000087']
Solution returned: True

Dynamic Programming Solver
States calculated: [168, 168, 168, 168, 168]
State counts deterministic: True
Runtimes in seconds: ['0.000040', '0.000034', '0.000032', '0.000031', '0.000032']
Solution returned: True

Brute Force and DP solutions equal: True
-----------------------------
Number of items: 12

Brute Force Solver
Subsets checked: [4096, 4096, 4096, 4096, 4096]
Subset checks deterministic: True
Runtimes in seconds: ['0.002251', '0.002198', '0.002133', '0.004746', '0.001875']
Solution returned: True

Dynamic Programming Solver
States calculated: [252, 252, 252, 252, 252]
State counts deterministic: True
Runtimes in seconds: ['0.000053', '0.000045', '0.000043', '0.000043', '0.000042']
Solution returned: True

Brute Force and DP solutions equal: True
-----------------------------
Number of items: 16

Brute Force Solver
Subsets checked: [65536, 65536, 65536, 65536, 65536]
Subset checks deterministic: True
Runtimes in seconds: ['0.040472', '0.042155', '0.046264', '0.174426', '0.039789']
Solution returned: True

Dynamic Programming Solver
States calculated: [336, 336, 336, 336, 336]
State counts deterministic: True
Runtimes in seconds: ['0.000067', '0.000057', '0.000057', '0.000055', '0.000056']
Solution returned: True

Brute Force and DP solutions equal: True
-----------------------------
```

## Analysis

- With four items, brute force was faster in these recorded runs. As the number of items increased, the runtimes of the brute force solver increased drastically, while the runtimes of the DP solver remained low and increased only slightly.

- In the brute force solver, each item is either selected or not selected, so there are $2^n$ subsets in total. The number of subsets grows exponentially.

- In the DP solver, it solves a subproblem for each number of items considered (from $0$ to $n$) and for each capacity (from $0$ to $C$). The $C+1$ subproblems with $0$ items are trivial, so there are $n(C+1)$ subproblems to be solved. With capacity fixed at $20$, the number of subproblems grows linearly.

- In these cases, only the number of items is growing while the capacity is fixed. Since linear growth is much slower than exponential growth, the DP solver scaled better.

- However, the DP solver is not always better since the state count also scales with the capacity. A small number of items and high capacity can make DP slower and more memory-intensive. The brute force solver has less overhead than the DP solver, so it can be more competitive for tiny inputs and with high capacity.

- Subset evaluations and DP-state calculations represent different operations, so their counts should be used to show growth patterns rather than compared as equal units of work.