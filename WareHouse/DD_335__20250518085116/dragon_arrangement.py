'''
Module for arranging dragon parts on a grid.
'''
from typing import List, Tuple
def arrange_dragon_parts(N: int) -> List[Tuple[int, int]]:
    '''
    Arranges dragon parts on an N x N grid, starting from the center.
    Parameters:
    N (int): The size of the grid.
    Returns:
    List[Tuple[int, int]]: A list of positions where dragon parts are placed.
    '''
    grid = [[None for _ in range(N)] for _ in range(N)]
    center = (N // 2, N // 2)
    grid[center[0]][center[1]] = 'T'  # Place Takahashi at the center
    current_position = center
    positions = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_index = 0
    steps = 1
    for x in range(2, N * N + 1):
        placed = False  # Flag to check if the current dragon part is placed
        for _ in range(2):  # Two times for each step count
            for _ in range(steps):
                next_position = (current_position[0] + directions[dir_index][0],
                                 current_position[1] + directions[dir_index][1])
                if (0 <= next_position[0] < N and 0 <= next_position[1] < N and
                        grid[next_position[0]][next_position[1]] is None):
                    grid[next_position[0]][next_position[1]] = x
                    positions.append(next_position)
                    current_position = next_position
                    placed = True  # Mark as placed
                    break  # Break out of the steps loop to place the next dragon part
            if placed:
                break  # If placed, break out of the direction loop
            dir_index = (dir_index + 1) % 4  # Change direction
        if not placed:  # If not placed, we need to try the next direction
            dir_index = (dir_index + 1) % 4  # Change direction again
        steps += 1  # Increase the step count after completing a full cycle
    return positions