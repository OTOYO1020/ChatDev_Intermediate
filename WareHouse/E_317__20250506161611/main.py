'''
Main entry point for the grid navigation application.
'''
from grid import Grid
def main():
    # Read dimensions of the grid
    H, W = map(int, input().split())
    # Read the grid representation
    grid_data = [list(input().strip()) for _ in range(H)]
    # Create the grid object
    grid = Grid(H, W, grid_data)
    # Perform BFS to find the minimum moves
    moves = grid.bfs()
    # Print the result
    if moves != -1:
        print(f"Minimum moves: {moves}")
    else:
        print("Goal is unreachable.")
if __name__ == "__main__":
    main()