'''
Helper functions for calculating distances and permutations.
'''
import itertools
import math
def euclidean_distance(x1, y1, x2, y2):
    '''
    Calculate the Euclidean distance between two points.
    '''
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def get_permutations(towns):
    '''
    Generate all permutations of the towns.
    '''
    return itertools.permutations(towns)
def is_chest_on_path(start, end, chest, threshold=1.0):
    '''
    Check if the chest is on the path from start to end within a given threshold.
    '''
    # Calculate the distance from the chest to the line segment defined by start and end
    start_to_end = (end[0] - start[0], end[1] - start[1])
    start_to_chest = (chest[0] - start[0], chest[1] - start[1])
    segment_length_squared = start_to_end[0] ** 2 + start_to_end[1] ** 2
    if segment_length_squared == 0:
        # Start and end are the same point
        return euclidean_distance(start[0], start[1], chest[0], chest[1]) <= threshold
    # Calculate the projection of start_to_chest onto start_to_end
    t = (start_to_chest[0] * start_to_end[0] + start_to_chest[1] * start_to_end[1]) / segment_length_squared
    t = max(0, min(1, t))  # Clamp t to the range [0, 1]
    # Find the closest point on the segment to the chest
    closest_point = (start[0] + t * start_to_end[0], start[1] + t * start_to_end[1])
    # Check if the distance from the closest point to the chest is within the threshold
    return euclidean_distance(closest_point[0], closest_point[1], chest[0], chest[1]) <= threshold