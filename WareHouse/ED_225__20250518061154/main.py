'''
Main application file for the visible sevens calculator.
'''
from typing import List, Tuple  # Importing List and Tuple for type annotations
from computation import max_visible_sevens
def main():
    try:
        N = int(input("Enter number of 7's: "))
        coordinates_input = input("Enter coordinates (x,y) separated by semicolons: ")
        # Correctly parse coordinates separated by semicolons
        coordinates = [tuple(map(int, coord.split(','))) for coord in coordinates_input.split(';')]
        if len(coordinates) != N:
            raise ValueError(f"Expected {N} coordinates, but got {len(coordinates)}.")
        max_visible = max_visible_sevens(N, coordinates)
        print(f"Maximum visible 7's: {max_visible}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
if __name__ == "__main__":
    main()