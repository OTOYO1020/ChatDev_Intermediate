'''
Module to find the smallest integer X such that X = a^3 + a^2 * b + a * b^2 + b^3 for non-negative integers a and b.
'''
def find_smallest_integer(N):
    if N < 0 or N > 10**18:
        raise ValueError("N must be in the range 0 <= N <= 10^18.")
    X = N
    while True:
        if check_pairs(X):
            return X
        X += 1
def check_pairs(X):
    '''
    Check for pairs (a, b) such that X = a^3 + a^2 * b + a * b^2 + b^3.
    This function optimizes the search by limiting the range of b based on the value of a.
    '''
    max_a = int(X**(1/3)) + 1  # a can be at most the cube root of X
    for a in range(max_a + 1):
        # Calculate the remaining value after subtracting a^3
        remaining = X - a**3
        if remaining < 0:
            continue
        # Now we need to find b such that a^2 * b + a * b^2 + b^3 = remaining
        max_b = int(remaining**(1/3)) + 1
        for b in range(max_b + 1):
            # Calculate the value of the polynomial
            polynomial_value = a**2 * b + a * b**2 + b**3
            if polynomial_value == remaining:
                return True
            if polynomial_value > remaining:
                break  # Early termination if the value exceeds remaining
    return False