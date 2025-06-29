'''
Main entry point for the Roadwork Simulator application.
'''
import sys
from roadwork_manager import populate_blocked_intervals
from simulation import find_distance  # Importing the function to find distance
def main():
    # Input Handling
    input_data = sys.stdin.read().strip().splitlines()
    N, Q = map(int, input_data[0].split())
    roadworks = [tuple(map(int, line.split())) for line in input_data[1:N + 1]]
    start_times = [int(input_data[i]) for i in range(N + 1, N + 1 + Q)]
    # Populate Blocked Intervals
    blocked_intervals = populate_blocked_intervals(roadworks)
    # Simulate Walking
    distances = [find_distance(D_i, blocked_intervals) for D_i in start_times]
    # Output Results
    for distance in distances:
        print(distance)
if __name__ == "__main__":
    main()