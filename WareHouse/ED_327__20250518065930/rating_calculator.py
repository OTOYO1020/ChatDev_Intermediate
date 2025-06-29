'''
Module for calculating the maximum contest rating based on performances.
'''
import math
def max_rating(N: int, P: list) -> float:
    max_rating_value = float('-inf')
    # Iterate through all possible non-empty subsets of contests using bitmask
    for i in range(1, 1 << N):  # from 1 to 2^N - 1
        subset = [P[j] for j in range(N) if (i & (1 << j)) > 0]
        rating = calculate_rating(subset)
        max_rating_value = max(max_rating_value, rating)
    return max_rating_value
def calculate_rating(subset: list) -> float:
    '''
    Calculate the rating R for a given subset of performances.
    R = (sum of performances) / (sqrt of number of performances)
    '''
    total_performance = sum(subset)
    num_performances = len(subset)
    if num_performances == 0:
        return 0.0
    return total_performance / math.sqrt(num_performances)