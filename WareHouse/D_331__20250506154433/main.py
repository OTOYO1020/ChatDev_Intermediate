'''
Main application file for the color grid counting application.
'''
import sys
from grid import Grid
from query import Query
def main():
    # Read the size of the grid
    N = int(input("Enter grid size (N): "))
    # Initialize the grid
    colors = []
    print("Enter grid colors (B/W) for each cell in row-major order:")
    for _ in range(N):
        while True:
            row_colors = input().strip().split()
            if len(row_colors) != N or any(color not in ['B', 'W'] for color in row_colors):
                print(f"Invalid input. Please enter exactly {N} colors (B/W) for the row.")
            else:
                colors.append(row_colors)
                break
    grid = Grid(N, colors)
    # Read the number of queries
    Q = int(input("Enter number of queries (Q): "))
    results = []
    for _ in range(Q):
        while True:
            try:
                A, B, C, D = map(int, input("Enter query (A B C D): ").strip().split())
                # Adjusted validation to ensure A, B, C, D are within 1 to N
                if A < 1 or B < 1 or C < 1 or D < 1 or A > N or B > N or C > N or D > N or A > C or B > D:
                    print("Invalid query. Please ensure A, B, C, D are within the grid size (1 to N) and A <= C, B <= D.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter four integers for the query.")
        # Adjust indices for 0-based indexing before passing to count_black_squares
        query = Query(A, B, C, D)
        black_count = grid.count_black_squares(query)
        results.append(black_count)
    # Print the results for each query
    for result in results:
        print(result)
if __name__ == "__main__":
    main()