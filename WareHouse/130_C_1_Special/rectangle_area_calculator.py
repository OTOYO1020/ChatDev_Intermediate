'''
Module for calculating rectangle areas based on given dimensions and point coordinates.
'''
class RectangleAreaCalculator:
    '''
    Class to calculate areas of a rectangle based on its dimensions and a point.
    '''
    def __init__(self, width, height, x, y):
        '''
        Initializes the rectangle dimensions and point coordinates.
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def calculate_total_area(self):
        '''
        Computes the total area of the rectangle.
        '''
        return self.width * self.height
    def calculate_max_possible_area(self):
        '''
        Computes the maximum possible area of the smaller part.
        '''
        total_area = self.calculate_total_area()
        return total_area / 2  # Use regular division to ensure the result is a float
    def check_multiple_ways(self):
        '''
        Checks if there are multiple ways to achieve the maximum area.
        '''
        return self.x == self.width / 2 and self.y == self.height / 2