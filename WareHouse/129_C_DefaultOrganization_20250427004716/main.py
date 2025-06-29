'''
Main application file for the grid lighting application.
'''
from grid_logic import GridLogic
def main():
    try:
        # Input Handling
        dimensions = input("Enter grid dimensions (H W): ").split()
        try:
            H = int(dimensions[0])
            W = int(dimensions[1])
            if H <= 0 or W <= 0:
                raise ValueError("Grid dimensions must be positive integers.")
        except ValueError:
            print("Error: Please enter valid positive integers for H and W.")
            return  # Exit the program if input is invalid
        grid = []
        for i in range(H):
            row = input(f"Enter row {i + 1} of the grid layout: ").strip()  # Strip whitespace
            if len(row) != W:
                raise ValueError(f"Row {i + 1} must be exactly {W} characters long.")
            grid.append(row)
        # New validation step for grid characters
        for row in grid:
            if any(char not in ['#', '.'] for char in row):
                raise ValueError("Grid can only contain '#' for obstacles and '.' for empty squares.")
        grid_logic = GridLogic(grid)
        max_lighted = grid_logic.get_max_lighted()
        print(f"Max Lighted Squares: {max_lighted}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()