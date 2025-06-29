'''
Utility functions for validating input and checking pairs (a, b).
'''
def is_valid_input(N):
    """
    Check if the input N is within the valid range.
    """
    return 0 <= N <= 10**18
def check_pairs(X):
    """
    Check for non-negative integers a and b such that
    X = a^3 + a^2 * b + a * b^2 + b^3.
    This function has been optimized to reduce the number of iterations.
    """
    max_a = int(X**(1/3)) + 1  # Estimate upper limit for a
    for a in range(max_a):
        # Calculate the remaining value after a^3
        remaining = X - a**3
        if remaining < 0:
            continue
        # Calculate the maximum possible value for b based on remaining
        max_b = int(remaining**(1/3)) + 1  # Estimate upper limit for b
        for b in range(max_b):
            expression = a**2 * b + a * b**2 + b**3
            if expression == remaining:
                return True
            if expression > remaining:
                break  # No need to check further if the expression exceeds remaining
    return False  # Ensure the function returns False if no pairs are found