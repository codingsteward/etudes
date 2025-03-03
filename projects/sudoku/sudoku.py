import re
from typing import Dict, Optional

def cross(A, B) -> tuple:
    return tuple(a + b for a in A for b in B)

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

Digit = str # '1'
DigitSet = str # '123'
Square = str # e.g 'A1'
Grid = Dict[Square, DigitSet] # E.g {'A9': '123' ... }
Picture = str

squares = cross(rows, cols)

# each box is cross from abc to 123, 456, 789
all_boxes = [cross(rs, rc) for rs in ['abc', 'def', 'ghi'] for rc in ['123', '456', '789']]

all_boxes = [cross(rs, cs)  for rs in ['ABC','DEF','GHI'] for cs in ['123','456','789']]

all_cols = [cross(rows, c) for c in cols]
all_rows = [cross(r, cols) for r in rows]

all_units = all_cols + all_rows + all_boxes
print(len(all_units))

units = {s: tuple(u for u in all_units if s in u) for s in squares}

peers = {s: set().union(*units[s]) - {s} for s in squares}


def is_solution(solution: Grid, puzzle: Grid) -> bool:
    "Is this proposed solution to the puzzle actually valid?"
    return (solution is not None and
            all(solution[s] in puzzle[s] for s in squares) and
            all({solution[s] for s in unit} == set(digits) for unit in all_units))




print(all_units)
print("\n")

print(units['A1'])

print(*units['A1'])

print(len(peers['A1']))


# Implement constrain
def constrain(grid) -> Grid:
    "Propagate constraints on a copy of grid to yield a new constraint grid"
    result: Grid = {s: digits for s in squares}
    for s in grid:
        if len(grid[s]) == 1: # only has 1 possibility
            fill(result, s, grid[s])
    return result


# Implement eliminate
def fill(grid: Grid, s: Square, d: Digit) -> Optional[Grid]:
    "Eliminate all the digits except d from grid[s]"
    if grid[s] == d:
        return grid
    else:
        return None


# Implement fill
def eliminate(grid: Grid, s: Square, d: Digit) -> Optional[Grid]:
    "Eliminate d from grid[s]; implement two constraint propagation strategies"
    if d not in grid[s]:
        return grid         # Already eliminated
    grid[s] = grid[s].replace(d, '')
    if not grid[s]:
        return None         # Not legal move after eliminating
    elif grid[s] == 1:      # Square has only one possibility, eliminate on square's peers
        only_digit = grid[s]
        if not all(eliminate(grid, peer, only_digit) for peer in peers[s]):          # Not able to delete only_digit from peer
            return None





