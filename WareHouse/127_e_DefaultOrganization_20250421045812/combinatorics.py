'''
Utility class for calculating combinations and factorials.
'''
class Combinatorics:
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod
        self.fact = [1] * (n + 1)
        self.inv_fact = [1] * (n + 1)
        self.precompute_factorials()
    def precompute_factorials(self):
        for i in range(2, self.n + 1):
            self.fact[i] = self.fact[i - 1] * i % self.mod
        self.inv_fact[self.n] = pow(self.fact[self.n], self.mod - 2, self.mod)
        for i in range(self.n - 1, 0, -1):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % self.mod
    def combination(self, n, k):
        if k > n or k < 0:
            return 0
        return self.fact[n] * self.inv_fact[k] % self.mod * self.inv_fact[n - k] % self.mod