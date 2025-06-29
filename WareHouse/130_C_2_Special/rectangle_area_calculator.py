'''
This module contains the RectangleAreaCalculator class which handles the calculations
related to the rectangle area based on user input.
'''
class RectangleAreaCalculator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_total_area(self):
        '''Calculates the total area of the rectangle.'''
        return self.width * self.height
    def calculate_max_area(self):
        '''Calculates the maximum possible area of the smaller part of the rectangle.'''
        # Calculate the total area
        total_area = self.calculate_total_area()
        # The maximum possible area of the smaller part
        return total_area / 2
    def check_multiple_ways(self, x, y):
        '''Checks if there are multiple ways to achieve the maximum area.'''
        center_x = self.width / 2  # Use floating-point division
        center_y = self.height / 2  # Use floating-point division
        return (x == center_x and y == center_y)  # Check for exact center without tolerance