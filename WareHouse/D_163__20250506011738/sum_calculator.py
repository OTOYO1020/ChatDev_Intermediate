'''
Utility class for calculating unique sums based on N and K.
'''
class SumCalculator:
    MODULO = 10**9 + 7
    def __init__(self, N, K):
        self.N = N
        self.K = K
        self.unique_sums = set()
    def calculate_unique_sums(self):
        # Check if K is greater than N; if so, return a message as no combinations can be formed
        if self.K > self.N:
            return "K cannot be greater than N. No combinations can be formed."
        if self.N == 0:
            return 0  # Return 0 since there are no integers to combine
        start = 10**100
        # Calculate the unique sums directly
        for size in range(self.K, self.N + 1):
            total_sum = (size * (start + (size - 1) / 2)) % self.MODULO
            self.unique_sums.add(total_sum)
        # Return the count of unique sums
        return len(self.unique_sums)