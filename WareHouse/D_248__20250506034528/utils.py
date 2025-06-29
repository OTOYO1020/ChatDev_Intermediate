'''
Utility functions for counting occurrences in a sequence.
'''
def count_occurrences(A, L, R, X):
    '''
    Counts how many elements in the subarray A[L-1:R] are equal to X.
    Parameters:
    A (list): The list of integers.
    L (int): The starting index (1-based).
    R (int): The ending index (1-based).
    X (int): The integer to count.
    Returns:
    int: The count of occurrences of X in the specified range.
    '''
    count = 0
    for i in range(L - 1, R):
        if A[i] == X:
            count += 1
    return count