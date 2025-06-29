'''
Module for calculating Santa's final position and distinct houses visited.
'''
from typing import List, Tuple
import math
def bresenham(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    if dx > dy:
        err = dx / 2.0
        while x1 != x2:
            points.append((x1, y1))
            err -= dy
            if err < 0:
                y1 += sy
                err += dx
            x1 += sx
    else:
        err = dy / 2.0
        while y1 != y2:
            points.append((x1, y1))
            err -= dx
            if err < 0:
                x1 += sx
                err += dy
            y1 += sy
    points.append((x2, y2))  # Include the endpoint
    return points
def find_final_position_and_houses(N: int, houses: List[Tuple[int, int]], M: int, movements: List[Tuple[str, int]], S: Tuple[int, int]) -> Tuple[Tuple[int, int], int]:
    """
    Calculate Santa's final position and the number of distinct houses visited.
    Parameters:
    N (int): Number of houses.
    houses (List[Tuple[int, int]]): List of house coordinates.
    M (int): Number of movements.
    movements (List[Tuple[str, int]]): List of movement instructions.
    S (Tuple[int, int]): Starting position of Santa.
    Returns:
    Tuple[Tuple[int, int], int]: Final position of Santa and count of distinct houses visited.
    """
    distinct_houses = set()
    current_position = S
    house_set = set(houses)
    for direction, distance in movements:
        new_position = current_position
        # Calculate new position based on direction
        if direction == 'U':
            new_position = (current_position[0], current_position[1] + distance)
        elif direction == 'D':
            new_position = (current_position[0], current_position[1] - distance)
        elif direction == 'L':
            new_position = (current_position[0] - distance, current_position[1])
        elif direction == 'R':
            new_position = (current_position[0] + distance, current_position[1])
        elif direction in ['UR', 'UL', 'DR', 'DL']:
            dx = round(distance / math.sqrt(2))  # Round to nearest integer
            dy = round(distance / math.sqrt(2))  # Round to nearest integer
            if direction == 'UR':
                new_position = (current_position[0] + dx, current_position[1] + dy)
            elif direction == 'UL':
                new_position = (current_position[0] - dx, current_position[1] + dy)
            elif direction == 'DR':
                new_position = (current_position[0] + dx, current_position[1] - dy)
            elif direction == 'DL':
                new_position = (current_position[0] - dx, current_position[1] - dy)
        # Check all points in the movement path
        points = bresenham(current_position[0], current_position[1], new_position[0], new_position[1])
        for (x, y) in points:
            if (x, y) in house_set:
                distinct_houses.add((x, y))
        current_position = new_position  # Update position after checking houses
    return current_position, len(distinct_houses)