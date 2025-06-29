'''
Module for counting occurrences of the substring "ABC" in a given string.
'''
def count_ABC(S):
    '''
    Count occurrences of the substring "ABC" in the string S.
    Parameters:
    S (str): The string in which to count occurrences of "ABC".
    Returns:
    int: The count of occurrences of "ABC".
    '''
    count = 0
    for i in range(len(S) - 2):
        if S[i:i + 3] == "ABC":
            count += 1
    return count