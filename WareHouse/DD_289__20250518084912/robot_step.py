'''
Module containing the logic to determine if the robot can reach the X-th step.
'''
from collections import deque
from typing import List
def canReachStep(X: int, A: List[int], B: set) -> bool:
    '''
    Determines if the robot can reach the X-th step.
    Parameters:
    X (int): The target step.
    A (List[int]): List of step sizes.
    B (set): Set of trap steps.
    Returns:
    bool: True if the robot can reach the X-th step, otherwise False.
    '''
    # Validate inputs
    if X < 0:
        return False
    if not A:
        return False  # Provide clear feedback if A is empty
    if any(step <= 0 for step in A) or any(trap < 0 for trap in B):
        return False
    if X == 0:
        return True  # Robot is already at step 0
    visited = set()
    queue = deque([0])
    while queue:
        current_step = queue.popleft()
        if current_step == X:
            return True
        for step_size in A:
            next_step = current_step + step_size
            # Only add next_step if it does not exceed X, is not visited, and is not a trap
            if next_step <= X and next_step not in visited and next_step not in B:
                visited.add(next_step)
                queue.append(next_step)
    return False