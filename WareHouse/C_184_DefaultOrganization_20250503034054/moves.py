'''
Module containing the function to calculate minimum moves using BFS.
'''
from collections import deque
def min_moves(r1, c1, r2, c2):
    # Check if the start position is the same as the target position
    if (r1, c1) == (r2, c2):
        return 0
    # Initialize the queue for BFS and the visited set
    queue = deque([(r1, c1, 0)])  # (row, column, moves)
    visited = set((r1, c1))
    while queue:
        a, b, moves = queue.popleft()
        # Generate all possible next positions based on movement rules
        for delta_r in range(-3, 4):
            for delta_c in range(-3, 4):
                c, d = a + delta_r, b + delta_c
                # Check the movement rules
                if (a + b == c + d) or (a - b == c - d) or (abs(a - c) + abs(b - d) <= 3):
                    if (c, d) == (r2, c2):
                        return moves + 1
                    if (c, d) not in visited:
                        visited.add((c, d))
                        queue.append((c, d, moves + 1))
    return -1  # Indicate that the target is unreachable (theoretically should not happen)