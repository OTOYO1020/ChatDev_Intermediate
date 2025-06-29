'''
Main application file for the grid game.
'''
import sys
from game_logic import minimum_moves
def main():
    try:
        N = int(input("Enter grid size (N): "))
        print("Enter grid (each row as a string):")
        grid = [input().strip() for _ in range(N)]
        if len(grid) != N:
            raise ValueError("Grid size does not match the number of rows provided.")
        # Validate grid contents
        for row in grid:
            if any(c not in ['.', '1', '2'] for c in row):
                raise ValueError("Grid contains invalid characters. Only '.', '1', and '2' are allowed.")
        result = minimum_moves(N, grid)
        print(f"Minimum Moves: {result}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()