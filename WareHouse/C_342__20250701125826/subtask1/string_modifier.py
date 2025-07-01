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
    modified_string = original_string  # Start with the original string
    for c, d in pairs:
        modified_string = modified_string.replace(
            c.strip(), d.strip()
        )  # Use a temporary modified string
    return modified_string
