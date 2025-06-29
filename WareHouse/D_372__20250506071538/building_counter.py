'''
Module for counting valid buildings based on their heights.
'''
class BuildingCounter:
    def __init__(self, heights):
        self.heights = heights
    def count_valid_buildings(self):
        n = len(self.heights)
        result = [0] * n  # Keep the size as N to match the number of buildings
        for i in range(n):  # Start from 0 to N-1 to match the requirement of starting from 1
            max_height = 0
            for j in range(i + 1, n):  # Adjust to go up to n (exclusive)
                if self.heights[j] > max_height:  # Access heights directly
                    result[i] += 1  # Increment the count for the current building
                    max_height = self.heights[j]
        return result  # Return the complete result