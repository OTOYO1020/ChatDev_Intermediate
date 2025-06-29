'''
Contains functions to check if a number is a palindrome,
including handling leading zeros.
'''
def is_palindrome(s):
    """Check if the given string is a palindrome."""
    return s == s[::-1]
def check_palindrome(number):
    """Check if the number or its padded versions can form a palindrome."""
    str_N = str(number)
    # Additional check for the case where the number is "0"
    if str_N == "0":
        return "YES"
    # Check if the original string representation is a palindrome
    if is_palindrome(str_N):
        return "YES"
    length = len(str_N)
    # Check for palindromes with leading zeros, limiting the count
    for leading_zeros in range(1, length + 1):  # Change to length + 1 to include full length
        padded_str = '0' * leading_zeros + str_N
        if is_palindrome(padded_str):
            return "YES"
    return "NO"