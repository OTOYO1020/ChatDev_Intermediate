'''
Module containing the logic for calculating the maximum number of illuminated buildings.
'''
from typing import List
def maxIlluminatedBuildings(N: int, H: List[int]) -> int:
    # Handle edge case where there is only one building
    if N == 1:
        return 1
    unique_heights = set(H)  # Get unique heights
    max_count = 0  # Initialize maximum count of illuminated buildings
    for height in unique_heights:
        indices = [i for i, h in enumerate(H) if h == height]  # Get indices of buildings with the current height
        num_indices = len(indices)
        if num_indices < 2:
            continue  # Skip if there are less than 2 buildings of this height
        # Check all possible intervals
        for start in range(num_indices):
            for next in range(start + 1, num_indices):
                interval = indices[next] - indices[start]  # Calculate the interval
                count = 2  # Start with the first two buildings
                last_index = indices[next]
                # Count how many buildings can be illuminated with this interval
                for k in range(next + 1, num_indices):
                    if (indices[k] - last_index) == interval:
                        count += 1  # Increment count for this interval
                        last_index = indices[k]  # Update last_index to the current building
                # Update max_count based on the maximum found for this height
                max_count = max(max_count, count)
    return max_count  # Return the maximum count of illuminated buildings