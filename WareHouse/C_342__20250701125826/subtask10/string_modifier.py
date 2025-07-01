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
    # Create a mapping for replacements
    replacement_map = {}
    # Build the replacement map
    for c_i, d_i in pairs:
        replacement_map[c_i] = d_i
    # Create a new string with the replacements
    modified_string = original_string
    for c_i, d_i in replacement_map.items():
        modified_string = modified_string.replace(c_i, d_i)
    return modified_string