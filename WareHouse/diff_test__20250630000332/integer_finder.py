'''
Module to find the smallest integer X such that X = a^3 + a^2 * b + a * b^2 + b^3 for non-negative integers a and b.
'''
def find_smallest_integer(N):
    if N < 0 or N > 10**18:
        raise ValueError("N must be in the range 0 <= N <= 10^18.")
    X = N
    max_iterations = 1000000  # Set a reasonable limit to prevent infinite loops
    iterations = 0
    while iterations < max_iterations:
        if check_pairs(X):
            return X
        X += 1
        iterations += 1
    raise RuntimeError("No valid integer found within the iteration limit.")
def check_pairs(X):
    '''
    Check for pairs (a, b) such that X = a^3 + a^2 * b + a * b^2 + b^3.
    This function optimizes the search by limiting the range of a and b based on the value of X.
    '''
    max_a = int(X**(1/3)) + 1  # a can be at most the cube root of X
    for a in range(max_a + 1):
        for b in range(max_a + 1):  # Use max_a for b as well
            polynomial_value = a**3 + a**2 * b + a * b**2 + b**3
            if polynomial_value == X:
                return True
            elif polynomial_value > X:
                break  # No need to check further if polynomial value exceeds X
    return False