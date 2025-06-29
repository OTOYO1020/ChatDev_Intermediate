'''
Main application file to run the simulation for the roadworks.
'''
import sys
from blocked_intervals import populate_blocked_intervals, merge_intervals
from walking_simulation import find_distance
def main():
    # Input Handling
    try:
        N, Q = map(int, sys.stdin.readline().strip().split())
        roadworks = []
        for _ in range(N):
            X, S, T = map(int, sys.stdin.readline().strip().split())
            roadworks.append((X, S, T))
        queries_input = [int(sys.stdin.readline().strip()) for _ in range(Q)]
    except ValueError as e:
        print("Error in input format. Please ensure you provide integers as specified.")
        return
    # Populate Blocked Intervals
    blocked_intervals = populate_blocked_intervals(roadworks)
    # Store Results
    distances = []
    for D in queries_input:
        distance = find_distance(D, blocked_intervals)
        distances.append(distance)
    # Output Results
    for distance in distances:
        print(distance)
if __name__ == "__main__":
    main()