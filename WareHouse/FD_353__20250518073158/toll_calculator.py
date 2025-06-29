'''
Module for calculating the minimum toll based on tile types.
'''
from collections import deque
def minimum_toll(K: int, S_x: int, S_y: int, T_x: int, T_y: int) -> int:
    '''
    Calculate the minimum toll required for Takahashi to move from the start point to the target point.
    Parameters:
    K (int): The size of the tiles.
    S_x (int): The starting x-coordinate.
    S_y (int): The starting y-coordinate.
    T_x (int): The target x-coordinate.
    T_y (int): The target y-coordinate.
    Returns:
    int: The total toll paid upon reaching the target point.
    '''
    if (S_x, S_y) == (T_x, T_y):
        return 0  # No toll if starting point is the same as target point
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Right, Left, Down, Up
    queue = deque([(S_x, S_y, get_tile_type(S_x, S_y, K), 0)])  # (x, y, current_tile_type, toll_count)
    visited = set((S_x, S_y))
    min_toll = float('inf')  # Initialize minimum toll as infinity
    while queue:
        x, y, current_tile_type, toll_count = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) == (T_x, T_y):
                next_tile_type = get_tile_type(nx, ny, K)
                if next_tile_type != current_tile_type:
                    min_toll = min(min_toll, toll_count + 1)  # Update minimum toll if crossing tile boundary
                else:
                    min_toll = min(min_toll, toll_count)  # No toll if not crossing tile boundary
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                next_tile_type = get_tile_type(nx, ny, K)
                new_toll_count = toll_count + (1 if next_tile_type != current_tile_type else 0)
                queue.append((nx, ny, next_tile_type, new_toll_count))
    return min_toll if min_toll != float('inf') else -1  # Return the minimum toll found
def get_tile_type(i: int, j: int, K: int) -> str:
    '''
    Determine the type of tile at given coordinates.
    Parameters:
    i (int): The x-coordinate.
    j (int): The y-coordinate.
    K (int): The size of the tiles.
    Returns:
    str: 'small' if the tile is small, 'large' if the tile is large.
    '''
    tile_type = (i // K) + (j // K)
    return 'small' if tile_type % 2 == 0 else 'large'