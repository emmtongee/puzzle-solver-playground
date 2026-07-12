# Puzzle Solver Playground

Puzzle Solver Playground is a Python project that implements and compares algorithms for classic constraint-solving and optimization problems.

## Features

The project solves and displays the following problems while measuring algorithm performance:

### N-Queens

Given an $n \times n$ chessboard, place $n$ queens such that no two queens share the same row, column, or diagonal.

#### Algorithms used

Backtracking: Place one queen in each row. For every row, try each column and continue recursively whenever the placement does not conflict with an existing queen. If no valid placement remains, backtrack to the previous row.

## Structure

```text
puzzle-solver-playground/
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── solvers/
│   │   ├── __init__.py
│   │   └── n_queens.py
│   └── utils/
│       ├── __init__.py
│       └── display.py
└── tests/
    └── test_n_queens.py
```

## How to use

To run the N-Queens demonstration:

```bash
python -m src.main
```

To run the tests:

```bash
python -m pytest
```

## Current Progress

- [x] N-Queens backtracking solver
- [x] Board display
- [x] Search-state counter
- [x] Runtime measurement
- [x] N-Queens tests
- [ ] Sudoku backtracking solver
- [ ] Sudoku MRV heuristic
- [ ] 0/1 Knapsack brute force
- [ ] 0/1 Knapsack dynamic programming
- [ ] CLI benchmark command