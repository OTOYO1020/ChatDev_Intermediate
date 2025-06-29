'''
Module containing transformation functions to check if one set of points can be transformed into another.
'''
from typing import List, Tuple
import math
def canTransform(S: List[Tuple[int, int]], T: List[Tuple[int, int]]) -> bool:
    if len(S) != len(T) or len(S) == 0:  # Check for empty or unequal sets
        return False
    T_set = set(T)  # Convert T to a set for faster lookup
    for angle in range(0, 361):  # Include 360 degrees
        rotated_S = [rotate(point, angle) for point in S]
        for s_point in rotated_S:
            # Calculate translation based on each point of T
            for t_point in T:
                q, r = t_point[0] - s_point[0], t_point[1] - s_point[1]
                translated_S = {translate(point, q, r) for point in rotated_S}
                # Check if all points in T can be matched with the translated points
                if T_set.issubset(translated_S):
                    return True
    return False
def rotate(point: Tuple[int, int], angle: float) -> Tuple[float, float]:
    '''
    Rotate a point by a given angle around the origin.
    '''
    radians = math.radians(angle)  # Convert angle to radians
    x_new = point[0] * math.cos(radians) - point[1] * math.sin(radians)
    y_new = point[0] * math.sin(radians) + point[1] * math.cos(radians)
    return (x_new, y_new)  # Return exact float values without rounding
def translate(point: Tuple[int, int], q: float, r: float) -> Tuple[float, float]:
    '''
    Translate a point by q in the x-direction and r in the y-direction.
    '''
    return (point[0] + q, point[1] + r)