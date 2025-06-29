'''
Utility functions for sequence comparison.
'''
from collections import Counter
from typing import List
def can_make_equal(A: List[int], B: List[int]) -> str:
    '''
    Check if sequences A and B can be made equal by rearranging their elements.
    Parameters:
    A (List[int]): First sequence of integers.
    B (List[int]): Second sequence of integers.
    Returns:
    str: 'Yes' if sequences can be made equal, 'No' otherwise.
    '''
    if len(A) != len(B):
        return 'No'
    count_a = Counter(A)
    count_b = Counter(B)
    if count_a == count_b:
        return 'Yes'
    else:
        return 'No'