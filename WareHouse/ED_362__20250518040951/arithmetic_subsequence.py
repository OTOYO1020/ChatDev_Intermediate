'''
Module to count arithmetic subsequences in a given list of integers.
'''
from typing import List
from itertools import combinations
def is_arithmetic_sequence(subseq: List[int]) -> bool:
    if len(subseq) < 2:
        return False
    # Sort the subsequence to ensure correct order
    subseq.sort()
    # Check the differences
    diff = subseq[1] - subseq[0]
    for i in range(2, len(subseq)):
        if subseq[i] - subseq[i - 1] != diff:
            return False
    return True
def count_arithmetic_subsequences(N: int, A: List[int]) -> List[int]:
    if N == 0:
        return []
    if N == 1:
        return [1]  # Only one subsequence of length 1, which is the element itself
    result = [0] * N
    MOD = 998244353
    # Iterate through all lengths k from 1 to N
    for k in range(1, N + 1):
        # Generate all combinations of length k
        for subseq in combinations(A, k):
            if is_arithmetic_sequence(list(subseq)):
                result[k - 1] += 1
                result[k - 1] %= MOD
    return result