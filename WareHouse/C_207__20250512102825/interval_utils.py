'''
Utility functions for counting intersecting intervals.
'''
from typing import List, Tuple
def count_intersecting_intervals(N: int, intervals: List[Tuple[int, int, int]]) -> int:
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if do_intervals_intersect(intervals[i], intervals[j]):
                count += 1
    return count
def do_intervals_intersect(interval1: Tuple[int, int, int], interval2: Tuple[int, int, int]) -> bool:
    t1, l1, r1 = interval1
    t2, l2, r2 = interval2
    # Check for intersection based on interval types
    if t1 == 1 and t2 == 1:  # Both closed
        return not (r1 < l2 or r2 < l1)
    elif t1 == 2 and t2 == 2:  # Both open
        return not (r1 < l2 + 1 or r2 + 1 < l1)
    elif t1 == 1 and t2 == 2:  # First closed, second open
        return not (r1 < l2 + 1 or r2 < l1)
    elif t1 == 2 and t2 == 1:  # First open, second closed
        return not (r1 + 1 < l2 or r2 < l1)