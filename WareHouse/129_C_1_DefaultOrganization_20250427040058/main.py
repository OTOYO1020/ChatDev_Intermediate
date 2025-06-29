'''
Main application file for the Climbing Steps application.
'''
from climbing_logic import countWaysToClimb
if __name__ == "__main__":
    # Input Handling
    N, M = map(int, input().split())
    broken_steps = list(map(int, input().split()))
    # Pass parameters to the function
    result = countWaysToClimb(N, M, broken_steps)
    # Output the result
    print(result)