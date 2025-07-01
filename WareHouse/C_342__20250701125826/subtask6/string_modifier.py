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
    modified_string = original_string
    # Replace characters based on the original pairs order
    for c_i, d_i in pairs:
        modified_string = modified_string.replace(c_i, d_i)
    return modified_string