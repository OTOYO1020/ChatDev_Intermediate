'''
This module contains the JewelConverter class responsible for converting red jewels to blue jewels.
'''
class JewelConverter:
    def __init__(self, N, X, Y):
        self.N = N
        self.X = X
        self.Y = Y
    def convert_jewels(self):
        total_blue_jewels = 0
        blue_jewels_at_level_n = 0  # Initialize blue jewels at level n
        for n in range(self.N, 1, -1):
            # Convert the red jewel of level n into a red jewel of level (n-1) and X blue jewels of level n
            blue_jewels_at_level_n = self.X  # Initialize blue jewels from red jewel
            total_blue_jewels += blue_jewels_at_level_n  # Update total blue jewels
            # Convert each blue jewel of level n into a red jewel of level (n-1) and Y blue jewels of level (n-1)
            total_blue_jewels += blue_jewels_at_level_n * self.Y  # Add blue jewels from converting blue jewels
        # After processing all levels, we need to account for the blue jewels at level 1
        total_blue_jewels += blue_jewels_at_level_n * self.Y  # Add blue jewels from the last level conversion
        return total_blue_jewels