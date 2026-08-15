# Week 5 Refactor Checklist

## Session 1 Baseline

- Application command: `python3 -m src.main`
- Full test command: `python3 -m pytest`
- Baseline result: 69 passed in 0.09s
- Code modified during inspection: No
- Temporary package-file changes restored: Yes

## 1

**Status:** Rejected

**Rejected change:** Delete `src/__init__.py` and `src/solvers/__init__.py`.  

**Evidence:** Imports, `python3 -m src.main`, and test discovery work without them.  

**Reason for rejection:** Their presence clearly marks `src` and `src.solvers` as packages, while deleting them provides no meaningful maintenance benefit.

## 2

**Status:** Deferred

**Deferred improvement:** Consider adding a Knapsack demonstration to `src/main.py` in a future usability or integration milestone.  

**Reason for rejection:** It expands behavior and is unrelated to the Week 5 structural refactor.

## 3

**Status:** Completed

**Problem:** Solver functions and their supporting functions communicate accepted and returned data types only through docstrings and usage. This makes interfaces harder to inspect and maintain.  

**Exact change:** Add parameter and return type hints to the listed functions. Where a complicated repeated type occurs, use a narrowly named type alias only if it clearly improves readability. Do not change parameters, return values, data representation, validation, or runtime behavior.  

**Affected functions:**
- `solve_n_queens`
- `n_queens_is_safe`
- `solve_sudoku`
- `mrv_solve_sudoku`
- `read_sudoku_file`
- `parse_sudoku`
- `sudoku_is_safe`
- `sudoku_board_is_valid`
- `sudoku_get_cell_candidates`
- `sudoku_select_mrv_cell`
- `solve_knapsack`
- `dynamic_solve_knapsack`
- `knapsack_problem_is_valid`
- `number_power_set`  

**Affected files:**
- `src/solvers/n_queens.py`
- `src/solvers/sudoku.py`
- `src/solvers/knapsack.py`

**Protected behavior:** Public call forms, returned values, deterministic choices, validation, metrics, exceptions, failure behavior, and input preservation remain unchanged.  

**Relevant checks:** Full test suite and final signature inspection. Do not add a type-checking dependency during this refactor.

## 4A

**Status:** Completed

**Problem:** In `number_power_set`, the relationship between recursion order and deterministic subset order is not immediately clear.  

**Exact change:** Add a concise explanation of why the exclude-first and include-second recursive calls produce the required order. Improve local names only where doing so makes the recursion easier to follow. Do not redesign the recursion.  

**Affected file:** `src/solvers/knapsack.py`  

**Protected behavior:** Generated subsets and their order remain identical.  

**Relevant tests:** Knapsack brute-force correctness, tie-breaking, metrics, and cross-solver tests; final diff review.

## 4B

**Status:** Completed

**Problem:** In `dynamic_solve_knapsack`, numeric tuple indexing obscures the current item’s weight and value, and the connection between the two previous table cells and the include/exclude transition is difficult to follow.  

**Exact change:** Unpack the current item into clearly named local variables. Add one concise explanation of the include/exclude DP transition. Preserve the existing tie-breaking comment and behavior. Do not change the DP table representation unless a separate demonstrated need appears.  

**Affected file:** `src/solvers/knapsack.py`  

**Protected behavior:** Optimal value, selected-index set, deterministic tie-breaking, calculated-state metric, validation, and input preservation remain identical.  

**Relevant tests:** All Knapsack tests, especially cross-solver, tie-breaking, metrics, validation, and input-preservation tests; final diff review.

## 5A

**Status:** Completed

**Problem:** Six Sudoku behaviors are tested separately for the row-major and MRV solvers even though their setup and expected contract are the same. 

**Exact change:** Parameterize the duplicated behavior tests over `solve_sudoku` and `mrv_solve_sudoku`. Preserve separate tests wherever solver-specific metrics or implementation-specific expectations differ. Give parameter cases readable IDs so failures identify both the solver and scenario.  

**Affected file:** `tests/test_sudoku_solver.py` 

**Affected scenarios:**

- contradictory board
- one empty cell
- unsolvable board
- already complete board
- easy board
- hard board  

**Protected behavior:** Both solvers continue to run independently against every shared contract. A failure must still identify the solver and scenario clearly.  

**Relevant checks:** Run the Sudoku solver test file, inspect collected parameterized test names, and then run the full suite. 

**Rejected scope:** Do not build a shared testing framework across Sudoku and Knapsack. Do not consolidate solver-specific metric tests.

## 5B

**Status:** Completed

**Problem**: Seven Knapsack contract tests are duplicated for the brute-force and dynamic-programming solvers. The paired tests use the same inputs and assertions but call different solver functions.

**Exact change**: Parameterize the shared tests over solve_knapsack and dynamic_solve_knapsack, using readable IDs brute-force and dynamic-programming.

**Affected file**: tests/test_knapsack.py

**Affected scenarios**:

- no fitting items
- deterministic tie-breaking
- duplicate items
- zero-weight items
- zero-value items
- zero capacity
- negative input

**Protected behavior**: Both solvers remain independently checked for the same returned value and selected-index set, validation behavior, and applicable edge cases.

**Relevant checks**: Inspect collected Knapsack test names, run tests/test_knapsack.py, and then run the full suite.

**Rejected scope**: Keep metric-specific assertions separate because the solvers measure different work. Do not create a generic test framework shared by Knapsack and Sudoku.

## 6

**Status:** Completed

**Problem:** `sudoku_is_safe` uses the descriptive name `current_row` for column scanning but the generic name `i` for row scanning.  

**Exact change:** Rename `i` to `current_col` in the row-conflict loop only.  

**Affected file:** `src/solvers/sudoku.py`  

**Protected behavior:** Sudoku conflict detection remains unchanged.  

**Relevant tests:** `tests/test_sudoku_validation.py` and the full test suite.

---

## Session 2 Verification

- Targeted tests: Passed
- Parameterized test collection: Reviewed; all intended scenarios run for both relevant solvers
- Full test suite: 69 passed in 0.11s
- Application command: `python3 -m src.main` passed
- Pylance errors in affected files: None
- Final diff: Reviewed; all changes map to approved checklist items
- Behavior changes: None

---

## Final Analysis

**Before:**

- solver interfaces lacked type hints
- two Knapsack sections obscured important reasoning
- shared solver-contract tests were duplicates
- one Sudoku loop used inconsistent naming

**Change:**

- added type hints to solver and supporting functions
- clarified power-set ordering and Knapsack DP transition
- parameterized shared Sudoku and Knapsack contract tests
- renamed Sudoku column-loop variable

**Safety:**

- all targeted tests passed
- full suite passed with 69 tests
- `python3 -m src.main` ran successfully
- Pylance reported no errors
- outputs, validation, metrics, tie-breaking, failure behavior, and input preservation remain unchanged

**Result:** Function contracts, recursive ordering, DP transitions, and shared test coverage are now easier to understand and maintain.

**Rejected scope:**

Did not:
- delete package files
- add a Knapsack demonstration
- insert broad explanatory comments
- create a generic testing framework
- add a type-checking dependency