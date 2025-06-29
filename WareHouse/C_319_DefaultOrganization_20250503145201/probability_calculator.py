'''
Utility class for calculating the probability of not getting disappointed.
'''
class ProbabilityCalculator:
    def __init__(self, disappointment_count, total_permutations):
        self.disappointment_count = disappointment_count
        self.total_permutations = total_permutations
    def calculate(self):
        if self.total_permutations == 0:
            return 0.0
        return 1 - (self.disappointment_count / self.total_permutations)