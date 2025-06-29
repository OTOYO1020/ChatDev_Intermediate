'''
DistanceCalculator class for computing Manhattan distances.
'''
from utils import mod_inverse
MOD = 10**9 + 7
class DistanceCalculator:
    def __init__(self, N, M, K):
        self.N = N
        self.M = M
        self.K = K
        self.fact = []
        self.inv_fact = []
        self.precalculate_combinations()
    def precalculate_combinations(self):
        max_n = self.N * self.M
        self.fact = [1] * (max_n + 1)
        self.inv_fact = [1] * (max_n + 1)
        for i in range(2, max_n + 1):
            self.fact[i] = self.fact[i - 1] * i % MOD
        self.inv_fact[max_n] = mod_inverse(self.fact[max_n], MOD)
        for i in range(max_n - 1, 0, -1):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % MOD
    def calculate_distance_cost(self):
        row_cost = self.calculate_row_cost()
        col_cost = self.calculate_col_cost()
        total_cost = (row_cost + col_cost) % MOD
        return total_cost
    def calculate_row_cost(self):
        total = 0
        total_pairs = self.combinations(self.K, 2)  # C(K, 2)
        if total_pairs == 0:
            return 0  # No pairs to calculate
        for i in range(self.N):
            # Calculate the distance contribution for this row
            for j in range(self.M):
                for k in range(j + 1, self.M):
                    distance = abs(j - k)
                    remaining = self.K - 2  # Two pieces are already selected
                    total += distance * self.combinations(remaining, self.K - 2)  # Corrected logic
            total *= self.combinations(self.M, 2)  # Each row contributes this many pairs
        return total * total_pairs % MOD  # Return total cost for all rows
    def calculate_col_cost(self):
        total = 0
        total_pairs = self.combinations(self.K, 2)  # C(K, 2)
        if total_pairs == 0:
            return 0  # No pairs to calculate
        for j in range(self.M):
            # Calculate the distance contribution for this column
            for i in range(self.N):
                for k in range(i + 1, self.N):
                    distance = abs(i - k)
                    remaining = self.K - 2  # Two pieces are already selected
                    total += distance * self.combinations(remaining, self.K - 2)  # Corrected logic
            total *= self.combinations(self.N, 2)  # Each column contributes this many pairs
        return total * total_pairs % MOD  # Return total cost for all columns
    def combinations(self, n, k):
        if k > n or k < 0:
            return 0
        return self.fact[n] * self.inv_fact[k] % MOD * self.inv_fact[n - k] % MOD