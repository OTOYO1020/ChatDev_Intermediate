'''
Module to calculate the number of arrangements of balls.
'''
from typing import List
MOD = 10**9 + 7
def countArrangements(N: int, K: int) -> List[int]:
    ways = [0] * (K + 1)  # Initialize ways list to store arrangements for each move count
    if K == 0 or K > N:
        return [0] * K  # Return a list of zeros of size K if K is 0 or K > N
    # Calculate the factorial and inverse factorial for combinations
    factorial = [1] * (N + 1)
    for i in range(2, N + 1):
        factorial[i] = factorial[i - 1] * i % MOD
    def mod_inverse(x: int) -> int:
        return pow(x, MOD - 2, MOD)
    inverse_factorial = [1] * (N + 1)
    for i in range(2, N + 1):
        inverse_factorial[i] = mod_inverse(factorial[i])
    # Calculate arrangements for each move count from 1 to K
    for i in range(1, K + 1):
        if i <= N:  # Ensure i does not exceed N
            # Calculate the number of ways to arrange K blue balls in exactly i moves
            # Using the stars and bars combinatorial method
            ways[i] = (factorial[K - 1] * inverse_factorial[i - 1] % MOD * inverse_factorial[K - i] % MOD) % MOD
            # Additionally, consider arrangements of red balls
            ways[i] = (ways[i] * factorial[N - K] % MOD) % MOD
    return ways[1:K + 1]  # Return the complete list of arrangements from 1 to K