'''
Class for calculating the Manhattan distances based on grid dimensions and pieces.
'''
from combinatorics import Combinatorics
class DistanceCalculator:
    MOD = 10**9 + 7
    def __init__(self, n, m, k):
        self.n = n
        self.m = m
        self.k = k
        self.combinatorics = Combinatorics(n * m, self.MOD)
    def calculate_distance(self):
        total_distance = 0
        # Calculate row distances
        row_distance = self.calculate_row_distance()
        total_distance += row_distance
        # Calculate column distances
        column_distance = self.calculate_column_distance()
        total_distance += column_distance
        return total_distance % self.MOD
    def calculate_row_distance(self):
        distance = 0
        for i in range(self.n):
            # Contribution of distances for all pairs in the same row
            for j in range(self.m):
                distance += j * (self.m - j - 1)  # Each column contributes to the distance based on its index
        return distance * self.combinatorics.combination(self.n, self.k - 2) % self.MOD  # Adjust for row combinations
    def calculate_column_distance(self):
        distance = 0
        for j in range(self.m):
            # Contribution of distances for all pairs in the same column
            for i in range(self.n):
                distance += i * (self.n - i - 1)  # Each row contributes to the distance based on its index
        return distance * self.combinatorics.combination(self.m, self.k - 2) % self.MOD  # Adjust for column combinations