'''
Module for calculating the number of bounces based on input values.
'''
class BounceCalculator:
    def calculate_bounces(self, n, x, l):
        """
        Calculate the number of bounces where the coordinate is at most X.
        """
        D = 0
        bounce_count = 0
        # Check first bounce at coordinate 0
        if D <= x:
            bounce_count += 1
        # Iterate over bounces starting from index 0 to n-1
        for i in range(n):  # Loop from 0 to n-1 (inclusive)
            D += l[i]  # Update the coordinate D using the current bounce distance
            if D <= x:
                bounce_count += 1
        return bounce_count