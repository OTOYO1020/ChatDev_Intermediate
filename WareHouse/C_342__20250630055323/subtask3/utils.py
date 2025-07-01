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
    # Initialize a modified string with the original string
    modified_string = S
    # Continue replacing until no changes are made
    while True:
        new_string = ''.join(replacement_map.get(char, char) for char in modified_string)
        if new_string == modified_string:  # No changes made, exit loop
            break
        modified_string = new_string  # Update modified_string for the next iteration
    return modified_string