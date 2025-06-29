'''
Main application file for the grid manipulation using standard input and output.
'''
from grid_processor import shift_outer_squares
def get_grid_input(N):
    """Function to handle grid input from the user."""
    grid = []
    print("Enter each row of the grid as space-separated integers (0 or 1):")  # Improved prompt
    for i in range(N):
        row = list(map(int, input().split()))
        if len(row) != N or any(x not in (0, 1) for x in row):
            raise ValueError("Each row must contain exactly N integers (0 or 1).")
        grid.append(row)
    return grid
def main():
    N = int(input("Enter the size of the grid (N): "))
    if N < 0:  # Ensure N is non-negative
        raise ValueError("N must be a non-negative integer.")
    if N == 0:  # Handle case when N is 0
        print("Modified Grid:")
        return  # Return an empty grid
    grid = get_grid_input(N)  # Encapsulated input handling
    modified_grid = shift_outer_squares(grid)
    print("Modified Grid:")
    for row in modified_grid:
        print(' '.join(map(str, row)))
if __name__ == "__main__":
    main()