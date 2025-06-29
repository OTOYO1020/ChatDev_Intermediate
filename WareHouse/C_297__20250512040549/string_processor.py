'''
Module for string processing functions.
'''
from typing import List
def max_pcs(H: int, W: int, S: List[str]) -> List[str]:
    """
    Replace occurrences of 'TT' with 'PC' in each string of the input list.
    Parameters:
    H (int): The number of strings in the list.
    W (int): The maximum length of each string.
    S (List[str]): The list of strings to process.
    Returns:
    List[str]: A list of modified strings with 'TT' replaced by 'PC'.
    """
    result = []
    for string in S:
        # Check if the string exceeds the maximum length W
        if len(string) > W:
            raise ValueError(f"String '{string}' exceeds the maximum length of {W}.")
        modified_string = ""
        i = 0
        while i < len(string):
            # Check for the occurrence of 'TT'
            if i < len(string) - 1 and string[i:i+2] == 'TT':
                modified_string += 'PC'  # Replace 'TT' with 'PC'
                i += 2  # Skip the next character to avoid overlap
            else:
                modified_string += string[i]  # Keep the current character
                i += 1  # Move to the next character
        result.append(modified_string)  # Add the modified string to the result list
    return result