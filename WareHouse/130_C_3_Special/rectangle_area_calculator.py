'''
Contains the RectangleAreaCalculator class for calculating areas.
'''
class RectangleAreaCalculator:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def calculate_area(self):
        total_area = self.width * self.height
        max_area = total_area / 2
        multiple_ways = self.check_multiple_ways()
        return max_area, multiple_ways
    def check_multiple_ways(self):
        return 1 if (self.x == self.width / 2 and self.y == self.height / 2) else 0