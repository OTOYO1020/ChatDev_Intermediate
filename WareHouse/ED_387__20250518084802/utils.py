'''
Utility functions for calculating digit sum, checking good integers,
and finding twin good integers.
'''
from typing import Tuple, Union
def digit_sum(n: int) -> int:
    '''Calculates the sum of the digits of a positive integer n.'''
    return sum(int(digit) for digit in str(n))
def is_good_integer(n: int) -> bool:
    '''Checks if a positive integer n is divisible by its digit sum.'''
    d_sum = digit_sum(n)
    if d_sum == 0:
        return False  # This case should not occur for positive integers, but it's a safeguard.
    return n % d_sum == 0
def find_twin_good_integers(N: int) -> Union[Tuple[int, int], str]:
    '''Finds a pair of twin good integers (a, a + 1) such that N <= a <= 2N.'''
    for a in range(N, 2 * N + 1):
        if is_good_integer(a) and is_good_integer(a + 1):
            return (a, a + 1)
    return "No twin good integers found in the specified range."  # Return a message instead of None