'''
Module for checking if the target hat configuration can be achieved.
'''
from typing import List
def canAchieveTarget(S: List[str], T: List[str]) -> bool:
    """
    Determines if the target configuration T can be achieved from the current configuration S.
    Parameters:
    S (List[str]): Current hat colors.
    T (List[str]): Target hat colors.
    Returns:
    bool: True if the target configuration can be achieved, otherwise False.
    """
    # Check if both lists are permutations of each other
    return sorted(S) == sorted(T)