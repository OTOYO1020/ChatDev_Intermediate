'''
This module contains the logic to equalize a list of integers by dividing them by 2 or 3.
'''
from typing import List, Tuple
def reduce_to_prime_factors(x: int) -> Tuple[int, int]:
    """
    Returns the count of 2s and 3s in the prime factorization of x.
    Parameters:
    x (int): A positive integer to factorize.
    Returns:
    Tuple[int, int]: A tuple containing the count of 2s and 3s.
    """
    if x <= 0:
        raise ValueError("Input must be a positive integer.")  # Raise exception for non-positive integers
    count_2 = 0
    count_3 = 0
    while x % 2 == 0:
        count_2 += 1
        x //= 2
    while x % 3 == 0:
        count_3 += 1
        x //= 3
    return count_2, count_3
def min_operations_to_equalize(A: List[int]) -> int:
    """
    Determines the minimum number of operations required to equalize a list of integers
    by dividing them by 2 or 3.
    Parameters:
    A (List[int]): A list of positive integers.
    Returns:
    int: The minimum number of operations to equalize the integers, or -1 if impossible.
    """
    if not A:  # Check for empty list
        return -1
    if any(x <= 0 for x in A):  # Check for non-positive integers
        return -1
    if len(set(A)) == 1:  # Check if all elements are already equal
        return 0
    try:
        counts = [reduce_to_prime_factors(x) for x in A]
    except ValueError as e:
        print(e)
        return -1  # Handle the exception for non-positive integers
    # Calculate the base numbers after removing all factors of 2 and 3
    base_numbers = [x // (2 ** counts[i][0] * 3 ** counts[i][1]) for i, x in enumerate(A)]
    # Check if all base numbers are the same
    first_base = base_numbers[0]
    for base in base_numbers:
        if base != first_base:  # If any base number differs from the first
            return -1  # Return -1 if the base numbers differ
    # Calculate the total operations needed to equalize counts of 2s and 3s
    total_operations = 0
    max_count_2 = max(count[0] for count in counts)
    max_count_3 = max(count[1] for count in counts)
    for count in counts:
        total_operations += (max_count_2 - count[0]) + (max_count_3 - count[1])
    return total_operations