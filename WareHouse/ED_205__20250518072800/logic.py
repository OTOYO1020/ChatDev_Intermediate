'''
Logic module for calculating valid arrangements of balls.
'''
from utils import modular_arithmetic
def precompute_factorials(max_n: int, mod: int):
    factorials = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        factorials[i] = (factorials[i - 1] * i) % mod
    return factorials
def countArrangements(N: int, M: int, K: int) -> int:
    MOD = 10**9 + 7
    # Check if K is sufficient for valid arrangements
    if abs(N - M) > K:
        return 0  # No valid arrangements possible
    # Precompute factorials
    max_factorial = max(N, M)
    factorials = precompute_factorials(max_factorial, MOD)
    def combinations(n: int, k: int) -> int:
        if k > n or k < 0:
            return 0
        numerator = factorials[n]  # This is already modulo
        denominator = (factorials[k] * factorials[n - k]) % MOD  # Ensure denominator is modulo
        return (numerator * pow(denominator, MOD - 2, MOD)) % MOD  # Apply modulo here
    valid_arrangements = 0
    for w_used in range(N + 1):
        # Calculate the range for black balls based on the condition w_i <= b_i + K
        b_used_min = max(0, w_used - K)  # Minimum black balls needed
        b_used_max = min(M, w_used + K)  # Maximum black balls allowed
        # Iterate through the valid range of black balls
        for b_used in range(b_used_min, b_used_max + 1):
            total_balls_used = w_used + b_used
            arrangements = combinations(total_balls_used, w_used)
            valid_arrangements = (valid_arrangements + arrangements) % MOD  # Use modular arithmetic
    return valid_arrangements