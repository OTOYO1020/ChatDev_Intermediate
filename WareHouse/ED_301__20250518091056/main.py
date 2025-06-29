'''
Main application file for the Candy Collector game.
'''
import sys
from pathfinding import canReachGoal
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    max_moves = int(input_data[0])
    grid = [list(row) for row in input_data[1:]]
    H = len(grid)
    W = len(grid[0]) if H > 0 else 0
    reachable, candies_collected = canReachGoal(H, W, max_moves, grid)
    if reachable:
        print(f"Goal is reachable! Candies collected: {candies_collected}")
    else:
        print("Goal is not reachable.")
if __name__ == "__main__":
    main()