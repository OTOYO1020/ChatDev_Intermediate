'''
Module to handle blocked intervals for roadworks.
'''
def populate_blocked_intervals(roadworks):
    blocked_intervals = {}
    for X, S, T in roadworks:
        if X not in blocked_intervals:
            blocked_intervals[X] = []
        blocked_intervals[X].append((S, T))
    for X in blocked_intervals:
        blocked_intervals[X] = merge_intervals(blocked_intervals[X])
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