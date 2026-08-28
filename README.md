# Puzzle Solver Playground

Puzzle Solver Playground is a Python project that implements and compares algorithms for classic constraint-solving and optimization problems.

## Features

The project solves and displays the following problems while measuring algorithm performance:

### N-Queens

Given an $n \times n$ chessboard, place $n$ queens such that no two queens share the same row, column, or diagonal.

#### Algorithms used

**Backtracking**: Place one queen in each row. For every row, try each column and continue recursively whenever the placement does not conflict with an existing queen. If no valid placement remains, backtrack to the previous row.

### Sudoku

On a $9 \times 9$ board divided into 9 $3 \times 3$ boxes, some integers from 1 to 9 are filled in some cells. Fill the remaining cells so that each row, column, and 3 × 3 box contains every integer from 1 to 9 exactly once.

#### Algorithms used

**Naive backtracking:** Select the first empty cell in row-major order. Try candidate values from 1 to 9 and continue recursively whenever a placement is valid. If no candidate leads to a solution, backtrack to the previous decision.

**Minimum Remaining Values backtracking:** Select the empty cell with the fewest legal candidates. Ties are resolved in row-major order. Try the candidates in ascending order and backtrack when a candidate does not lead to a solution.

### 0/1 Knapsack

Given $n$ items, each with weight $w_i$ and value $v_i$, and a knapsack with capacity $c$, where $n, w_i, v_i, c$ are non-negative integers. Each item may either be selected once or not selected. Find a combination of items whose total weight does not exceed the capacity and whose total value is maximized.

#### Algorithm used

**Brute force**: Examine every possible combination and select the one with the maximum total value that does not exceed the capacity.

**Bottom-up dynamic programming**: Solve smaller subproblems defined by the number of available items and the knapsack capacity. Store their optimal results in a table, then use those results to build solutions for larger subproblems until the original problem is solved.

## Requirements

This project requires Python 3 and has been tested with Python 3.13.7.
The solvers use only the Python standard library and have no third-party runtime dependencies.
`pytest` is required to run the test suite.

## Setup

A virtual environment is recommended.

1. Create a virtual environment:

```bash
python3 -m venv .venv
```

2. Activate the virtual environment:

- Windows Command Prompt

```bash
.venv\Scripts\activate.bat
```

- Windows PowerShell

```bash
.venv\Scripts\Activate.ps1
```

- macOS and Linux

```bash
source .venv/bin/activate
```

3. Install pytest (if you want to run the tests):

```bash
python3 -m pip install pytest
```

## Usage

The commands listed here should be run from the repository root.

To launch the interactive CLI:

```bash
python3 -m src.main
```

To run the tests:

```bash
python3 -m pytest
```

To compare the naive and MRV Sudoku solvers:

```bash
python3 -m benchmarks.sudoku_comparison
```

To compare the brute-force and dynamic-programming Knapsack solvers:

```bash
python3 -m benchmarks.knapsack_comparison
```

The raw measurements and analysis are available in [benchmarks/sudoku_results.md](benchmarks/sudoku_results.md) and [benchmarks/knapsack_results.md](benchmarks/knapsack_results.md).

### Sample Output

The following is representative output from the Knapsack demonstration. Runtime varies by machine and between runs.

```text
1. N-Queens
2. Sudoku
3. Knapsack
4. Exit
Choose one: 3
-----------------------------
Items: [(3, 4), (2, 3), (1, 1)]
Capacity: 5
Maximum value: 7
Selected items:
Item 1: weight 3, value 4
Item 2: weight 2, value 3
States calculated: 18
-----------------------------
1. N-Queens
2. Sudoku
3. Knapsack
4. Exit
Choose one: 4
```

## Project Status

Puzzle Solver Playground currently includes:

- interactive CLI demonstrations for N-Queens, Sudoku, and 0/1 Knapsack;
- multiple algorithms for comparing approaches to Sudoku and Knapsack;
- input parsing and validation for Sudoku;
- board and solution display utilities;
- search-state and runtime measurements;
- benchmark measurements and analysis for Sudoku and Knapsack; and
- 69 automated tests covering solver behavior, validation, parsing, and display.

All three solver demonstrations are accessible through `python3 -m src.main`.

## Future Improvements

Possible future extensions include:

- adding more puzzles and solving algorithms;
- allowing users to enter and play selected puzzles;
- generating puzzles;
- adding a GUI for puzzle interaction;
- visualizing the algorithms on a small scale;
- exploring graph coloring or local search.