# Puzzle Solver Playground

Puzzle Solver Playground is a Python project that implements and compares algorithms for classic constraint-solving and optimization problems.

## Features

The project solves and displays the following problems while measuring algorithm performance:

### N-Queens

Given an $n \times n$ chessboard, place $n$ queens such that no two queens share the same row, column, or diagonal.

#### Algorithms used

Backtracking: Place one queen in each row. For every row, try each column and continue recursively whenever the placement does not conflict with an existing queen. If no valid placement remains, backtrack to the previous row.

### Sudoku

On a $9 \times 9$ board divided into 9 $3 \times 3$ boxes, some integers from 1 to 9 are filled in some cells. Fill in the rest of the cells with integers from 1 to 9 such that no two same numbers share the same row, column or box.

#### Algorithms used

Backtracking: Starting from the top left corner, for every cell from top to bottom, then from left to right, try putting an integer from 1 to 9 and continue recursively whenever the cell does not conflict with other cells. If no valid numbers exist for this cell, backtrack to the previous cell.

## Structure

```text
puzzle-solver-playground/
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── solvers/
│   │   ├── __init__.py
│   │   ├── n_queens.py
│   │   └── sudoku.py
│   └── utils/
│       ├── __init__.py
│       └── display.py
├── tests/
│   ├── test_display.py
│   ├── test_n_queens.py
│   ├── test_sudoku_parser.py
│   ├── test_sudoku_validation.py
│   └── test_sudoku_solver.py
└── examples/
    ├── sudoku_easy.txt
    └── sudoku_hard.txt
```

## How to use

To run the demonstration:

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