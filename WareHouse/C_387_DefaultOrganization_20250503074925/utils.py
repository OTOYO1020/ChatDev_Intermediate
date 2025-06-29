'''
Utility file containing functions related to Snake number calculations.
'''
def is_snake_number(num):
    """
    Determine if a number is a Snake number.
    A Snake number is defined as a number where all digits after the most significant digit are less than it.
    Parameters:
    num (int): The number to check.
    Returns:
    bool: True if the number is a Snake number, False otherwise.
    """
    num_str = str(num)
    top_digit = int(num_str[0])
    for digit in num_str[1:]:
        if int(digit) >= top_digit:
            return False
    return True
def count_snake_numbers_iterative(digit_position, is_tight, top_digit, num_str):
    """
    Iterative function to count Snake numbers based on digit positions.
    This function ensures that the digits being processed do not exceed the constraints
    imposed by the upper limit number.
    """
    count = 0
    while digit_position < len(num_str):
        limit = int(num_str[digit_position]) if is_tight else 9
        for digit in range(0, limit + 1):
            if digit <= top_digit:
                count += 1
                # Move to the next digit
                digit_position += 1
                is_tight = is_tight and (digit == limit)
                break  # Exit the loop after processing the current digit
        else:
            break  # Exit if no valid digit was found
    return count
def count_snake_up_to(n):
    """
    Count the number of Snake numbers up to a given number n.
    This function analyzes the digits of n and counts valid combinations.
    Parameters:
    n (int): The upper limit to count Snake numbers.
    Returns:
    int: The count of Snake numbers up to n.
    """
    if n < 1:
        return 0
    count = 0
    num_str = str(n)
    length = len(num_str)
    # Count Snake numbers with fewer digits
    for digits in range(1, length):
        count += 9 * (10 ** (digits - 1))  # 1-9 for the first digit, then 0-9 for the rest
    # Count Snake numbers with the same number of digits
    top_digit = int(num_str[0])
    # Count valid combinations for the first digit
    for i in range(1, top_digit):
        count += 10 ** (length - 1)  # Remaining digits can be anything from 0-9
    # Handle the case where the first digit is the top_digit
    count += count_snake_numbers_iterative(1, True, top_digit, num_str)
    # Check if the number itself is a Snake number
    if is_snake_number(n):
        count += 1
    return count
def optimized_count_snake_numbers(L, R):
    """
    Count the number of Snake numbers in the range [L, R].
    Utilizes the count_snake_up_to function for efficiency.
    """
    if L == R:
        return 1 if is_snake_number(L) else 0
    count = count_snake_up_to(R) - count_snake_up_to(L - 1)
    return count