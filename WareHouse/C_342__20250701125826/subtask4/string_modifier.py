"""
Module containing the character replacement logic.
"""


def replace_characters(original_string, pairs):
    """
    Replaces characters in the original string based on the provided pairs.
    Parameters:
    original_string (str): The string to modify.
    pairs (list of tuples): A list of character pairs (c_i, d_i) for replacement.
    Returns:
    str: The modified string after replacements.
    """
    # Create a mapping for replacements
    replacement_map = {c_i: d_i for c_i, d_i in pairs}
    # Create a new string with the replacements
    modified_string = original_string
    # Continue replacing until no changes are made
    while True:
        new_string = "".join(
            replacement_map.get(char, char) for char in modified_string
        )
        if new_string == modified_string:  # No changes made
            break
        modified_string = new_string
    return modified_string
