'''
Utility functions for checking multiples of 3 and calculating minimum digits to erase.
'''
from itertools import combinations
from typing import Tuple
def is_multiple_of_3(num: str) -> bool:
    '''
    Check if the given number represented as a string is a multiple of 3.
    '''
    digit_sum = sum(int(digit) for digit in num)
    return digit_sum % 3 == 0
def min_digits_to_erase(N: int) -> Tuple[bool, int]:
    '''
    Determine if a multiple of 3 can be formed from the digits of N
    and calculate the minimum digits to erase.
    '''
    str_N = str(N)
    k = len(str_N)
    min_erased = float('inf')
    found = False
    checked_combinations = set()  # To avoid checking the same combination multiple times
    for i in range(1, k + 1):  # Start from 1 to avoid empty combination
        for combo in combinations(str_N, i):
            num_str = ''.join(combo)
            # Check if the number is valid (not starting with '0' unless it is '0')
            if num_str and (num_str[0] != '0' or num_str == '0'):  # Allow '0' only as a single digit
                if num_str not in checked_combinations:  # Check if already processed
                    checked_combinations.add(num_str)
                    if is_multiple_of_3(num_str):
                        found = True
                        digits_erased = k - len(num_str)
                        min_erased = min(min_erased, digits_erased)
    return found, min_erased if found else -1