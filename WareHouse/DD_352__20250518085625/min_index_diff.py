'''
Module to calculate the minimum index difference for a given permutation.
'''
from itertools import combinations
def find_minimum_index_difference(N: int, K: int, P: list) -> int:
    # Handle edge cases
    if K <= 0 or N <= 0:
        raise ValueError("N and K must be positive integers.")
    if K > N:
        return -1  # Return -1 if K is greater than N, indicating no valid sequences can be formed
    if K == 1:
        return 0  # Only one index, difference is zero
    if N == K:
        return N - 1  # All indices are selected, difference is N-1
    min_diff = float('inf')
    good_sequences = combinations(range(N), K)
    for indices in good_sequences:
        subsequence = [P[i] for i in indices]  # This is correct as indices are zero-based
        if can_form_consecutive(subsequence):
            # Adjusting for 1-based indexing for the difference calculation
            diff = (indices[-1] + 1) - (indices[0] + 1)  # Adjust for one-based indexing
            min_diff = min(min_diff, diff)
    return min_diff if min_diff != float('inf') else -1  # No need to add 1 here, as min_diff is already adjusted
def can_form_consecutive(subsequence: list) -> bool:
    # Check if the subsequence can be rearranged to form consecutive integers
    if len(subsequence) < 2:
        return True  # A single element or empty can be considered consecutive
    unique_values = set(subsequence)
    if len(unique_values) != len(subsequence):  # Check for duplicates
        return False
    return (max(unique_values) - min(unique_values) == len(unique_values) - 1)