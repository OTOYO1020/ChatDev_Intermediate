'''
Utility functions for generating and checking 321-like numbers.
'''
from itertools import combinations, permutations
def find_kth_321_like_number(K: int) -> int:
    """
    Find the K-th smallest 321-like number.
    Generates all possible 321-like numbers and returns the K-th one.
    """
    if K < 1:
        raise ValueError("K must be a positive integer.")
    # Use a set to store unique 321-like numbers
    numbers = set()
    # Generate all 321-like numbers using decreasing sequences
    for length in range(3, 10):  # Length of numbers from 3 to 9
        for combo in combinations(range(1, 10), length):
            # Create all permutations of the combination and filter for decreasing order
            for perm in permutations(combo):
                if list(perm) == sorted(perm, reverse=True):  # Check if it's strictly decreasing
                    number = int(''.join(map(str, perm)))
                    numbers.add(number)  # Add directly to set for uniqueness
    # Convert set to sorted list to find the K-th smallest
    sorted_numbers = sorted(numbers)
    if K <= len(sorted_numbers):
        return sorted_numbers[K - 1]
    else:
        raise ValueError("K is out of bounds for the generated 321-like numbers.")