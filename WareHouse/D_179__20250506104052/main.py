'''
Main application file for the segment calculator.
'''
import sys
from calculator import calculate_ways
def main():
    # Read integers N and K from standard input
    try:
        N, K = map(int, sys.stdin.readline().strip().split())
    except ValueError:
        print("Error: Please enter valid integers for N and K.")
        return
    if N < 1:
        print("Error: N must be at least 1.")
        return
    if K < 1:
        print("Error: K must be at least 1 to define segments.")
        return
    segments = []
    # For each segment from 1 to K, read the values L_i and R_i
    for _ in range(K):
        try:
            L, R = map(int, sys.stdin.readline().strip().split())
        except ValueError:
            print("Error: Please enter valid integers for segment endpoints L and R.")
            return
        if L < 1 or R < 1 or L > N or R > N:
            print(f"Error: Segment ({L}, {R}) is out of bounds for N={N}.")
            return
        segments.append((L, R))
    # Sort segments to ensure they are processed in order
    segments.sort()
    # Check for non-intersecting condition
    for i in range(1, len(segments)):
        if segments[i][0] < segments[i-1][1]:  # Change to strictly less than
            print(f"Error: Segment {segments[i]} intersects with previous segment {segments[i-1]}.")
            return
    # Calculate the number of ways to reach cell N
    result = calculate_ways(N, K, segments)
    # Print the result
    print(result)
if __name__ == "__main__":
    main()