'''
Movement logic for calculating the minimum moves for Takahashi.
'''
from collections import deque
def min_moves(s_x, s_y, g_x, g_y, obstacles, grid_width, grid_height):
    # Check if starting position is the same as goal position
    if (s_x, s_y) == (g_x, g_y):
        return 0
    # Create a set for obstacles for O(1) access
    obstacle_set = set(obstacles)
    # Directions for movement: up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # BFS initialization
    queue = deque([(s_x, s_y, 0)])  # (current_x, current_y, moves)
    visited = set()
    visited.add((s_x, s_y))
    while queue:
        x, y, moves = queue.popleft()
        # Check if we reached the goal
        if (x, y) == (g_x, g_y):
            return moves
        for dx, dy in directions:
            nx, ny = x, y
            # Move in the direction until hitting an obstacle or boundary
            while (1 <= nx + dx <= grid_width) and (1 <= ny + dy <= grid_height) and (nx + dx, ny + dy) not in obstacle_set:
                nx += dx
                ny += dy
            # After exiting the loop, check if we can add the last valid position (nx, ny)
            if (nx, ny) != (s_x, s_y) and (1 <= nx <= grid_width) and (1 <= ny <= grid_height):
                # Only add to queue if not visited
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))
    return -1  # If the goal is unreachable