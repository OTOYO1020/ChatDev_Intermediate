'''
Calculator module for computing the sum of K smallest elements from subarrays.
'''
from typing import List
def sum_of_k_smallest(A: List[int], N: int, M: int, K: int) -> List[int]:
    results = []
    # Check if N is greater than or equal to M
    if N < M:
        raise ValueError("N must be greater than or equal to M.")
    for i in range(N - M + 1):
        subarray = A[i:i + M]
        subarray.sort()
        k_smallest_sum = sum(subarray[:K])  # This will work for K == M as well
        results.append(k_smallest_sum)
    return results