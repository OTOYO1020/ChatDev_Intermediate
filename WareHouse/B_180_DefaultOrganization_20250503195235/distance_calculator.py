'''
Module for calculating Manhattan, Euclidean, and Chebyshev distances.
'''
import math
class DistanceCalculator:
    def __init__(self, coordinates):
        '''
        Initializes the DistanceCalculator with the given coordinates.
        Parameters:
        coordinates (list): A list of integers representing the coordinates in N-dimensional space.
        '''
        self.coordinates = coordinates
    def calculate_distances(self):
        '''
        Calculates the Manhattan, Euclidean, and Chebyshev distances based on the coordinates.
        Returns:
        tuple: A tuple containing the Manhattan distance, Euclidean distance, and Chebyshev distance.
        '''
        manhattan_distance = 0
        euclidean_distance = 0
        chebyshev_distance = 0
        for x in self.coordinates:
            manhattan_distance += abs(x)  # Update Manhattan distance
            euclidean_distance += x ** 2   # Update Euclidean distance
            chebyshev_distance = max(chebyshev_distance, abs(x))  # Update Chebyshev distance
        euclidean_distance = math.sqrt(euclidean_distance)  # Finalize Euclidean distance
        return manhattan_distance, euclidean_distance, chebyshev_distance