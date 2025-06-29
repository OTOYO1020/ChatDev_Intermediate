'''
Module for palindrome checking logic.
'''
def is_palindrome(concat_str):
    """
    Check if the given string is a palindrome.
    A palindrome is a string that reads the same forwards and backwards.
    """
    return concat_str == concat_str[::-1]  # Check if the string is a palindrome