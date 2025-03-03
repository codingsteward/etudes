# Sudoku

Implementing Norvig's sudoku for practise purpose

What ideas are important to take away?


## Constraint propagation

If a square has only one possible digit, eliminate that digit as a possibility for each of the square's peers.

If a unit only has one possible square to hold a digit,    fill that square up with the digit.

This suggests we need two functions:
1. eliminate(grid, s, d) # eliminates digit d as a possibility for square s
2. fill(grid, s, d) # fill square s with digit d

Constraint: constrain what values can go in
Propagation: a fill of one square leads to elimination of other squares which in turn can cause a fill and so on..


