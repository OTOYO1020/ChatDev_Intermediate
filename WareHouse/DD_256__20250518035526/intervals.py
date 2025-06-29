'''
Module for processing intervals and merging them.
'''
from typing import List, Tuple
def union_intervals(N: int, intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    '''
    Function to merge overlapping intervals.
    '''
    if N == 0 or not intervals:  # Check for empty intervals list
        return []
    # Sort the intervals based on the starting point
    intervals.sort(key=lambda x: x[0])
    result = []
    # Initialize the first interval
    current_start, current_end = intervals[0]
    for i in range(1, N):
        start, end = intervals[i]
        if start <= current_end:  # Overlapping intervals
            current_end = max(current_end, end)  # Merge intervals
        else:
            result.append((current_start, current_end))  # Add the previous interval
            current_start, current_end = start, end  # Move to the next interval
    # Add the last interval
    result.append((current_start, current_end))
    return result