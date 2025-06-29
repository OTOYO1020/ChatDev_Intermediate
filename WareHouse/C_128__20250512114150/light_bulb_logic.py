'''
Logic for counting valid combinations of lighted bulbs based on switch states.
'''
from typing import List, Tuple
import itertools
def count_lighted_bulbs(N: int, M: int, connections: List[Tuple[List[int], int]]) -> int:
    '''
    Counts the number of valid combinations of switch states that light all bulbs.
    Parameters:
    N (int): Number of switches.
    M (int): Number of bulbs.
    connections (List[Tuple[List[int], int]]): List of tuples containing the list of switches connected to each bulb and the required parity.
    Returns:
    int: The count of valid combinations that light all bulbs.
    '''
    valid_count = 0
    # Generate all possible combinations of switch states (0 for off, 1 for on)
    for combination in itertools.product([0, 1], repeat=N):
        if check_bulbs(combination, connections):
            valid_count += 1
    return valid_count
def check_bulbs(combination: Tuple[int], connections: List[Tuple[List[int], int]]) -> bool:
    '''
    Checks if the current combination of switch states lights all bulbs according to their conditions.
    Parameters:
    combination (Tuple[int]): Current combination of switch states.
    connections (List[Tuple[List[int], int]]): List of tuples containing the list of switches connected to each bulb and the required parity.
    Returns:
    bool: True if all bulbs are lighted according to their conditions, False otherwise.
    '''
    for switches, parity in connections:
        count_on = sum(combination[i] for i in switches)
        if count_on % 2 != parity:
            return False
    return True