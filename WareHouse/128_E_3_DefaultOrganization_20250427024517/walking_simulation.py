'''
Module to simulate walking and calculate distances based on blocked intervals.
'''
def find_distance(D, blocked_intervals):
    distance = 0
    last_coordinate = max(blocked_intervals.keys()) if blocked_intervals else 0
    # Check if there are no blocked intervals
    if not blocked_intervals:
        return last_coordinate
    # Iterate through sorted blocked intervals
    for X in sorted(blocked_intervals.keys()):
        intervals = blocked_intervals[X]
        # If D is less than the start of the first interval, return the current coordinate
        if D < intervals[0][0]:
            return X
        for S, T in intervals:
            if D < S:  # Not blocked yet
                return X  # Return the current coordinate as distance
            if S <= D <= T:  # Blocked
                return distance  # Return the last distance before being blocked
            distance = X  # Update distance to the current coordinate if not blocked
    # If all intervals are checked and no blocks encountered, return the last distance
    if D > intervals[-1][1]:  # If D is greater than the end of the last interval
        return last_coordinate  # Ensure to return the last coordinate
    return distance