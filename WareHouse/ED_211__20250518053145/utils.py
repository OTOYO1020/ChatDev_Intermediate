'''
Utility functions for counting combinations and connectivity checks.
'''
from itertools import combinations
from grid import Grid
def count_connected_red_paintings(N, K, S):
    '''Counts the number of valid combinations of K connected red paintings.'''
    if K == 0:
        return 1  # One way to choose zero squares
    grid = Grid(N, S)
    white_squares = grid.get_white_squares()
    if K > len(white_squares):
        return f"Error: Not enough white squares to paint {K} squares."
    count = 0
    for combo in combinations(white_squares, K):
        if grid.is_connected(combo):
            count += 1
    return count