'''
Module to calculate distinct median values based on input ranges.
'''
from typing import List
def count_median_values(N: int, A: List[int], B: List[int]) -> int:
    # Validate input constraints
    if not (2 <= N <= 200000):
        raise ValueError("N must be between 2 and 200000.")
    if len(A) != N or len(B) != N:
        raise ValueError("Length of A and B must be equal to N.")
    for a, b in zip(A, B):
        if not (1 <= a <= b <= 10**9):
            raise ValueError("Each A_i must be between 1 and B_i, and B_i must be at most 10^9.")
    # Sort the lists A and B
    A.sort()
    B.sort()
    medians = set()
    if N % 2 == 1:  # Odd case
        median_index = (N + 1) // 2 - 1
        lower_bound = A[median_index]
        upper_bound = B[median_index]
        if lower_bound <= upper_bound:
            medians.add(lower_bound)
            medians.add(upper_bound)
    else:  # Even case
        median_index1 = N // 2 - 1
        median_index2 = N // 2
        lower_bound1 = A[median_index1]
        upper_bound1 = B[median_index1]
        lower_bound2 = A[median_index2]
        upper_bound2 = B[median_index2]
        # Calculate all possible median values
        medians.add((lower_bound1 + lower_bound2) / 2)
        medians.add((upper_bound1 + upper_bound2) / 2)
        medians.add((lower_bound1 + upper_bound2) / 2)
        medians.add((upper_bound1 + lower_bound2) / 2)
        medians.add((lower_bound1 + lower_bound1) / 2)  # Add this line
        medians.add((upper_bound1 + upper_bound1) / 2)  # Add this line
    return len(medians)