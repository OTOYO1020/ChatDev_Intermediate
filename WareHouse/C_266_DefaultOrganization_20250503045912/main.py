'''
Main application file for checking the convexity of a quadrilateral.
'''
import sys
import re
from convexity import is_convex
# Define a constant for coordinate range
COORDINATE_RANGE = (-10000, 10000)
def is_valid_coordinate(coord):
    return isinstance(coord, int) and COORDINATE_RANGE[0] <= coord <= COORDINATE_RANGE[1]
def main():
    '''
    Main function to read input and check the convexity of a quadrilateral.
    '''
    while True:
        try:
            # Prompt user for input with clear instructions
            coords_input = input("Enter coordinates as Ax, Ay, Bx, By, Cx, Cy, Dx, Dy (comma-separated): ").strip()
            if not coords_input:
                raise ValueError("Input cannot be empty.")
            # Validate input format using regex
            if not re.match(r'^-?\d+,-?\d+,-?\d+,-?\d+,-?\d+,-?\d+,-?\d+,-?\d+$', coords_input):
                raise ValueError("Input must be 8 integers separated by commas.")
            # Split by commas and strip spaces from each coordinate
            coords_list = [coord.strip() for coord in coords_input.split(',')]
            valid_coords = []
            for coord in coords_list:
                try:
                    value = int(coord)
                    if not is_valid_coordinate(value):
                        raise ValueError(f"Coordinate {value} is out of range.")
                    valid_coords.append(value)
                except ValueError:
                    raise ValueError(f"Coordinate '{coord}' is not a valid integer.")
            vertices = [(valid_coords[i], valid_coords[i + 1]) for i in range(0, 8, 2)]
            result = is_convex(vertices)
            print(result)
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Input Error: {e}. Please ensure you enter 8 integers within the range of -10,000 to 10,000, separated by commas.")
        except Exception as e:
            print(f"Unexpected Error: {e}")
if __name__ == "__main__":
    main()