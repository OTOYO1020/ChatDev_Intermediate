'''
Module for calculating the expected value based on a list of integers.
'''
from typing import List
from math import gcd
def expected_value(A: List[int], K: int, M: int) -> int:
    n = len(A)
    num_zeros = A.count(0)
    non_zero_elements = sorted([x for x in A if x != 0])
    # If there are no zeros, simply return the K-th element modulo 998244353
    if num_zeros == 0:
        return non_zero_elements[K - 1] % 998244353
    # Calculate the expected value of the K-th element
    expected_value_k = 0
    expected_contribution_of_zeros = (M + 1) / 2  # Average value of a uniformly random integer from 1 to M
    # If K is within the range of non-zero elements
    if K <= len(non_zero_elements):
        expected_value_k += non_zero_elements[K - 1]
    else:
        zeros_needed = K - len(non_zero_elements)
        if zeros_needed > num_zeros:
            zeros_needed = num_zeros
        # Calculate expected contribution from zeros
        expected_value_k += expected_contribution_of_zeros * zeros_needed
        # Adjust for the remaining zeros that could be placed in front of the K-th position
        remaining_zeros = num_zeros - zeros_needed
        if remaining_zeros > 0:
            # Calculate the expected contribution of remaining zeros
            total_elements = len(non_zero_elements) + num_zeros
            expected_value_k += expected_contribution_of_zeros * remaining_zeros * (len(non_zero_elements) + zeros_needed) / total_elements
    # Calculate P and Q
    P = int(expected_value_k * (M + 1))
    Q = M + 1
    common_divisor = gcd(P, Q)
    P //= common_divisor
    Q //= common_divisor
    # Modular arithmetic to find R
    MOD = 998244353
    R = (P * pow(Q, MOD - 2, MOD)) % MOD
    return R