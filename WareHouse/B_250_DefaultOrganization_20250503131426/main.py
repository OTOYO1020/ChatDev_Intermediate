'''
Main entry point for the grid generation application.
'''
from grid_generator import GridGenerator
def main():
    try:
        N = int(input("Enter N: "))
        A = int(input("Enter A: "))
        B = int(input("Enter B: "))
        grid_gen = GridGenerator(N, A, B)
        grid = grid_gen.create_grid()
        display_grid(grid)
    except ValueError:
        print("Please enter valid integers for N, A, and B.")
def display_grid(grid):
    '''
    Displays the grid in a formatted manner.
    Parameters:
    grid (list): A 2D list representing the grid to be displayed.
    '''
    for row in grid:
        print(' '.join(row))  # Add a space between each tile for clarity
if __name__ == "__main__":
    main()