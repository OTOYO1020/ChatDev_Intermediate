'''
Contains the logic to count valid combinations of sets.
'''
from typing import List
def count_valid_sets(M: int, N: int, sets: List[List[int]]) -> int:
    valid_count = 0
    # Generate all combinations of sets
    for i in range(1, 1 << M):  # from 1 to (2^M - 1)
        covered = set()
        for j in range(M):
            if i & (1 << j):  # if the j-th set is included
                covered.update(sets[j])
        # Check if all integers from 1 to N are covered
        if all(x in covered for x in range(1, N + 1)):
            valid_count += 1
    return valid_count