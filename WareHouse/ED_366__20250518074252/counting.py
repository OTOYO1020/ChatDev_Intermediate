'''
Module for counting integer pairs based on Manhattan distance.
'''
from typing import List, Tuple
def count_integer_pairs(N: int, D: int, points: List[Tuple[int, int]]) -> int:
    # Determine the minimum and maximum x and y coordinates from the points
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    valid_pairs_count = 0
    # Iterate through all possible integer values of x and y within the defined range
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            # Calculate the total Manhattan distance for the current (x, y)
            total_distance = sum(abs(x - x_i) + abs(y - y_i) for (x_i, y_i) in points)
            # Count the pairs where the total distance is less than or equal to D
            if total_distance <= D:
                valid_pairs_count += 1
    return valid_pairs_count