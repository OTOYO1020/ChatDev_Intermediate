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
    # Iterate through each replacement pair
    for c, d in replacements:
        S = S.replace(c, d)  # Replace all occurrences of c with d
    return S