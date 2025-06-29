'''
This module contains functions to check for lunlun numbers and generate them.
'''
from typing import List
from collections import deque
def is_lunlun_number(num: int) -> bool:
    """
    Check if a number is a lunlun number.
    A lunlun number has the property that the absolute difference between
    each pair of adjacent digits is at most 1.
    """
    digits = list(map(int, str(num)))
    for i in range(len(digits) - 1):
        if abs(digits[i] - digits[i + 1]) > 1:
            return False
    return True
def generate_lunlun_numbers(limit: int) -> List[int]:
    """
    Generate lunlun numbers up to a specified limit using BFS.
    """
    lunlun_numbers = set()  # Use a set to avoid duplicates
    queue = deque(range(10))  # Start with single-digit numbers
    while queue:
        num = queue.popleft()
        if num <= limit:  # Check if the number is within the limit
            lunlun_numbers.add(num)  # Add to set for uniqueness
            last_digit = num % 10
            # Generate next lunlun numbers
            for next_digit in (last_digit - 1, last_digit, last_digit + 1):
                if 0 <= next_digit <= 9:  # Ensure next digit is valid
                    next_num = num * 10 + next_digit
                    if next_num <= limit:  # Check before adding to queue
                        queue.append(next_num)
    return sorted(lunlun_numbers)  # Return sorted list of unique numbers
def find_kth_lunlun_number(K: int) -> int:
    """
    Find the K-th smallest lunlun number.
    """
    limit = 10**6  # Start with a reasonable limit
    lunlun_numbers = generate_lunlun_numbers(limit)
    # Increase limit until we have enough lunlun numbers
    while len(lunlun_numbers) < K:
        limit *= 2  # Double the limit
        lunlun_numbers = generate_lunlun_numbers(limit)
        if limit > 10**9:  # Safety cap to prevent infinite loop
            raise ValueError("Exceeded maximum limit for lunlun number generation. Please try a smaller K.")
    return lunlun_numbers[K - 1]  # K is 1-based index