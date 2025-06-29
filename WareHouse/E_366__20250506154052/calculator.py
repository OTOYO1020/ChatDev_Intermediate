'''
Module for calculating valid integer pairs based on points and distance D.
'''
def calculate_valid_pairs(point_counts, D):
    """
    Calculate the number of valid integer pairs (x, y) such that the total distance
    from all points to (x, y) is less than or equal to D.
    Parameters:
    point_counts (Counter): A Counter object with points as keys and their frequencies as values.
    D (int): The maximum allowable total distance.
    Returns:
    int: The count of valid integer pairs (x, y).
    """
    unique_points = list(point_counts.keys())
    min_x = min(point[0] for point in unique_points)
    max_x = max(point[0] for point in unique_points)
    min_y = min(point[1] for point in unique_points)
    max_y = max(point[1] for point in unique_points)
    count = 0
    # Iterate through the range of possible x and y values
    for x in range(min_x - D, max_x + D + 1):
        for y in range(min_y - D, max_y + D + 1):
            # Calculate the total Manhattan distance from (x, y) to all unique points
            total_distance = sum(abs(x - point[0]) + abs(y - point[1]) for point in unique_points)
            if total_distance <= D:  # Check if total distance is within the allowed range
                count += 1
    return count