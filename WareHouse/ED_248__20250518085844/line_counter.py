'''
Module for counting unique lines formed by points.
'''
from typing import List, Tuple, Union
from collections import defaultdict, Counter
def count_lines(N: int, K: int, points: List[Tuple[int, int]]) -> Union[int, str]:
    if N == 0:
        return 0  # Handle empty points list
    if K > N:
        raise ValueError("K cannot be greater than N.")  # Raise an error instead of returning a string
    if N < 2:
        return 0  # Not enough points to form a line
    # Remove duplicate points and count occurrences
    points_counter = Counter(points)
    points = list(points_counter.keys())
    N = len(points)  # Update N after removing duplicates
    # Check if all points are collinear
    def are_all_collinear(points):
        if len(points) < 3:
            return True
        (x0, y0), (x1, y1) = points[0], points[1]
        for x, y in points[2:]:
            # Check collinearity using cross product
            if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
                return False
        return True
    if are_all_collinear(points):
        return "Infinity"
    lines = defaultdict(set)
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2:  # Vertical line
                slope = None  # Use None to indicate vertical line
                intercept = x1
            else:
                slope = (y2 - y1) / (x2 - x1)
                intercept = y1 - slope * x1
            lines[(slope, intercept)].add(i)
            lines[(slope, intercept)].add(j)
    # Count unique lines that have K or more points
    count = 0
    for line in lines.values():
        total_points_on_line = sum(points_counter[points[i]] for i in line)
        if total_points_on_line >= K:
            count += 1
    return count