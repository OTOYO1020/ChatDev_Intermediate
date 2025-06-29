'''
Utility functions for the 1122 sequence finder.
'''
from typing import List
def max_1122_subarray_length(A: List[int]) -> int:
    '''
    Computes the maximum length of a contiguous subarray that is a 1122 sequence.
    '''
    if len(A) % 2 != 0:
        return 0
    max_length = 0
    n = len(A)
    for start in range(n):
        freq = {}  # Initialize frequency dictionary for each starting index
        for end in range(start, n):
            num = A[end]
            freq[num] = freq.get(num, 0) + 1
            if (end - start + 1) % 2 == 0:  # Check only even lengths
                # Check if all counts are 2
                if all(count == 2 for count in freq.values()):
                    max_length = max(max_length, end - start + 1)
    return max_length