'''
Main application file for the cell color viewer.
'''
from grid import Grid
def get_valid_input():
    """Prompt the user for valid row and column inputs."""
    while True:
        try:
            R = int(input("Enter Row (1-15): "))
            C = int(input("Enter Column (1-15): "))
            if 1 <= R <= 15 and 1 <= C <= 15:
                return R, C
            else:
                print("Row and Column must be between 1 and 15. Please try again.")
        except ValueError:
            print("Please enter valid integers.")
def main():
    grid = Grid()
    R, C = get_valid_input()  # Get valid inputs from the user
    cell_color = grid.get_color(R - 1, C - 1)  # Access the cell color
    print(f"Cell Color: {cell_color}")  # Print the cell color
if __name__ == "__main__":
    main()