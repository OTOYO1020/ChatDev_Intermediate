'''
Logic for determining if a target coordinate can be reached using jumps.
'''
from collections import deque
def canReach(X, jumps):
    """
    Determine if the target coordinate X can be reached using the given jumps.
    Parameters:
    X (int): The target coordinate.
    jumps (list of tuples): A list of tuples where each tuple contains two integers (a_i, b_i).
    Returns:
    bool: True if X can be reached, False otherwise.
    """
    possible_positions = {0}
    queue = deque([0])  # Initialize queue for BFS
    while queue:
        current_position = queue.popleft()
        for a_i, b_i in jumps:
            for new_position in (current_position + a_i, current_position + b_i):
                if new_position == X:
                    return True
                if new_position not in possible_positions:
                    possible_positions.add(new_position)
                    queue.append(new_position)
    return False  # Return False if X is not reachable