'''
Module for calculating maximum GCDs from a list of integers.
'''
from math import gcd
from itertools import combinations
from typing import List
from functools import reduce
def max_gcd_with_k_elements(A: List[int], K: int) -> List[int]:
    results = []
    n = len(A)
    unique_elements = list(set(A))  # Get unique elements once
    for i in range(n):
        current_element = A[i]
        max_gcd = 0
        # Handle edge case where K is 1
        if K == 1:
            results.append(current_element)
            continue
        # Generate combinations of K-1 elements from the unique elements
        remaining_elements = [x for x in unique_elements if x != current_element]
        # If there are not enough unique elements, we cannot form a valid combination
        if len(remaining_elements) < K - 1:
            results.append(max_gcd)  # Append 0 or some default value
            continue
        # Generate combinations of K-1 elements from the remaining unique elements
        for combo in combinations(remaining_elements, K - 1):
            selected_elements = (current_element,) + combo
            current_gcd = reduce(gcd, selected_elements)  # Optimize GCD calculation
            max_gcd = max(max_gcd, current_gcd)
        results.append(max_gcd)
    return results