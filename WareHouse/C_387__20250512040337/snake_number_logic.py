'''
Contains logic for counting Snake numbers.
'''
def is_snake_number(n: int) -> bool:
    """
    Check if a given integer n is a Snake number.
    A Snake number is defined as a number where the most significant digit
    is greater than or equal to all other digits.
    """
    digits = str(n)
    most_significant_digit = digits[0]
    return all(most_significant_digit >= digit for digit in digits)
def count_snake_numbers_up_to(n: int) -> int:
    """
    Count the number of Snake numbers up to n (inclusive).
    A Snake number is defined as a number where the most significant digit
    is greater than or equal to all other digits.
    """
    if n < 10:
        return 0  # No Snake numbers below 10
    count = 0
    str_n = str(n)
    length = len(str_n)
    # Count Snake numbers with fewer digits
    for digits in range(1, length):
        count += 9  # 1-9 for the most significant digit
    # Count Snake numbers with the same number of digits
    most_significant_digit = int(str_n[0])
    # Count valid leading digits
    for digit in range(1, most_significant_digit + 1):
        count += 1  # Count valid leading digits
        count += (10 ** (length - 1)) * (most_significant_digit - digit)
    # Handle the case where the number has the same leading digit
    for i in range(1, most_significant_digit + 1):
        if i == most_significant_digit:
            # Count valid combinations for the remaining digits
            for remaining_digit in range(length - 1):
                # Ensure we respect the upper limit of n
                if remaining_digit == 0:
                    count += int(str_n[1:]) + 1  # Count the last digit as well
                else:
                    count += 10 ** (remaining_digit - 1)  # All combinations of remaining digits
                # Ensure that all digits are less than or equal to the most significant digit
                if remaining_digit > 0:
                    count -= (10 ** (remaining_digit - 1)) * (most_significant_digit - 1)
    # Additional check for the case where n itself is a Snake number
    if is_snake_number(n):
        count += 1
    return count
def count_snake_numbers(L: int, R: int) -> int:
    """
    Count the number of Snake numbers between L and R (inclusive).
    This implementation uses the helper function to count Snake numbers up to R and L-1.
    """
    return count_snake_numbers_up_to(R) - count_snake_numbers_up_to(L - 1)