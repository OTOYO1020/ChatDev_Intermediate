'''
Module for determining which person is further to the front.
'''
def find_front_person(persons, a, b):
    """
    Determines which person is further to the front between positions A and B.
    Args:
        persons (list): List of persons standing in positions.
        a (int): Position A (1-based index).
        b (int): Position B (1-based index).
    Returns:
        int: The person number standing further to the front.
        If A and B are the same, returns the person at that position.
    Raises:
        ValueError: If positions are out of valid range.
    """
    if a < 1 or b < 1 or a > len(persons) or b > len(persons):
        raise ValueError(f"Positions must be within the valid range. Received A: {a}, B: {b}, Length of persons: {len(persons)}.")
    # Adjust for 0-based indexing in Python
    a_index = a - 1
    b_index = b - 1
    # Return the person at the position that is further to the front (lower index)
    return persons[a_index] if a_index < b_index else persons[b_index]