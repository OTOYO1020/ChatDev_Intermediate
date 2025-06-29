'''
Module for counting students based on height queries.
'''
from bisect import bisect_left
def count_students_with_min_height(heights, queries):
    """
    Counts the number of students with height at least for each query.
    Parameters:
    heights (list of int): List of student heights.
    queries (list of int): List of height queries.
    Returns:
    list of int: Number of students meeting each height requirement.
    """
    if not heights:  # Check for empty heights list
        return [0] * len(queries)  # Return a list of zeros for each query
    heights.sort()  # Sort the heights for binary search
    results = []
    for query in queries:
        index = bisect_left(heights, query)  # Find the first index where height >= query
        count = len(heights) - index  # Count of students with height >= query
        results.append(count)
    return results