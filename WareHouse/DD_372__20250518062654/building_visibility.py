'''
Module to count the number of visible buildings based on their heights.
'''
from typing import List
def count_visible_buildings(N: int, H: List[int]) -> List[int]:
    result = []
    for i in range(N):
        count = 0  # Start count from 0
        max_height = 0  # Initialize max_height to 0
        for j in range(i + 1, N):
            if H[j] > max_height:
                count += 1
                max_height = H[j]  # Update max_height to the height of building j
        result.append(count)  # Append the count of visible buildings for building i
    return result