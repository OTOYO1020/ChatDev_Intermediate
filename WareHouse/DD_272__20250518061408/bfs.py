'''
Contains the BFS function to determine reachable squares in a grid.
'''
from typing import List, Tuple
from collections import deque
import math
def canReach(N: int, M: int) -> List[Tuple[int, int, bool, int]]:
    # Check if M is zero
    if M == 0:
        result = [(i, j, (i == 1 and j == 1), 0 if (i == 1 and j == 1) else -1) for i in range(1, N + 1) for j in range(1, N + 1)]
        return result
    # Check if M is valid
    if M < 0:
        return [(i, j, False, -1) for i in range(1, N + 1) for j in range(1, N + 1)]
    result = [[(i, j, False, -1) for j in range(1, N + 1)] for i in range(1, N + 1)]
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    queue = deque([(1, 1, 0)])  # (i, j, operations)
    visited[1][1] = True
    result[0][0] = (1, 1, True, 0)  # Starting position is reachable with 0 operations
    distance = int(math.sqrt(M))
    # Calculate possible moves based on distance
    possible_moves = []
    for dx in range(-distance, distance + 1):
        for dy in range(-distance, distance + 1):
            if dx * dx + dy * dy == M:
                possible_moves.append((dx, dy))
    while queue:
        i, j, operations = queue.popleft()
        for dx, dy in possible_moves:  # Iterate through all possible moves
            new_k = i + dx
            new_l = j + dy
            if 1 <= new_k <= N and 1 <= new_l <= N:
                if not visited[new_k][new_l]:
                    visited[new_k][new_l] = True
                    queue.append((new_k, new_l, operations + 1))
                    result[new_k - 1][new_l - 1] = (new_k, new_l, True, operations + 1)
                else:
                    # Check if we found a shorter path to (new_k, new_l)
                    if result[new_k - 1][new_l - 1][3] > operations + 1:
                        result[new_k - 1][new_l - 1] = (new_k, new_l, True, operations + 1)
    # Finalize results for all squares
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not visited[i][j]:  # If not reachable
                result[i - 1][j - 1] = (i, j, False, -1)  # Update to unreachable
    return [item for sublist in result for item in sublist]  # Flatten the result list