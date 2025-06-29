'''
Module for generating repunits and finding the N-th smallest sum of combinations.
'''
from typing import List
from itertools import combinations
def generate_repunits(max_digits: int) -> List[int]:
    '''
    Generate repunits up to a specified number of digits.
    A repunit is a number consisting of only the digit 1.
    '''
    repunits = []
    for i in range(1, max_digits + 1):
        repunit = int('1' * i)  # Generate repunit by repeating '1'
        repunits.append(repunit)
    return repunits
def find_nth_repunits_sum(N: int) -> int:
    '''
    Find the N-th smallest sum of combinations of three repunits.
    '''
    repunits = generate_repunits(333)  # Generate repunits with up to 333 digits
    unique_sums = set()
    # Use combinations to generate unique sums of three repunits
    for i, j, k in combinations(repunits, 3):
        sum_value = i + j + k
        unique_sums.add(sum_value)
    sorted_sums = sorted(unique_sums)
    if len(sorted_sums) < N:
        return -1  # Indicate that there are not enough unique sums
    return sorted_sums[N - 1]