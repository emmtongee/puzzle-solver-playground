# Sudoku Comparison Results

Each solver is called 5 times for each puzzle. The results are as follows:

```text
Sudoku Comparison
-----------------------------
Board: Easy

Naive Solver
Candidate checks: [37652, 37652, 37652, 37652, 37652]
Candidate checks deterministic: True
Runtimes in seconds: ['0.018723', '0.011678', '0.011280', '0.011257', '0.011361']
Solution returned: True
Solution valid: True

MRV Solver
Candidate checks: [11934, 11934, 11934, 11934, 11934]
Candidate checks deterministic: True
Runtimes in seconds: ['0.004983', '0.005009', '0.004977', '0.004984', '0.004981']
Solution returned: True
Solution valid: True

Naive and MRV solutions equal: True
-----------------------------
Board: Hard

Naive Solver
Candidate checks: [102444, 102444, 102444, 102444, 102444]
Candidate checks deterministic: True
Runtimes in seconds: ['0.033587', '0.033017', '0.047571', '0.032844', '0.032548']
Solution returned: True
Solution valid: True

MRV Solver
Candidate checks: [32634, 32634, 32634, 32634, 32634]
Candidate checks deterministic: True
Runtimes in seconds: ['0.014511', '0.014240', '0.014536', '0.014177', '0.014443']
Solution returned: True
Solution valid: True

Naive and MRV solutions equal: True
-----------------------------
```

## Analysis  

Candidate-check count is deterministic for this implementation and input, while runtime is affected by measurement noise and the execution environment. The MRV solver shows improvement in both candidate-check count and runtime compared to the naive solver. 

### Candidate-check results  

Using MRV solver, the candidate-check count is reduced by 25718 or 68.3% for the easy puzzle, and 69810 or 68.1% for the hard puzzle. The absolute reduction is much larger for the hard puzzle, but the percentage reduction is slightly larger for the easy puzzle.

### Runtime results  

Since runtime varies between runs, the longest and shortest runtimes are discarded. The mean of the remaining 3 runtimes is considered. These runtime values describe this set of five runs and should not be treated as a general performance guarantee. Using MRV solver, runtime is reduced by around 0.00646 seconds or 56.4% for the easy puzzle, and around 0.01875 seconds or 56.6% for the hard puzzle. Notice that runtime improvement is not proportional to candidate-check count improvement.

### Explanation  

The disproportionate runtime improvement compared to the candidate-check count improvement is consistent with the overhead caused by inspecting many empty cells during MRV selection. MRV has additional selection overhead because it calculates candidates for many empty cells before choosing the next cell, introducing extra costs such as:

- scanning empty cells;
- constructing candidate lists;
- comparing candidate-list lengths; and 
- additional loop and function-call work.

The naive solver only needs to locate the first empty cell. Therefore, reducing candidate checks does not produce an equal proportional reduction in runtime.

Despite performing more inspection at each recursive state, the MRV solver is faster in these runs. Choosing a more constrained cell can expose forced moves and dead ends earlier, reducing the number of branches explored and the amount of later backtracking.

However, the naive solver could be faster when row-major order already encounters forced or highly constrained cells, or when the puzzle needs little backtracking. In that case, MRV’s repeated inspection of all empty cells may add overhead without eliminating enough search to compensate.

### Fairness  

During the comparison, both solvers use the same:

- puzzles;
- board representation;
- clue validation;
- candidate order;
- first-solution policy;
- input-copying behaviour; and
- candidate-check definition.

The two solvers differ in their algorithms. The naive solver selects the first empty cell in row-major order, while the MRV solver selects the empty cell with the fewest legal candidates. Note that MRV’s candidate-check count includes the validity checks used to inspect cells during MRV selection.