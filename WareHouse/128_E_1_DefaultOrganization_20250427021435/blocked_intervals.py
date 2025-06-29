'''
Module to manage blocked intervals for roadworks.
'''
class BlockedIntervals:
    def __init__(self):
        self.blocked_intervals = {}
    def populate_intervals(self, roadworks):
        for x, s, t in roadworks:
            if x not in self.blocked_intervals:
                self.blocked_intervals[x] = []
            self.blocked_intervals[x].append((s, t))
        for x in self.blocked_intervals:
            self.blocked_intervals[x].sort(key=lambda interval: interval[0])
            self.blocked_intervals[x] = self.merge_intervals(self.blocked_intervals[x])
    def merge_intervals(self, intervals):
        merged = []
        for current in intervals:
            if not merged or merged[-1][1] < current[0]:
                merged.append(current)
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
        return merged
    def get_blocked_intervals(self):
        return self.blocked_intervals