'''
Module for counting arithmetic progressions with a given sum N.
'''
def count_arithmetic_progressions(N: int) -> int:
    '''
    Count the number of arithmetic progressions that sum to N.
    Parameters:
    N (int): The target sum of the arithmetic progressions.
    Returns:
    int: The count of valid arithmetic progressions.
    '''
    count = 0
    # Iterate through possible values of the first term 'a'
    for a in range(1, N + 1):
        # Calculate the remaining sum after taking 'a'
        remaining_sum = N - a
        # Check if remaining_sum can be expressed as k * (k - 1) / 2
        # This is equivalent to solving the quadratic equation k^2 - k - 2 * remaining_sum = 0
        # The discriminant must be a perfect square
        discriminant = 1 + 8 * remaining_sum
        if discriminant >= 0:
            sqrt_discriminant = int(discriminant**0.5)
            if sqrt_discriminant * sqrt_discriminant == discriminant:
                k = (1 + sqrt_discriminant) // 2
                if k > 0:
                    count += 1
    return count