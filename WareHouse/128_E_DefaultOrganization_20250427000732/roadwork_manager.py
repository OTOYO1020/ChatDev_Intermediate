'''
Module for managing roadworks and blocked intervals.
'''
def populate_blocked_intervals(roadworks):
    blocked_intervals = {}
    for X_i, S_i, T_i in roadworks:
        if X_i not in blocked_intervals:
            blocked_intervals[X_i] = []
        blocked_intervals[X_i].append((S_i, T_i))
    # Sort and merge intervals for each coordinate
    for key in blocked_intervals:
        blocked_intervals[key] = merge_intervals(blocked_intervals[key])
    return blocked_intervals
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping intervals
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged