'''
Utility functions for calculating problem ID index and total IDs.
'''
def calculate_total_ids(length):
    '''
    Calculate the total number of problem IDs with lengths less than the given length.
    Parameters:
    length (int): The length of the problem ID string.
    Returns:
    int: The total number of problem IDs with lengths less than the given length.
    '''
    if length <= 1:
        return 0  # No problem IDs with lengths less than 1
    # Correct formula for the sum of a geometric series
    total_ids = (26 ** length - 1) // 25
    return total_ids
def calculate_index_of_problem_id(S):
    '''
    Calculate the index of the given problem ID string.
    Parameters:
    S (str): The problem ID string.
    Returns:
    int: The 1-indexed position of the problem ID in the sequence of all possible IDs.
    '''
    length = len(S)
    total_ids = calculate_total_ids(length)
    index = 0
    for i, char in enumerate(S):
        position_of_char = ord(char) - ord('A')
        index += position_of_char * (26 ** (length - i - 1))
    index += total_ids + 1  # 1-indexed
    return index