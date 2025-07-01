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
    # Create a dictionary to map characters to their final replacements
    replacement_map = {}
    # Build the replacement map
    for c, d in replacements:
        replacement_map[c] = d
    # Create a new string with the replacements applied
    modified_string = S
    while True:
        new_string = ''.join(replacement_map.get(char, char) for char in modified_string)
        if new_string == modified_string:  # If no changes, break the loop
            break
        modified_string = new_string
    # Resolve cascading replacements
    final_string = ''.join(replacement_map.get(char, char) for char in modified_string)
    return final_string