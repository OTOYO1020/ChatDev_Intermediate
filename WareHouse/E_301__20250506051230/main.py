'''
Main application file for the grid candy collection game.
'''
from grid import Grid
from utils import can_reach_goal  # Importing the can_reach_goal function from utils
def main():
    # Read integers H, W, and T from standard input
    H, W, T = map(int, input().split())
    grid_input = [input().strip() for _ in range(H)]
    grid = Grid()
    grid.populate_grid(grid_input)
    result = can_reach_goal(grid.start, grid.goal, T, grid.grid)  # Call the imported function
    print(result)
if __name__ == "__main__":
    main()