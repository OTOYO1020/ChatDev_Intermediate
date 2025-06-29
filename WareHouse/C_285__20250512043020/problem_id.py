'''
Module for calculating the index of a problem ID.
'''
def find_problem_index(S: str) -> int:
    '''
    Calculate the index of the problem ID S among all possible problem IDs.
    '''
    if not S.isalpha() or not S.isupper():
        raise ValueError("Problem ID must be an uppercase alphabetic string.")
    length = len(S)
    # Calculate total number of problem IDs with lengths less than that of S
    total_count = sum(combinations_count(i) for i in range(1, length))
    # Calculate the index of the problem ID S among IDs of the same length
    index = index_of_problem_id(S)
    return total_count + index
def combinations_count(length: int) -> int:
    '''
    Calculate the number of combinations of uppercase English letters for a given length.
    '''
    return 26 ** length
def index_of_problem_id(S: str) -> int:
    '''
    Calculate the index of the problem ID S among IDs of the same length.
    '''
    index = 0
    length = len(S)
    for i, char in enumerate(S):
        position = ord(char) - ord('A')
        index += position * (26 ** (length - i - 1))
    return index