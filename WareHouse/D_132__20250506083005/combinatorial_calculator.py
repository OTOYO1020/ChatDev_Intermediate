'''
Contains the logic for calculating the number of arrangements of balls.
'''
from math import comb  # Import comb for binomial coefficient calculation
class CombinatorialCalculator:
    def __init__(self):
        self.MOD = 10**9 + 7
    def calculate_ways(self, k, n):
        ways = [0] * (k + 1)
        for i in range(1, k + 1):
            if i > n:
                break
            ways[i] = self._count_arrangements(i, k, n)
        return ways[1:]  # Return from index 1 to K
    def _count_arrangements(self, i, k, n):
        # Calculate the number of ways to arrange K blue balls with i moves
        if i > k or i > n:  # Ensure there are enough blue balls for the moves and i is not greater than N
            return 0
        remaining_balls = n - k  # Total red balls
        total_segments = i  # Total segments formed by blue balls
        remaining_blue_balls = k - i  # Remaining blue balls after placing one in each segment
        # The number of ways to distribute remaining red balls into total_segments
        red_ways = comb(remaining_balls + total_segments - 1, total_segments - 1)
        # The number of ways to distribute remaining blue balls into total_segments
        if remaining_blue_balls >= 0:
            blue_ways = comb(remaining_blue_balls + total_segments - 1, total_segments - 1)
        else:
            blue_ways = 0
        return (red_ways * blue_ways) % self.MOD