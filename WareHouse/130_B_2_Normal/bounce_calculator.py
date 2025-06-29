'''
Module for calculating bounce coordinates and counting valid bounces.
'''
class BounceCalculator:
    def __init__(self, n, l, x):
        """Initialize the BounceCalculator with n, l, and x."""
        self.n = n
        self.l = l
        self.x = x
        self.d = [0] * (n + 1)
        self.initialize_variables()
        if self.n > 0:  # Only calculate if there are bounce coordinates
            self.calculate_bounce_coordinates()
    def initialize_variables(self):
        """Initialize the first bounce coordinate D[0]."""
        self.d[0] = 0
    def calculate_bounce_coordinates(self):
        """Calculate the bounce coordinates based on the list L."""
        for i in range(1, self.n + 1):
            self.d[i] = self.d[i - 1] + self.l[i - 1]
    def count_valid_bounces(self):
        """Count how many bounce coordinates are less than or equal to X."""
        if self.n == 0:  # If there are no bounces, return 0
            return 0
        # Use a list comprehension to count valid bounces
        return sum(1 for value in self.d if value <= self.x)
    def get_result(self):
        """Return the count of valid bounces after calculating coordinates."""
        return self.count_valid_bounces()