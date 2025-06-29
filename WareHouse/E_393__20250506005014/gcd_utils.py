'''
Utility functions for GCD calculations.
'''
import math
from functools import reduce
def gcd(x, y):
    '''
    Compute the GCD of two numbers.
    '''
    return math.gcd(x, y)
def gcd_of_list(numbers):
    '''
    Compute the GCD of a list of numbers.
    '''
    return reduce(gcd, numbers)