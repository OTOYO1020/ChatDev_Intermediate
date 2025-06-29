'''
Main application file for the grid meeting problem using standard input.
'''
from grid import Grid
def main():
    size = int(input())  # Read the size of the grid
    grid_data = [input() for _ in range(size)]  # Read grid configuration
    grid = Grid(size, grid_data)
    try:
        result = grid.bfs()
        print(result)  # Print the result of the BFS
    except ValueError as e:
        print(e)  # Print the error message if players are not exactly two
if __name__ == "__main__":
    main()