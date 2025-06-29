'''
Module for calculating the number of valid divisions of a sequence.
'''
from typing import List
def count_valid_divisions(N: int, K: int, A: List[int]) -> int:
    '''
    Counts the number of ways to divide the sequence A into contiguous subsequences
    such that no subsequence sums to K.
    Parameters:
    N (int): Length of the sequence.
    K (int): Target sum.
    A (List[int]): List of integers representing the sequence.
    Returns:
    int: Count of valid divisions modulo 998244353.
    '''
    MOD = 998244353
    if N <= 0:
        return 0
    if N == 1:
        return 1 if A[0] != K else 0
    total_divisions = 1 << (N - 1)  # 2^(N-1)
    valid_count = 0
    for mask in range(total_divisions):
        current_sum = 0
        valid = True
        for i in range(N):
            current_sum += A[i]
            # Check if we need to split the subsequence
            if (mask & (1 << i)) and i < N - 1:
                if current_sum == K:
                    valid = False
                    break
                current_sum = 0  # Reset for the next subsequence
        # Check the last subsequence after the loop
        if valid and current_sum == K:
            valid = False  # Mark as invalid if the last subsequence sums to K
        if valid:
            valid_count += 1
            valid_count %= MOD
    return valid_count