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
    for c, d in replacements:
        if c in S:  # Check if the character to be replaced exists in the string
            S = S.replace(c, d)
        else:
            print(f"Warning: Character '{c}' not found in the string.")
    return S