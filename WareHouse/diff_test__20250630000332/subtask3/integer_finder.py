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
    # We will check for pairs (a, b) such that X = a^3 + a^2 * b + a * b^2 + b^3
    max_a = int(X**(1/3)) + 1  # a can be at most the cube root of X
    for a in range(max_a + 1):
        for b in range(max_a + 1):
            if a**3 + a**2 * b + a * b**2 + b**3 == X:
                return True
    return False