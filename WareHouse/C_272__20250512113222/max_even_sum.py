'''
Module to find the maximum even sum of pairs from a list of integers.
'''
from typing import List
def find_max_even_sum(A: List[int]) -> int:
    '''
    Find the maximum even sum of pairs in the list A.
    Returns -1 if no valid pairs exist.
    '''
    if len(A) < 2:
        return -1
    max_even1 = max_even2 = -1
    max_odd1 = max_odd2 = -1
    # Iterate through the list to find the two largest even and odd numbers
    for number in A:
        if number % 2 == 0:  # Even number
            if number > max_even1:
                max_even2 = max_even1
                max_even1 = number
            elif number > max_even2:
                max_even2 = number
        else:  # Odd number
            if number > max_odd1:
                max_odd2 = max_odd1
                max_odd1 = number
            elif number > max_odd2:
                max_odd2 = number
    max_even_sum = -1
    # Check if we found two even numbers
    if max_even1 != -1 and max_even2 != -1:
        max_even_sum = max(max_even_sum, max_even1 + max_even2)
    # Check if we found two odd numbers
    if max_odd1 != -1 and max_odd2 != -1:
        max_even_sum = max(max_even_sum, max_odd1 + max_odd2)
    return max_even_sum if max_even_sum != -1 else -1