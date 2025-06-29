'''
Utility functions for the Student Height Query application.
'''
def count_students(sorted_heights, query_height):
    """
    Count the number of students with height at least query_height using binary search.
    """
    if not sorted_heights:  # Check if the list is empty
        return 0
    low, high = 0, len(sorted_heights)
    while low < high:
        mid = (low + high) // 2
        if sorted_heights[mid] < query_height:
            low = mid + 1
        else:
            high = mid
    return len(sorted_heights) - low