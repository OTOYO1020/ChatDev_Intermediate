'''
Module containing the counting logic for valid tuples (A, B, C).
'''
def count_tuples(N: int) -> int:
    '''
    Counts the number of valid tuples (A, B, C) such that A * B + C = N.
    Parameters:
    N (int): A positive integer input.
    Returns:
    int: The count of valid tuples.
    '''
    count = 0
    for A in range(1, N + 1):
        # Calculate the maximum value of B such that C remains positive
        max_B = (N - 1) // A  # C must be at least 1, hence N - A*B > 0
        for B in range(1, max_B + 1):
            C = N - (A * B)
            if C > 0:  # Check if C is positive
                count += 1  # Increment count for valid (A, B, C)
    return count