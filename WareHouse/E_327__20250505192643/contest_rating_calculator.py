'''
Contains the logic for calculating the maximum rating based on contest performances.
'''
from itertools import combinations
import math
class ContestRatingCalculator:
    '''
    Class to calculate the maximum rating from contest performances.
    '''
    def __init__(self, performances):
        '''
        Initializes the class with the list of performances.
        '''
        self.performances = performances
    def calculate_max_rating(self):
        '''
        Computes the maximum rating based on the performances.
        '''
        max_rating = float('-inf')
        N = len(self.performances)
        # Handle the edge case where there is only one contest
        if N == 1:
            return self.performances[0]  # Directly return the performance of the single contest
        # Iterate over all possible sizes of subsets
        for k in range(1, N + 1):
            for subset in combinations(range(N), k):  # Generate all combinations of size k
                Q = [self.performances[i] for i in subset]
                R = self.calculate_rating(Q, k)
                if R > max_rating:  # Update only if R is greater
                    max_rating = R
        # Return the maximum rating found
        return max_rating
    def calculate_rating(self, Q, k):
        '''
        Calculates the rating R based on the performances Q.
        '''
        numerator = sum((0.9 ** (k - i - 1)) * Q[i] for i in range(k))
        denominator = sum(0.9 ** (k - i - 1) for i in range(k))
        R = (numerator / denominator) - (1200 / math.sqrt(k))
        return R