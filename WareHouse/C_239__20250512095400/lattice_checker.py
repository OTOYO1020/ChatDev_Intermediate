'''
This module contains the function to check for lattice points
at a distance of sqrt(5) from two given points.
'''
def is_lattice_point_distance_sqrt5(x1: int, y1: int, x2: int, y2: int) -> bool:
    # Calculate the maximum range needed based on the coordinates of both points
    range_limit = int(2.5)  # Adjusted to be more dynamic based on distance requirement
    min_x = min(x1, x2) - range_limit
    max_x = max(x1, x2) + range_limit
    min_y = min(y1, y2) - range_limit
    max_y = max(y1, y2) + range_limit
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            # Calculate squared distances to both points
            dist1 = (x - x1) ** 2 + (y - y1) ** 2
            dist2 = (x - x2) ** 2 + (y - y2) ** 2
            # Check if both distances equal 5
            if dist1 == 5 and dist2 == 5:
                return True
    return False