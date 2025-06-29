'''
Module to count valid tuples (A, B, C) such that A * B + C = N.
'''
def count_valid_tuples(N):
    '''
    Function to count valid tuples (A, B, C) for a given positive integer N.
    Parameters:
    N (int): The positive integer input by the user.
    Returns:
    int: The count of valid tuples.
    '''
    count = 0
    for A in range(1, N):
        # Loop through all possible values of B ensuring A * B < N
        for B in range(1, (N - 1) // A + 1):  # Adjusted to ensure A * B < N
            C = N - (A * B)  # Calculate C based on the equation
            if C > 0:  # Check if C is a positive integer
                count += 1
    return count