'''
Pathfinding logic for the Candy Collector game.
'''
from typing import List, Tuple
from collections import deque
def canReachGoal(H: int, W: int, T: int, grid: List[List[str]]) -> Tuple[bool, int]:
    start = None
    goal = None
    candies = []
    # Locate 'S', 'G', and 'o' in the grid
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)
            elif grid[i][j] == 'o' and len(candies) < 18:  # Limit to 18 candies
                candies.append((i, j))
    if not start or not goal:
        return (False, 0)  # Return false if start or goal is missing
    # BFS setup
    queue = deque([(start[0], start[1], 0, set())])  # (x, y, moves, collected_candies)
    visited = set()
    visited.add((start[0], start[1], frozenset()))  # Track position and collected candies
    max_candies = 0
    goal_reached = False
    while queue:
        x, y, moves, collected_candies = queue.popleft()
        # If we exceed the number of moves, skip
        if moves >= T:
            continue
        # Explore adjacent squares
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#':  # Not a wall
                new_collected_candies = set(collected_candies)  # Copy the set of collected candies
                if grid[nx][ny] == 'o':
                    new_collected_candies.add((nx, ny))  # Add candy to the set
                # Ensure we do not exceed 18 unique candies
                if len(new_collected_candies) <= 18 and (nx, ny, frozenset(new_collected_candies)) not in visited:
                    visited.add((nx, ny, frozenset(new_collected_candies)))
                    queue.append((nx, ny, moves + 1, new_collected_candies))
                    # Check if we reached the goal
                    if (nx, ny) == goal and moves + 1 <= T:
                        goal_reached = True
                        max_candies = max(max_candies, len(new_collected_candies))
    return goal_reached, max_candies