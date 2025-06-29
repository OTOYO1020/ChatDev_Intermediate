'''
Main application file for the distance calculator.
'''
import re
from distance_calculator import DistanceCalculator
def main():
    try:
        # Read the number of dimensions
        N = int(input())
        # Read the coordinates
        coordinates_input = input()
        # Split by either spaces or commas, and convert to integers
        coordinates = list(map(int, (x.strip() for x in re.split(r'[,\s]+', coordinates_input) if x)))
        if len(coordinates) != N:
            raise ValueError(f"Expected {N} coordinates, but got {len(coordinates)}. Please ensure you enter exactly {N} integers.")
        distance_calculator = DistanceCalculator(coordinates)
        manhattan, euclidean, chebyshev = distance_calculator.calculate_distances()
        # Print the calculated distances
        print(manhattan)
        print(f"{euclidean:.2f}")
        print(chebyshev)
    except ValueError as e:
        print(f"Invalid input: {e}. Please ensure you enter integers in the correct format.")
if __name__ == "__main__":
    main()