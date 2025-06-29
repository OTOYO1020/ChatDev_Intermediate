'''
Module for calculating the minimum square side length based on point coordinates.
'''
from typing import List, Tuple
def min_square_side(N: int, K: int, points: List[Tuple[int, int]]) -> int:
    # Calculate the minimum and maximum x and y coordinates
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    # Calculate total distances to align all points to min_x and min_y
    total_distance_x = sum(abs(point[0] - min_x) for point in points)
    total_distance_y = sum(abs(point[1] - min_y) for point in points)
    # Check if we can align all points within K operations
    if total_distance_x <= K and total_distance_y <= K:
        return 0
    # Calculate the optimal target coordinates (medians)
    sorted_x = sorted(point[0] for point in points)
    sorted_y = sorted(point[1] for point in points)
    # Median calculation
    median_x = sorted_x[N // 2]
    median_y = sorted_y[N // 2]
    # Calculate distances to move to the median
    total_distance_x = sum(abs(point[0] - median_x) for point in points)
    total_distance_y = sum(abs(point[1] - median_y) for point in points)
    # Check if we can align all points to the median within K operations
    if total_distance_x <= K and total_distance_y <= K:
        return 0
    # Calculate the remaining operations after aligning to the median
    remaining_x = K - total_distance_x
    remaining_y = K - total_distance_y
    # Calculate the new min and max based on the remaining operations
    new_min_x = min_x
    new_max_x = max_x
    new_min_y = min_y
    new_max_y = max_y
    if total_distance_x > K:
        # Cannot align to median, use original min/max
        new_min_x = min_x
        new_max_x = max_x
    else:
        if remaining_x > 0:
            new_min_x = min_x - remaining_x
            new_max_x = max_x + remaining_x
    if total_distance_y > K:
        # Cannot align to median, use original min/max
        new_min_y = min_y
        new_max_y = max_y
    else:
        if remaining_y > 0:
            new_min_y = min_y - remaining_y
            new_max_y = max_y + remaining_y
    # Calculate the side length of the square
    side_length = max(new_max_x - new_min_x, new_max_y - new_min_y)
    return side_length