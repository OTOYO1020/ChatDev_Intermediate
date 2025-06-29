'''
Computation module for calculating the maximum number of visible 7's.
'''
from typing import List, Tuple
from itertools import combinations
def max_visible_sevens(N: int, coordinates: List[Tuple[int, int]]) -> int:
    if N == 0:
        return 0
    max_visible_count = 0
    # Check combinations of size 1 to N
    for r in range(1, N + 1):
        for combo in combinations(coordinates, r):
            visible_count = 0
            # Check visibility for each point in the combination
            for point in combo:
                if is_visible((0, 0), point, [p for p in combo if p != point]):
                    visible_count += 1
            # Update max visible count if the current combination is better
            max_visible_count = max(max_visible_count, visible_count)
    return max_visible_count
def is_visible(origin: Tuple[int, int], point: Tuple[int, int], other_points: List[Tuple[int, int]]) -> bool:
    # Check if the quadrilateral formed by the origin and the point intersects with any other point
    for other_point in other_points:
        if intersects(origin, point, other_point, (0, 0)):
            return False  # If any intersection occurs, the point is not visible
    return True  # If no intersections, the point is visible
def intersects(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int], p4: Tuple[int, int]) -> bool:
    # Check if line segments p1p2 and p3p4 intersect
    def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> int:
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # collinear
        return 1 if val > 0 else 2  # clock or counterclockwise
    o1 = orientation(p1, p2, p3)
    o2 = orientation(p1, p2, p4)
    o3 = orientation(p3, p4, p1)
    o4 = orientation(p3, p4, p2)
    # General case
    if o1 != o2 and o3 != o4:
        return True
    # Special Cases
    if o1 == 0 and on_segment(p1, p2, p3):
        return True
    if o2 == 0 and on_segment(p1, p2, p4):
        return True
    if o3 == 0 and on_segment(p3, p4, p1):
        return True
    if o4 == 0 and on_segment(p3, p4, p2):
        return True
    return False  # Doesn't fall in the general case
def on_segment(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> bool:
    # Check if point r lies on segment pq
    return (min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and
            min(p[1], q[1]) <= r[1] <= max(p[1], q[1]))