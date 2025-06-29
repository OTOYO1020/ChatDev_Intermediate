'''
Module for simulating the walking distance based on blocked intervals.
'''
def find_distance(D_i, blocked_intervals):
    """
    Determines the distance a person can walk before encountering a blocked point.
    Parameters:
    D_i (int): The starting time of the person.
    blocked_intervals (dict): A dictionary where keys are coordinates and values are lists of blocked time intervals.
    Returns:
    int: The distance walked before encountering a blocked point or the maximum coordinate if no blocks exist.
    """
    if not blocked_intervals:  # Check if there are no blocked intervals
        return float('inf')  # Return infinity if there are no blocks encountered
    max_coordinate = max(blocked_intervals.keys())  # Track the maximum coordinate
    last_end_time = -1  # Variable to track the end time of the last blocked interval
    for X_i in sorted(blocked_intervals.keys()):
        for S_i, T_i in blocked_intervals[X_i]:
            last_end_time = max(last_end_time, T_i)  # Update the last end time
            if D_i < S_i:  # If the person starts before the blocked interval starts
                return X_i  # The distance walked is the coordinate of the blocked point
            if S_i <= D_i < T_i:  # If the person starts during the blocked interval
                return X_i  # The distance walked is the coordinate of the blocked point
    # If the person's starting time is greater than or equal to the end of the last blocked interval
    if D_i >= last_end_time:
        return max_coordinate  # Return max_coordinate if all intervals are passed
    return max_coordinate  # Return max_coordinate if all intervals are passed