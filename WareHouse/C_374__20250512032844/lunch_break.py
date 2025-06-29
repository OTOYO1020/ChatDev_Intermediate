'''
Module to calculate the minimum possible value of the maximum number of people taking a lunch break at the same time.
'''
from typing import List
from itertools import combinations
def min_lunch_break(N: int, K: List[int]) -> int:
    # Handle edge case for no departments
    if N <= 0:
        raise ValueError("Number of departments must be greater than 0.")
    if not K:
        raise ValueError("Department sizes list cannot be empty.")
    # Handle invalid department sizes
    if any(k < 0 for k in K):
        raise ValueError("Department sizes must be non-negative.")
    # Special case for a single department
    if N == 1:
        return K[0]  # Only one department, return its size
    total_people = sum(K)
    min_max_lunch_break = float('inf')
    # Generate all possible combinations of departments
    for i in range(1, N):
        for group_a in combinations(K, i):
            group_a_sum = sum(group_a)
            group_b_sum = total_people - group_a_sum
            max_lunch_break = max(group_a_sum, group_b_sum)
            min_max_lunch_break = min(min_max_lunch_break, max_lunch_break)
    return min_max_lunch_break