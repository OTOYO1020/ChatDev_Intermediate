'''
Main application file for the Rectangle Area Calculator.
This application reads the dimensions of a rectangle and a point within it,
calculates the areas of the sections formed by cutting the rectangle through the point,
and displays the maximum area of the smaller part along with whether there are multiple ways to achieve that area.
'''
import sys
from utils import calculate_areas
if __name__ == "__main__":
    try:
        while True:
            try:
                W = int(input("Enter Width (W) [positive integer]: "))
                if W <= 0:
                    raise ValueError("Width (W) must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input for Width (W): {e}. Please enter a positive integer.")
        while True:
            try:
                H = int(input("Enter Height (H) [positive integer]: "))
                if H <= 0:
                    raise ValueError("Height (H) must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input for Height (H): {e}. Please enter a positive integer.")
        # Loop for x coordinate input
        attempts = 3  # Maximum attempts for input
        for attempt in range(attempts):
            try:
                print(f"Valid range for X: 0 to {W} (inclusive)")
                x = int(input("Enter X Coordinate: "))
                if 0 <= x <= W:
                    break
                else:
                    print(f"X must be between 0 and {W}. Please try again.")
            except ValueError:
                print("Invalid input for X Coordinate. Please enter an integer.")
            if attempt == attempts - 1:
                print("Maximum attempts reached. Exiting the program.")
                sys.exit(1)
        # Loop for y coordinate input
        for attempt in range(attempts):
            try:
                print(f"Valid range for Y: 0 to {H} (inclusive)")
                y = int(input("Enter Y Coordinate: "))
                if 0 <= y <= H:
                    break
                else:
                    print(f"Y must be between 0 and {H}. Please try again.")
            except ValueError:
                print("Invalid input for Y Coordinate. Please enter an integer.")
            if attempt == attempts - 1:
                print("Maximum attempts reached. Exiting the program.")
                sys.exit(1)
        max_part_area, multiple_ways = calculate_areas(W, H, x, y)
        print(f"Max Area of Smaller Part: {max_part_area}")
        print(f"Multiple Ways: {'Yes' if multiple_ways else 'No'}")
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)