'''
Main application file to run the program for selecting combinations of white squares.
'''
import sys
from grid import Grid
from combination import Combination
def main():
    try:
        N = int(input("Enter grid size (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        K = int(input("Enter number of squares to select (K): "))
        if K <= 0 or K > N * N:
            raise ValueError("K must be a positive integer and less than or equal to N*N.")
        grid_input = []
        print("Enter grid (use '.' for white and '#' for black):")
        for _ in range(N):
            row = input().strip()
            if len(row) != N or any(char not in ['#', '.'] for char in row):
                raise ValueError("Each row must be of length N and contain only '#' and '.' characters.")
            grid_input.append(row)
        grid = Grid(N, grid_input)
        # New validation check for not enough white squares
        if len(grid.white_squares) < K:
            print("Not enough white squares to form combinations of the specified size.", file=sys.stderr)
            return  # Exit the program gracefully
        # Check for no white squares
        if not grid.white_squares:
            print("No white squares available in the grid.", file=sys.stderr)
            return  # Exit the program gracefully
        combination = Combination(grid)
        valid_count = combination.count_valid_combinations(K)
        print(f"Number of valid combinations: {valid_count}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()