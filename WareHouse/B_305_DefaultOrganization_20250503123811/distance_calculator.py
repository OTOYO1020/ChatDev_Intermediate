'''
Module for calculating distances between points A-G.
'''
class DistanceCalculator:
    '''
    Class to calculate distances between points.
    '''
    def __init__(self):
        self.points = [0, 3, 4, 8, 9, 14, 19, 28]
        self.point_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    def calculate(self, p, q):
        '''
        Calculates the distance between two points.
        Parameters:
        p (str): The first point (A-G).
        q (str): The second point (A-G).
        Returns:
        int: The distance between points p and q.
        Raises:
        ValueError: If either point is invalid.
        '''
        if p not in self.point_index or q not in self.point_index:
            raise ValueError("Invalid points: Both points must be uppercase letters A-G.")
        index_p = self.point_index[p]
        index_q = self.point_index[q]
        distance = abs(self.points[index_p] - self.points[index_q])
        return distance