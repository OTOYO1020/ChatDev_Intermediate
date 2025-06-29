'''
DistanceChecker class to validate painting conditions.
'''
class DistanceChecker:
    def __init__(self, distances):
        self.distances = distances
    def check_conditions(self, pairs):
        for p, d in pairs:
            if p in self.distances and self.distances[p] > d:
                return False
        return True