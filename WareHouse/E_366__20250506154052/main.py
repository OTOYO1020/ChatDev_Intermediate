'''
Main application file for the point distance calculator.
'''
import sys
from calculator import calculate_valid_pairs
from collections import Counter
def get_input():
    while True:
        try:
            n = int(input("Enter number of points (N): "))
            if n <= 0:
                print("N must be a positive integer. Please try again.")
                continue
            d = int(input("Enter non-negative distance (D): "))
            if d < 0:
                print("D must be a non-negative integer. Please try again.")
                continue
            return n, d
        except ValueError:
            print("Invalid input. Please enter integers for N and D.")
def main():
    try:
        n, d = get_input()  # Use the new input function
        points = []  # Use a list to store points
        # Read points from standard input
        for i in range(n):
            while True:
                point_input = input(f"Enter point {i + 1} (x,y): ")
                coords = point_input.split(',')
                if len(coords) != 2:
                    print(f"Invalid point format: {point_input}. Each point must be in the format 'x,y'. Please try again.")
                    continue
                try:
                    x, y = map(int, coords)
                    # Check for reasonable bounds
                    if not (-10**6 <= x <= 10**6 and -10**6 <= y <= 10**6):
                        print(f"Coordinates out of bounds: ({x}, {y}). Please enter values between -10^6 and 10^6.")
                        continue
                    points.append((x, y))  # Append point to the list
                    break  # Exit the loop if input is valid
                except ValueError:
                    print(f"Invalid coordinates: {point_input}. Coordinates must be integers. Please try again.")
        # Count the frequency of each point
        point_counts = Counter(points)
        count = calculate_valid_pairs(point_counts, d)  # Pass the frequency dictionary
        print(f"Valid integer pairs count: {count}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()