'''
Main application file to run the stair climbing application.
'''
from climb_stairs import countWaysToClimb
if __name__ == "__main__":
    # Read integers N and M from standard input
    N, M = map(int, input().split())
    # Validate N and M
    if N < 0 or M < 0:
        raise ValueError("N and M must be non-negative integers.")
    # Read a list of M integers representing broken steps
    broken_steps = list(map(int, input().split())) if M > 0 else []
    # Validate broken_steps length
    if len(broken_steps) != M:
        raise ValueError("Number of broken steps does not match M.")
    # Ensure broken steps are within the range of 0 to N
    if any(step < 0 or step > N for step in broken_steps):
        raise ValueError("Broken steps must be in the range from 0 to N.")
    # Call the function to count ways to climb
    result = countWaysToClimb(N, M, broken_steps)
    # Output the result
    print(result)