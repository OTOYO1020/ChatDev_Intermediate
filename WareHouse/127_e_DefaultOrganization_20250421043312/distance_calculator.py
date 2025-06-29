'''
Distance calculator for computing Manhattan distances.
'''
class DistanceCalculator:
    def __init__(self, n, m, k):
        self.n = n
        self.m = m
        self.k = k
        self.MOD = 10**9 + 7
        self.fact = [1] * (n * m + 1)
        self.inv_fact = [1] * (n * m + 1)
        self.precalculate_combinations()
    def precalculate_combinations(self):
        """
        Precalculate factorials and their modular inverses for combinations.
        """
        for i in range(2, self.n * self.m + 1):
            self.fact[i] = self.fact[i - 1] * i % self.MOD
        self.inv_fact[self.n * self.m] = pow(self.fact[self.n * self.m], self.MOD - 2, self.MOD)
        for i in range(self.n * self.m - 1, 0, -1):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % self.MOD
    def C(self, n, k):
        """
        Calculate combinations C(n, k) under modulo MOD.
        Parameters:
            n (int): Total number of items.
            k (int): Number of items to choose.
        Returns:
            int: The number of combinations C(n, k) modulo MOD.
        """
        if k > n or k < 0:
            return 0
        return self.fact[n] * self.inv_fact[k] % self.MOD * self.inv_fact[n - k] % self.MOD
    def calculate_distance(self):
        """
        Calculate the total Manhattan distance for K pieces placed on an N x M grid.
        Returns:
            int: The total Manhattan distance modulo MOD.
        """
        if self.k < 2 or self.k > self.n * self.m:
            return 0  # Cannot calculate distances with fewer than 2 pieces or more than available squares
        row_cost = 0
        # Calculate distance cost in row direction
        for i in range(self.n):
            distance_sum = 0
            for j1 in range(self.m):
                for j2 in range(j1 + 1, self.m):
                    distance_sum += (j2 - j1)  # |j1 - j2| is simply j2 - j1 since j2 > j1
            total_pairs = self.C(self.m, 2)
            # Correctly multiply by the number of combinations of the remaining pieces
            row_cost += distance_sum * total_pairs * self.C(self.n * self.m - 2, self.k - 2) % self.MOD
        col_cost = 0
        # Calculate distance cost in column direction
        for j in range(self.m):
            distance_sum = 0
            for i1 in range(self.n):
                for i2 in range(i1 + 1, self.n):
                    distance_sum += (i2 - i1)  # |i1 - i2| is simply i2 - i1 since i2 > i1
            total_pairs = self.C(self.n, 2)
            # Correctly multiply by the number of combinations of the remaining pieces
            col_cost += distance_sum * total_pairs * self.C(self.n * self.m - 2, self.k - 2) % self.MOD
        # Total cost is the sum of row and column costs
        total_cost = (row_cost + col_cost) % self.MOD
        return total_cost