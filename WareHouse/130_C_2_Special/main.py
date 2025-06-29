'''
This module initializes the application for calculating the maximum area of a rectangle
based on user input.
'''
from rectangle_area_calculator import RectangleAreaCalculator
def main():
    '''Main function to run the rectangle area calculator.'''
    try:
        # Input Handling
        W, H, x, y = map(int, input("Enter width, height, x, and y separated by spaces: ").split())
        # Input validation for width and height
        if W <= 0 or H <= 0:
            print("Width and Height must be positive integers.")
            return
        # Input validation for coordinates
        if not (0 <= x <= W and 0 <= y <= H):
            print("Coordinates (x, y) must be within the rectangle defined by width and height, including edges.")
            return
        calculator = RectangleAreaCalculator(W, H)
        # Calculate maximum area
        max_area = calculator.calculate_max_area()
        # Check for multiple ways
        multiple_ways = calculator.check_multiple_ways(x, y)
        # Output the result
        print(f"{max_area} {1 if multiple_ways else 0}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()