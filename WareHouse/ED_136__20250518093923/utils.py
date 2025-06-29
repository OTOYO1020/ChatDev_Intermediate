'''
Utility functions for input validation and formatting.
'''
def validate_input(N: int, A: list, K: int):
    if N < 2:
        raise ValueError("N must be at least 2.")
    if K < 0:
        raise ValueError("K must be a non-negative integer.")
    if len(A) != N:
        raise ValueError("Length of A must be equal to N.")