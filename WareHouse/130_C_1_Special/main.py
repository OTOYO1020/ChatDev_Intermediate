'''
Main function to handle input and output for the rectangle area calculation.
'''
import sys
from rectangle_area_calculator import RectangleAreaCalculator
def main():
    '''
    Main function to handle input and output for the rectangle area calculation.
    '''
    try:
        # Input Handling: Read integers W, H, x, and y from standard input
        W, H, x, y = map(int, sys.stdin.readline().strip().split())
        # Validate dimensions
        if W <= 0 or H <= 0:
            print("Width and height must be positive integers.")
            return
        # Validate coordinates
        if not (0 <= x <= W and 0 <= y <= H):
            print("Coordinates must be within the rectangle dimensions.")
            return
        # Create an instance of RectangleAreaCalculator
        calculator = RectangleAreaCalculator(W, H, x, y)
        # Calculate Maximum Possible Area
        max_area = calculator.calculate_max_possible_area()
        # Check for Multiple Ways
        multiple_ways = calculator.check_multiple_ways()
        # Output the Result
        print(f"{max_area} {1 if multiple_ways else 0}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()