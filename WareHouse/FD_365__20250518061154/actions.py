'''
Module containing the minimum_actions function and related logic.
'''
from typing import List, Tuple
from collections import deque
def minimum_actions(N: int, L: List[int], U: List[int], Q: int, queries: List[Tuple[int, int, int, int]]) -> List[int]:
    # Initialize grid representation
    grid = [['.' for _ in range(max(U) + 1)] for _ in range(N)]
    for i in range(N):
        # Mark empty cells based on lower and upper bounds
        for j in range(L[i], U[i] + 1):
            if j < len(grid[i]):  # Ensure j is within bounds before marking
                grid[i][j] = 'E'  # Mark empty cells
        # Ensure L[i] is within bounds and mark as wall if it's not already marked as empty
        if L[i] < len(grid[i]) and grid[i][L[i]] != 'E':
            grid[i][L[i]] = 'W'  # Mark wall cells at L[i]
        # Ensure U[i] is within bounds and mark as wall if it's not already marked as empty
        if U[i] < len(grid[i]) and U[i] > 0 and grid[i][U[i]] != 'E':
            grid[i][U[i]] = 'W'  # Mark wall cells at U[i]
    def bfs(start: Tuple[int, int], target: Tuple[int, int]) -> int:
        # If the starting cell is a wall, return -1 immediately
        if grid[start[0]][start[1]] == 'W':
            return -1
        # If the starting cell is the same as the target cell
        if start == target:
            return 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible movements (right, down, left, up)
        queue = deque([start])
        visited = set()
        visited.add(start)
        distance = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # Check if the next cell is within bounds and is an empty cell
                    if 0 <= nx < N and 0 <= ny < len(grid[nx]) and grid[nx][ny] == 'E' and (nx, ny) not in visited:
                        if (nx, ny) == target:
                            return distance + 1  # Return the distance if target is reached
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            distance += 1  # Increment distance after exploring all nodes at the current distance
        return -1  # Target not reachable
    results = []
    for s_x, s_y, t_x, t_y in queries:
        # Validate query indices
        if (0 <= s_x < N and 0 <= s_y < len(grid[s_x]) and grid[s_x][s_y] == 'E' and
            0 <= t_x < N and 0 <= t_y < len(grid[t_x]) and grid[t_x][t_y] == 'E'):
            result = bfs((s_x, s_y), (t_x, t_y))
        else:
            result = -1  # Invalid starting or target cell
        results.append(result)
    return results