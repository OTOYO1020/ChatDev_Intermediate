'''
Utility functions for finding coprime integers.
'''
from math import gcd
from typing import List
def find_coprime_integers(N: int, M: int, A: List[int]) -> List[int]:
    '''
    This function finds all integers k from 1 to M that are coprime with all integers in list A.
    Parameters:
    N (int): The number of integers in list A.
    M (int): The upper limit for k.
    A (List[int]): The list of positive integers.
    Returns:
    List[int]: A list of integers k that are coprime with all integers in A.
    '''
    result = []
    # Handle the case when N is 0
    if N == 0:
        return result  # Return an empty list when N is 0
    for k in range(1, M + 1):
        if all(gcd(a, k) == 1 for a in A):
            result.append(k)
    return result