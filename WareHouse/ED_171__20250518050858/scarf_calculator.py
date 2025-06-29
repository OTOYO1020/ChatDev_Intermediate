'''
Module for calculating scarf values based on XOR inputs.
'''
from typing import List
def restore_scarves(N: int, a: List[int]) -> List[int]:
    '''
    Calculate the scarf values for Snuke Cats based on XOR values.
    Parameters:
    N (int): Number of Snuke Cats.
    a (List[int]): List of XOR values.
    Returns:
    List[int]: List of calculated scarf values.
    '''
    # Validate that all values in 'a' are within the specified range
    for value in a:
        if not (0 <= value <= 10**9):
            raise ValueError("One or more XOR values are out of the valid range (0 ≤ a[i] ≤ 10^9).")
    total_xor = 0
    for value in a:
        total_xor ^= value
    scarf = [total_xor ^ value for value in a]
    # Ensure all computed integers are within the range (0 ≤ scarf[i] ≤ 10^9)
    for scarf_value in scarf:
        if not (0 <= scarf_value <= 10**9):
            raise ValueError("One or more computed scarf values are out of the valid range (0 ≤ scarf[i] ≤ 10^9).")
    return scarf