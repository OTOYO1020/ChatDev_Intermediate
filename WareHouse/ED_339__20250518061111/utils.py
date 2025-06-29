'''
Utility file containing the function to calculate the maximum subsequence length.
'''
from typing import List
def max_subsequence_length(N: int, D: int, A: List[int]) -> int:
    '''
    Calculates the maximum length of a valid subsequence based on the given criteria.
    '''
    if N == 0 or not A:  # Check for empty input
        return 0
    max_length = 0
    current_length = 1  # Start with the first element
    for i in range(1, N):
        if abs(A[i] - A[i - 1]) <= D:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1  # Reset for a new subsequence
    max_length = max(max_length, current_length)  # Final check for the last subsequence
    return max_length