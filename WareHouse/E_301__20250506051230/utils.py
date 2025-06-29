'''
Utility functions for pathfinding algorithms.
'''
from collections import deque
def bfs(start, goal, grid, T):
    '''
    Perform breadth-first search to determine if the goal can be reached within T moves
    while counting the number of candies collected along the path.
    '''
    if start == goal:
        return 0 if T >= 0 else -1  # If start is the same as goal, return 0 candies collected if T is non-negative
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, 0, 0)])  # (position, moves, candies_collected)
    visited = set()  # Track visited nodes
    visited.add(start)  # Mark the start position as visited
    max_candies = -1  # Initialize max candies to -1
    while queue:
        (current_x, current_y), moves, candies = queue.popleft()
        # If we exceed the allowed moves, skip this path
        if moves > T:
            continue
        # Check if we have reached the goal
        if (current_x, current_y) == goal:
            if moves <= T:
                max_candies = max(max_candies, candies)  # Update max candies when goal is reached
        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            new_x, new_y = current_x + dx, current_y + dy
            # Check bounds and wall conditions
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != '#':  # Not a wall
                new_candies = candies + (1 if grid[new_x][new_y] == 'o' else 0)
                new_position = (new_x, new_y)
                # Only add to queue if not visited
                if new_position not in visited:
                    visited.add(new_position)  # Mark as visited
                    queue.append(((new_x, new_y), moves + 1, new_candies))
    return max_candies if max_candies != -1 else -1  # Return max candies or -1 if unreachable
def can_reach_goal(start, goal, T, grid):
    '''
    Check if the goal can be reached from the start within T moves.
    '''
    # Check if start or goal is on a wall
    if grid[start[0]][start[1]] == '#' or grid[goal[0]][goal[1]] == '#':
        return -1  # Cannot start or end on a wall
    if start == goal:
        return 0 if T >= 0 else -1  # If start is the same as goal, return 0 candies collected if T is non-negative
    # Preliminary check for minimum required moves
    min_moves = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
    if min_moves > T:
        return -1  # Not enough moves to reach the goal
    return bfs(start, goal, grid, T)  # Pass grid to bfs