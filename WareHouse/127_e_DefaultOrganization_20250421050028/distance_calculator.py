'''
Module for calculating Manhattan distances in a grid.
'''
from utils import mod_inverse, comb
class DistanceCalculator:
    MOD = 10**9 + 7
    def __init__(self, N, M, K):
        self.N = N
        self.M = M
        self.K = K
        self.fact = []
        self.inv_fact = []
    def precalculate_combinations(self):
        max_size = self.N * self.M
        self.fact = [1] * (max_size + 1)
        self.inv_fact = [1] * (max_size + 1)
        for i in range(2, max_size + 1):
            self.fact[i] = self.fact[i - 1] * i % self.MOD
        self.inv_fact[max_size] = mod_inverse(self.fact[max_size], self.MOD)
        for i in range(max_size - 1, 0, -1):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % self.MOD
    def calculate_distance_cost(self):
        self.precalculate_combinations()
        total_cost = 0
        # Calculate distance cost in row direction
        row_cost = 0
        for i in range(self.N):
            for j in range(self.M):
                distance_contribution = j * (self.M - j - 1)  # Contribution of distance j
                total_pairs = comb(self.M - 1, 1, self.fact, self.inv_fact)  # Total ways to choose 1 more column
                row_cost += distance_contribution * total_pairs % self.MOD
        # Multiply by the number of ways to choose K-2 from remaining squares
        if self.K - 2 >= 0:
            row_cost *= comb(self.N * self.M - self.K, self.K - 2, self.fact, self.inv_fact) % self.MOD * self.M % self.MOD
        # Calculate distance cost in column direction
        col_cost = 0
        for j in range(self.M):
            for i in range(self.N):
                distance_contribution = i * (self.N - i - 1)  # Contribution of distance i
                total_pairs = comb(self.N - 1, 1, self.fact, self.inv_fact)  # Total ways to choose 1 more row
                col_cost += distance_contribution * total_pairs % self.MOD
        # Multiply by the number of ways to choose K-2 from remaining squares
        if self.K - 2 >= 0:
            col_cost *= comb(self.N * self.M - self.K, self.K - 2, self.fact, self.inv_fact) % self.MOD * self.N % self.MOD
        total_cost += (row_cost + col_cost) % self.MOD
        return total_cost % self.MOD