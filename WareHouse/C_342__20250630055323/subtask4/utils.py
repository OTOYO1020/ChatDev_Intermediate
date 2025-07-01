'''
Utility functions for the String Replacer application.
'''
def replace_characters_in_string(S, replacements):
    '''
    Replaces characters in the string S based on the provided replacements.
    Parameters:
    S (str): The original string.
    replacements (list of tuples): A list of character pairs (c, d) where c is replaced by d.
    Returns:
    str: The modified string after replacements.
    '''
    # Create a mapping for replacements
    replacement_map = {c: d for c, d in replacements}
    # Create a new string with the replacements applied
    modified_string = ''.join(replacement_map.get(char, char) for char in S)
    return modified_string