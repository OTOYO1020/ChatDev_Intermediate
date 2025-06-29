'''
Main application file for the Lattice Point Counter.
'''
import sys
from lattice_functions import manhattan_distance, is_lattice_point, count_lattice_points
def main():
    try:
        # Read input from standard input
        input_data = sys.stdin.read().strip().splitlines()
        p = list(map(int, input_data[0].split(',')))
        q = list(map(int, input_data[1].split(',')))
        D = int(input_data[2])
        # Validate dimensionality of points
        if len(p) != len(q):
            print("Input Error: Points p and q must have the same dimensionality.")
            return
        # Validate that all coordinates are integers
        if not all(isinstance(coord, int) for coord in p + q):
            print("Input Error: All coordinates of points p and q must be integers.")
            return
        # Validate that dimensions are greater than zero
        if len(p) == 0 or len(q) == 0:
            print("Input Error: Points must have at least one dimension.")
            return
        # Validate that D is a non-negative integer
        if D < 0:
            print("Input Error: Distance D must be a non-negative integer.")
            return
        # Calculate the number of valid lattice points
        count = count_lattice_points(p, q, D)
        # Output the result
        print(f"Number of valid lattice points: {count}")
    except ValueError:
        print("Input Error: Please enter valid integers for points and distance.")
if __name__ == "__main__":
    main()