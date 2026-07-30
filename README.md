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

## How to use

To run the demonstration:

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

The raw measurements and analysis are available in [benchmarks/sudoku_results.md](benchmarks/sudoku_results.md).

## Current Progress

### N-Queens

- [x] Backtracking solver
- [x] Board display
- [x] Search-state counter
- [x] Runtime measurement
- [x] Tests

### Sudoku

- [x] Parsing and validation
- [x] Naive backtracking solver
- [x] MRV backtracking solver
- [x] Candidate-check and runtime comparison
- [x] Tests

### Planned

- [ ] 0/1 Knapsack brute force
- [ ] 0/1 Knapsack dynamic programming
- [ ] CLI benchmark command