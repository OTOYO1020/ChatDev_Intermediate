'''
Module for calculating the minimum absolute difference between two sums of weights.
'''
class WeightCalculator:
    def __init__(self, weights):
        self.weights = weights
    def calculate_min_difference(self):
        N = len(self.weights)
        total_sum = sum(self.weights)
        min_difference = float('inf')
        # Iterate Over Possible Divisions
        for T in range(1, N):  # T should range from 1 to N-1
            # Calculate Sums for Each Division
            S1 = sum(self.weights[:T])  # S1 is the sum of weights from index 0 to T-1 (1-based index)
            S2 = total_sum - S1  # S2 is the sum of weights from index T to N-1 (1-based index)
            # Compute Absolute Difference
            difference = abs(S1 - S2)
            # Update Minimum Difference
            if difference < min_difference:
                min_difference = difference
        return min_difference