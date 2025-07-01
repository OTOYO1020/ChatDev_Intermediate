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
    # Create a translation table
    translation_table = str.maketrans({c: d for c, d in replacements if c != d})
    # Use the translation table to replace characters in the string
    modified_string = S.translate(translation_table)
    return modified_string