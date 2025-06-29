'''
Main application file for the Robot Step Checker.
'''
from collections import deque
from typing import List
from robot_step import canReachStep
if __name__ == "__main__":
    # Input handling and output logic
    import sys
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    # Validate and parse input
    try:
        X = int(input_data[0])
        A = list(map(int, input_data[1].split(','))) if len(input_data) > 1 else []
        B = set(map(int, input_data[2].split(','))) if len(input_data) > 2 else set()
    except ValueError:
        print("NO")
        sys.exit(1)
    # Validate input and call the function
    if canReachStep(X, A, B):
        print("YES")
    else:
        print("NO")