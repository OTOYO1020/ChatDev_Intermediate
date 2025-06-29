'''
Contains the implementation of the max_divisor function that computes the maximum divisor
after performing specified operations on the list A.
'''
from math import gcd
from functools import reduce
def max_divisor(N: int, A: list, K: int) -> int:
    if N < 2:
        raise ValueError("N must be at least 2.")
    if K < 0:
        raise ValueError("K must be a non-negative integer.")
    if len(A) != N:
        raise ValueError("Length of A must be equal to N.")
    total_positive = sum(A)
    if total_positive < K:
        raise ValueError("Not enough total value in A to perform K operations without going negative.")
    operations = 0
    while operations < K:
        # Find valid indices i and j
        valid_indices = [idx for idx in range(N) if A[idx] > 0]
        if len(valid_indices) < 2:
            break  # Not enough valid indices to perform operations
        # Use a controlled loop to select indices
        found = False
        for i in valid_indices:
            for j in valid_indices:
                if i != j and A[j] > 0:
                    # Perform the operation
                    A[i] += 1
                    A[j] -= 1
                    operations += 1
                    found = True
                    break
            if found:
                break
    # Ensure all elements are non-negative before calculating GCD
    if any(a < 0 for a in A):
        raise ValueError("List A contains negative values after operations.")
    # Compute GCD for the entire list A
    return reduce(gcd, A) if A else 0  # Return GCD or 0 if A is empty