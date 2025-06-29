'''
Utility functions for the application.
'''
def custom_pow(base, exponent):
    '''
    Calculate the power of a number using a custom implementation to handle large integers.
    This implementation uses exponentiation by squaring for efficiency.
    '''
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    if base == 0 and exponent == 0:
        raise ValueError("0 raised to the power of 0 is indeterminate")
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            result *= base
        base *= base  # Square the base
        exponent //= 2  # Divide the exponent by 2
    return result