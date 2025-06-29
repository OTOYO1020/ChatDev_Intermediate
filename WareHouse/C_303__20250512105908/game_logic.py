'''
Contains the logic for determining if Takahashi can complete his moves.
'''
from typing import List, Tuple
def can_complete_moves(N: int, M: int, H: int, K: int, S: str, items: List[Tuple[int, int]]) -> bool:
    position = (0, 0)
    health = H
    item_set = set(items)
    for move in S:
        # Update position based on the move
        if move == 'R':
            position = (position[0] + 1, position[1])
        elif move == 'L':
            position = (position[0] - 1, position[1])
        elif move == 'U':
            position = (position[0], position[1] + 1)
        elif move == 'D':
            position = (position[0], position[1] - 1)
        # Check if the new position is within the grid boundaries
        if position[0] < 0 or position[0] >= M or position[1] < 0 or position[1] >= N:
            return False
        health -= 1  # Decrement health for each move
        if health < 0:
            return False
        # Check if the current position is on an item and health is less than K
        if position in item_set and health < K:
            health = K  # Restore health to K only if it's below K
    return True