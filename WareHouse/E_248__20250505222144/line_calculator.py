'''
Contains logic for calculating slopes and intercepts of lines.
'''
from collections import defaultdict
from math import gcd
class LineCalculator:
    def calculate_lines(self, points, K):  # Accept K as a parameter
        line_count = defaultdict(set)  # Use a set to store unique points on each line
        valid_lines = 0
        N = len(points)
        if N < 2:
            return 0
        # Handle edge case where K = 1
        if K == 1:
            return N  # Every point is a valid line
        # Check for collinearity
        if N == 2:
            return 1 if K <= 2 else 0
        for i in range(N):
            for j in range(i + 1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2:  # Vertical line
                    line_repr = ('vertical', x1)  # Use a consistent identifier for vertical lines
                else:
                    dy = y2 - y1
                    dx = x2 - x1
                    g = gcd(dy, dx)
                    slope = (dy // g, dx // g)  # Normalize slope
                    if slope[1] < 0:  # Ensure denominator is positive
                        slope = (-slope[0], -slope[1])
                    intercept = (y1 * dx - x1 * dy) // g  # y = mx + b form
                    line_repr = (slope, intercept)
                line_count[line_repr].add((x1, y1))  # Add points to the set
                line_count[line_repr].add((x2, y2))  # Add points to the set
        for count in line_count.values():
            if len(count) >= K:  # Check for K or more unique points
                valid_lines += 1
        # Check for collinearity
        if valid_lines > 0:
            if len(line_count) == 1:  # All points are collinear
                return "Infinity"
            else:
                return valid_lines
        return 0