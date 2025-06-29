'''
Module for counting even-digit palindromes.
'''
def count_even_digit_palindromes(N: int) -> int:
    """
    Count the number of even-digit palindromes from 1 to N.
    Parameters:
    N (int): The upper limit for counting palindromes.
    Returns:
    int: The count of even-digit palindromes.
    """
    count = 0
    # Generate palindromes by constructing them from half the digits
    for half in range(1, 10**6):  # Adjust the range as needed
        half_str = str(half)
        palindrome_str = half_str + half_str[::-1]  # Create even-length palindrome
        palindrome = int(palindrome_str)
        if palindrome <= N:
            count += 1
        else:
            break  # No need to continue if the palindrome exceeds N
    return count