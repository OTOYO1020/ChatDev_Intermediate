'''
Main entry point of the Rectangle Area Calculator application.
'''
from rectangle_area_calculator import RectangleAreaCalculator
def main():
    # Input Handling with validation
    while True:
        try:
            W = int(input("Enter Width (W): "))
            H = int(input("Enter Height (H): "))
            x = int(input("Enter X Coordinate (x): "))
            y = int(input("Enter Y Coordinate (y): "))
            if W < 0 or H < 0:
                raise ValueError("Width and Height must be non-negative.")
            break  # Exit the loop if inputs are valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid integers.")
    # Create an instance of RectangleAreaCalculator
    calculator = RectangleAreaCalculator(W, H, x, y)
    # Calculate the maximum area and check for multiple ways
    max_area, multiple_ways = calculator.calculate_area()
    # Output the Result
    print(f"{max_area} {multiple_ways}")
if __name__ == "__main__":
    main()