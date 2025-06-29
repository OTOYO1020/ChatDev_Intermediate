'''
Main application file for the integer pairs counting application.
'''
from counting import count_integer_pairs
def main():
    try:
        # Read input values
        N = int(input("Number of Points (N): "))
        D = int(input("Distance Threshold (D): "))
        print(f"Please enter at least {N} unique points in the format 'x,y' separated by commas.")
        points_input = input("Enter Points (x,y) separated by commas: ")
        # Initialize a set to track unique points
        points_set = set()
        for point in points_input.split(','):
            coords = point.strip().split(',')
            if len(coords) != 2:
                raise ValueError(f"Invalid point format: '{point}'. Each point must be in the format 'x,y'.")
            x, y = map(int, coords)
            points_set.add((x, y))  # Add to set to ensure uniqueness
        points = list(points_set)  # Convert back to list
        # Inform the user about the number of unique points
        print(f"Number of unique points provided: {len(points)}")
        # Validate the number of unique points
        if len(points) < N:
            raise ValueError(f"Not enough unique points provided. Expected at least N ({N}), but got {len(points)}.")
        count = count_integer_pairs(len(points), D, points)
        print(f"Valid pairs: {count}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()