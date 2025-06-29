'''
Module containing the function to check if Takahashi can reach a target coordinate.
'''
from typing import List, Tuple
def canReachCoordinate(N: int, jumps: List[Tuple[int, int]], X: int) -> bool:
    '''
    Checks if Takahashi can reach coordinate X after N jumps.
    '''
    if N == 0 or not jumps:
        return False
    reachable_positions = {0}  # Start from position 0
    for _ in range(N):
        new_positions = set()
        for position in reachable_positions:
            for a, b in jumps:
                new_positions.add(position + a)
                new_positions.add(position + b)
        reachable_positions = new_positions  # Update reachable positions for the next jump
    return X in reachable_positions