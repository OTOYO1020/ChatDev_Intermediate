'''
Contains the game logic for counting ice squares and moving the player.
'''
from typing import List, Tuple
def move_player(direction: str, current_position: Tuple[int, int]) -> Tuple[int, int]:
    '''
    Determines the new position of the player based on the specified direction.
    Parameters:
    direction (str): The direction to move ('up', 'down', 'left', 'right').
    current_position (Tuple[int, int]): The current position of the player.
    Returns:
    Tuple[int, int]: The new position of the player after moving.
    '''
    x, y = current_position
    if direction == "up":
        return (x - 1, y)
    elif direction == "down":
        return (x + 1, y)
    elif direction == "left":
        return (x, y - 1)
    elif direction == "right":
        return (x, y + 1)
    return current_position
def count_ice_squares(N: int, M: int, grid: List[str]) -> int:
    '''
    Counts the number of unique ice squares touched by the player.
    Parameters:
    N (int): The number of rows in the grid.
    M (int): The number of columns in the grid.
    grid (List[str]): A list of strings representing the grid.
    Returns:
    int: The total number of unique ice squares touched by the player.
    '''
    visited = set()
    # Dynamically find a valid starting position
    starting_position_found = False
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'I':
                current_position = (i, j)
                starting_position_found = True
                break
        if starting_position_found:
            break
    if not starting_position_found:
        print("No valid ice position found! Exiting.")
        return 0
    visited.add(current_position)
    print("Starting position:", current_position)
    print("Grid:")
    for row in grid:
        print(row)
    print("Instructions: Enter direction (up, down, left, right) or 'exit' to stop.")
    while True:
        direction = input("Enter direction: ")
        if direction == 'exit':
            break
        if direction not in ["up", "down", "left", "right"]:
            print("Invalid direction! Please enter 'up', 'down', 'left', or 'right'.")
            continue
        new_position = move_player(direction, current_position)
        # Check for out of bounds
        if 0 <= new_position[0] < N and 0 <= new_position[1] < M:
            if grid[new_position[0]][new_position[1]] == 'I':
                visited.add(new_position)
                current_position = new_position
            elif grid[new_position[0]][new_position[1]] == 'R':
                print("Hit a rock! Stopping movement.")
                break
        else:
            print("Out of bounds! Stopping movement.")
            break
    return len(visited)