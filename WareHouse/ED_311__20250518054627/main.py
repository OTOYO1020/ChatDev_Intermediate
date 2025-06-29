'''
Main entry point of the application that initializes the console and handles user interactions.
'''
from grid import Grid
from utils import parse_input
def main():
    try:
        H = int(input("Enter Grid Height (H): "))
        W = int(input("Enter Grid Width (W): "))
        N = int(input("Enter Number of Holed Squares (N): "))
        holed_squares_input = input("Enter Holed Squares (x,y) separated by space: ")
        holed_squares = parse_input(holed_squares_input, N, H, W)
        grid = Grid(H, W, holed_squares)
        result = grid.count_holeless_squares()
        print(f"Total Holeless Squares: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()