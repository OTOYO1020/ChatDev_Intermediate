'''
Main application file for the connected red paintings counter.
'''
from utils import count_connected_red_paintings
def main():
    try:
        n = int(input("Enter grid size (N): "))
        k = int(input("Enter number of squares to paint (K): "))
        print("Enter the grid (use '.' for white squares and '#' for others, one row per line):")
        grid_input = [input().strip() for _ in range(n)]
        # Validate grid size
        if len(grid_input) != n or any(len(row) != n for row in grid_input):
            print("Error: Grid must be of size N x N.")
            return
        # Validate grid content
        if any(char not in {'.', '#'} for row in grid_input for char in row):
            print("Error: Grid can only contain '.' for white squares and '#' for others.")
            return
        result = count_connected_red_paintings(n, k, grid_input)
        if isinstance(result, str):  # Check if result is an error message
            print(result)
        else:
            print(f"Valid combinations: {result}")
    except ValueError:
        print("Error: Please enter valid integers for N and K.")
if __name__ == "__main__":
    main()