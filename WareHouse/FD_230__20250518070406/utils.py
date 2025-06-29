'''
Utility file containing the function to count unique sums from a sequence of integers.
'''
from typing import List
def count_sequences(N: int, A: List[int]) -> int:
    if N < 2:
        return 1
    unique_sums = set(A)  # Start with the original elements as potential sums
    current_sums = set(A)  # Initialize current sums with original elements
    # Check if all elements are the same
    if len(unique_sums) == 1:
        return 1  # Only one unique sum possible
    while True:
        new_sums = set()
        current_sums_list = list(current_sums)
        # Sum adjacent elements
        for i in range(len(current_sums_list) - 1):
            new_sum = current_sums_list[i] + current_sums_list[i + 1]
            new_sums.add(new_sum)  # Add new sum to the set
        # If no new sums were generated, we can break the loop
        if not new_sums:  # Check if new_sums is empty
            break
        # Update unique sums with new sums
        unique_sums.update(new_sums)
        # Update current sums to include newly generated sums
        current_sums = new_sums.union(current_sums)  # Ensure all sums are considered
    return len(unique_sums) % 998244353