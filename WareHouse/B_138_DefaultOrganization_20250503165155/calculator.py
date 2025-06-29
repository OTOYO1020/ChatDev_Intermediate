'''
Module for calculating the multiplicative inverse of the sum of inverses.
'''
def calculate_inverse(sequence):
    """
    Calculate the multiplicative inverse of the sum of inverses of the given sequence of positive integers.
    Parameters:
    sequence (list): A list of positive integers.
    Returns:
    float: The multiplicative inverse of the sum of inverses.
    """
    sum_of_inverses = 0
    for number in sequence:
        sum_of_inverses += 1 / number  # No need to check for zero since input is validated
    # Check if sum_of_inverses is zero to avoid division by zero
    if sum_of_inverses == 0:
        raise ValueError("The sum of inverses is zero, cannot compute multiplicative inverse.")
    result = 1 / sum_of_inverses
    return result