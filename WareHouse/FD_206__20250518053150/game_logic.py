'''
Game logic for determining the winner based on intervals.
'''
from typing import List, Tuple
def is_non_intersecting(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> bool:
    """
    Check if two intervals do not intersect.
    """
    return interval1[1] <= interval2[0] or interval2[1] <= interval1[0]
def find_winner(intervals: List[Tuple[int, int]]) -> str:
    """
    Determine the winner based on the optimal play strategy for Alice and Bob.
    """
    if len(intervals) == 0:
        return "Invalid Test Case: No intervals"
    elif len(intervals) == 1:
        return "Alice"  # Alice wins if there's only one interval
    intervals.sort()  # Sort intervals based on starting point
    chosen_intervals = []
    last_end = -1
    for interval in intervals:
        if last_end <= interval[0]:  # Non-intersecting condition
            chosen_intervals.append(interval)
            last_end = interval[1]
    return "Alice" if len(chosen_intervals) % 2 == 1 else "Bob"
def determine_winner(T: int, intervals_list: List[List[Tuple[int, int]]]) -> List[str]:
    """
    Determines the winner for each test case based on the intervals provided.
    Parameters:
    intervals_list (List[List[Tuple[int, int]]]): A list containing lists of tuples of intervals for each test case.
    Returns:
    List[str]: A list of strings indicating the winner for each test case.
    """
    results = []
    for intervals in intervals_list:
        if len(intervals) == 0:
            results.append("Invalid Test Case: No intervals")
            continue
        winner = find_winner(intervals)
        results.append(winner)
    return results