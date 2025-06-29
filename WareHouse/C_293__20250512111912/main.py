'''
Main application file for counting distinct paths in a grid.
'''
from typing import List
from path_counter import count_happy_paths
def main():
    try:
        H = int(input("Enter Height (H): "))
        W = int(input("Enter Width (W): "))
        print("Enter Grid values (comma-separated rows):")
        grid = []
        for _ in range(H):
            row_input = input()
            grid_row = list(map(int, row_input.split(',')))
            if len(grid_row) != W:
                raise ValueError("Row does not match the specified width.")
            grid.append(grid_row)
        result = count_happy_paths(H, W, grid)
        print(f"Distinct Paths: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()