'''
Module for calculating the sum of subarrays modulo M.
'''
from typing import List
def calculate_sum_mod(A: List[int], M: int) -> int:
    total_sum = 0
    n = len(A)
    # Create a prefix sum array
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + A[i - 1]  # Fill prefix sum array
    # Iterate over all pairs (l, r)
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            current_sum = prefix[r] - prefix[l - 1]  # Sum of A[l-1] to A[r-1]
            total_sum = (total_sum + current_sum % M) % M  # Accumulate the modulo
    return total_sum  # Return total_sum modulo M