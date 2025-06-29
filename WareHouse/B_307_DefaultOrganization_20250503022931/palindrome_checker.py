'''
Module containing the function to check if a string is a palindrome.
'''
def is_palindrome(concat_str):
    '''
    Check if the given string is a palindrome.
    '''
    return concat_str == concat_str[::-1]