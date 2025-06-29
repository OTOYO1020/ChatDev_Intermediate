'''
This module contains the CircleSquareCounter class which is responsible for
calculating the number of squares contained within a circle given a radius.
'''
import math
class CircleSquareCounter:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius must be a non-negative integer.")
        self.radius = radius
        self.count = 0
    def count_squares(self):
        if self.radius == 0:
            return 0  # No squares can be contained within a circle of radius zero.
        for i in range(-self.radius, self.radius + 1):
            for j in range(-self.radius, self.radius + 1):
                # Calculate the distances for all four corners of the square
                corners = [
                    (i + 0.5, j + 0.5),
                    (i + 0.5, j - 0.5),
                    (i - 0.5, j + 0.5),
                    (i - 0.5, j - 0.5)
                ]
                # Check if all corners are within the circle using squared distances
                if all((x ** 2 + y ** 2) <= self.radius ** 2 for x, y in corners):
                    self.count += 1
        return self.count