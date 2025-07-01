'''
Module containing the character replacement logic.
'''
def replace_characters(original_string, pairs):
    '''
    Replaces characters in the original string based on the provided pairs.
    Parameters:
    original_string (str): The string to modify.
    pairs (list of tuples): A list of character pairs (c_i, d_i) for replacement.
    Returns:
    str: The modified string after replacements.
    '''
    # Create a mapping of replacements
    replacement_map = {}
    for c_i, d_i in pairs:
        replacement_map[c_i] = d_i
    # Create a new string with replacements
    modified_string = ''.join(replacement_map.get(char, char) for char in original_string)
    return modified_string