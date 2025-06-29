'''
Utility functions for calculating the minimum digits to erase.
'''
def calculate_min_erased(n):
    digits = [int(d) for d in str(n)]
    digit_sum = sum(digits)
    remainder = digit_sum % 3
    k = len(digits)
    min_erased = k  # Start with the maximum number of digits that can be erased
    # Check if the sum of digits is already a multiple of 3
    if remainder == 0:
        return 0  # No need to erase any digits
    count_remainder_1 = sum(1 for d in digits if d % 3 == 1)
    count_remainder_2 = sum(1 for d in digits if d % 3 == 2)
    if remainder == 1:
        if count_remainder_1 >= 1:
            min_erased = min(min_erased, 1)
        if count_remainder_2 >= 2:
            min_erased = min(min_erased, 2)
    elif remainder == 2:
        if count_remainder_2 >= 1:
            min_erased = min(min_erased, 1)
        if count_remainder_1 >= 2:
            min_erased = min(min_erased, 2)
    # Return -1 if no valid erasure options were found
    return min_erased if min_erased < k else -1  # Ensure we return -1 if not possible