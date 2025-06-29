'''
Main application file for the grid navigation program using BFS.
'''
import sys
from typing import List, Tuple
from grid_input import GridInput
from bfs import canReachGoal
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    grid_data = []
    medicines_data = []
    # Parse input data
    for line in input_data:
        if line.startswith("GRID:"):
            grid_data = line[6:].strip().split(';')
        elif line.startswith("MEDICINES:"):
            medicines_data = line[11:].strip().split(';')
    grid_input = GridInput(grid_data, medicines_data)
    grid = grid_input.get_grid()
    medicines = grid_input.get_medicines()
    if grid is not None:
        start = grid_input.get_start()
        goal = grid_input.get_goal()
        if canReachGoal(len(grid), len(grid[0]), grid, medicines, start, goal):
            print("YES")
        else:
            print("NO")
    else:
        print("Invalid grid input.")
if __name__ == "__main__":
    main()