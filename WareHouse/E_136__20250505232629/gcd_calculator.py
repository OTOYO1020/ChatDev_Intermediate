'''
Module for GCD and Max Divisor calculations.
'''
from math import gcd
from functools import reduce
def calculate_gcd(A):
    '''
    Calculate the GCD of a list of integers.
    '''
    return reduce(gcd, A)
def calculate_max_divisor(A, K):
    '''
    Calculate the maximum possible positive integer divisor after K operations.
    '''
    total_sum = sum(A)
    min_value = min(A)
    gcd_value = calculate_gcd(A)  # Calculate the initial GCD of the elements
    # Adjust max_divisor based on the operations allowed
    if K >= abs(min_value - 1):
        max_divisor = total_sum + K  # This should still be valid
    else:
        max_divisor = total_sum - K  # This should still be valid
    # Ensure max_divisor is a divisor of gcd_value
    if max_divisor > gcd_value:
        max_divisor = gcd_value  # Set to GCD if max_divisor exceeds it
    # New logic to ensure max_divisor is a divisor of gcd_value
    if gcd_value > 0 and max_divisor % gcd_value != 0:
        max_divisor = max_divisor // gcd_value * gcd_value  # Adjust to the largest divisor of gcd_value
    return max(max_divisor, 0)  # Ensure max_divisor is positive; if not, set it to 0