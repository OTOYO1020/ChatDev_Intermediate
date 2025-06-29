'''
Module to define functions related to counting happy sets.
'''
from itertools import combinations
from typing import List
def is_coprime(x: int, y: int) -> bool:
    '''Check if two integers are coprime.'''
    while y:
        x, y = y, x % y
    return x == 1
def count_happy_sets(A: int, B: int) -> int:
    '''Count the number of happy sets between A and B.'''
    if A > B:
        return 0  # Invalid input case
    cards = list(range(A, B + 1))
    happy_count = 0
    # Generate all subsets using combinations
    for r in range(len(cards) + 1):
        for subset in combinations(cards, r):
            if len(subset) > 0:
                all_coprime = True
                for x, y in combinations(subset, 2):
                    if not is_coprime(x, y):
                        all_coprime = False
                        break
                if all_coprime:
                    happy_count += 1
    return happy_count