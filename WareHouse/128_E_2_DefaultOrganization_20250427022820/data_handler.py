'''
Data handling functions for the Roadwork Distance Calculator.
'''
import bisect
def merge_intervals(intervals):
    """
    Merges overlapping or contiguous time intervals.
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])  # Sort intervals by start time
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping intervals
            merged[-1] = (last[0], max(last[1], current[1]))  # Merge intervals
        else:
            merged.append(current)  # No overlap, add current interval
    return merged
def find_distance(D_i, blocked_intervals):
    """
    Finds the distance a person can walk before encountering a blocked point.
    """
    if not blocked_intervals:  # Check if there are no blocked intervals
        return None  # Indicate that the person can walk indefinitely
    for x in sorted(blocked_intervals.keys()):
        intervals = blocked_intervals[x]
        start_times = [start for start, end in intervals]
        # If D_i is less than the start of the first interval, return the coordinate
        if D_i < intervals[0][0]:
            return x
        index = bisect.bisect_right(start_times, D_i)  # Find the rightmost interval start time
        # Check if D_i falls within the last checked interval
        if index > 0:
            start, end = intervals[index - 1]
            if D_i >= start and D_i <= end:  # Check if within the interval
                return x  # Blocked at this coordinate
            # Additional check for the case where D_i equals the end of the last interval
            if D_i == end:
                return x  # Blocked at this coordinate
        # If D_i is greater than the end of the last interval, continue checking
        if index == len(intervals):
            distance = x  # Update distance to the last coordinate checked
    # Return None to indicate that the person can walk indefinitely
    return None  # Indicate that the person can walk indefinitely
def populate_blocked_intervals(roadworks):
    """
    Populates the blocked intervals dictionary from the list of roadworks.
    """
    blocked_intervals = {}
    for X_i, S_i, T_i in roadworks:
        if S_i > T_i:
            raise ValueError(f"Invalid interval: Start time {S_i} cannot be greater than end time {T_i}.")
        if X_i not in blocked_intervals:
            blocked_intervals[X_i] = []
        blocked_intervals[X_i].append((S_i, T_i))
    # Merge intervals for each coordinate
    for x in blocked_intervals:
        blocked_intervals[x] = merge_intervals(blocked_intervals[x])
    return blocked_intervals