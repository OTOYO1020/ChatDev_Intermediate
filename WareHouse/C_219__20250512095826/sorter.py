'''
Module for sorting names based on a custom alphabetical order.
'''
from typing import List
def is_valid_permutation(new_order: str) -> bool:
    '''
    Validates if the provided new order is a valid permutation of the lowercase English letters.
    '''
    return len(new_order) == 26 and len(set(new_order)) == 26 and all(c in new_order for c in 'abcdefghijklmnopqrstuvwxyz')
def sort_names(new_order: str, names: List[str]) -> List[str]:
    '''
    Sorts the list of names based on the custom alphabetical order provided.
    Parameters:
    new_order (str): The new alphabetical order.
    names (List[str]): The list of names to sort.
    Returns:
    List[str]: The sorted list of names.
    '''
    if not is_valid_permutation(new_order):
        raise ValueError("Invalid alphabetical order. Must be a permutation of 'abcdefghijklmnopqrstuvwxyz'.")
    order_map = {char: index for index, char in enumerate(new_order)}
    # Validate names
    for name in names:
        if any(char not in order_map for char in name):
            raise ValueError(f"Name '{name}' contains invalid characters.")
    def custom_compare(name: str) -> List[int]:
        return [order_map[char] for char in name]  # Directly map characters to their indices
    return sorted(names, key=custom_compare)