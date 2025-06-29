'''
Main application file for the square side length calculator.
'''
from calculator import min_square_side
def main():
    # Input parsing
    N = int(input("Enter the number of points (N): "))
    K = int(input("Enter the maximum operations (K): "))
    points_input = input("Enter the points (comma-separated x,y): ")
    points = []
    for point in points_input.split(','):
        coords = point.strip().split(',')
        if len(coords) != 2:
            raise ValueError(f"Invalid point format: {point}. Each point must be in the format x,y.")
        x, y = map(int, coords)
        points.append((x, y))
    if len(points) != N:
        raise ValueError("Number of points does not match N.")
    result = min_square_side(N, K, points)
    print(f"Minimum Side Length: {result}")
if __name__ == "__main__":
    main()