'''
Module for calculating maximum satisfaction from given flavors and deliciousness.
'''
from collections import defaultdict
from typing import List
from itertools import combinations
def max_satisfaction(N: int, flavors: List[int], deliciousness: List[int]) -> int:
    flavor_map = defaultdict(list)
    # Group deliciousness values by their respective flavors
    for i in range(N):
        flavor_map[flavors[i]].append(deliciousness[i])
    max_satis = 0
    max1 = max2 = float('-inf')
    # Calculate maximum satisfaction for same flavor pairs
    for del_values in flavor_map.values():
        if len(del_values) > 1:
            # Satisfaction for all pairs of same flavor
            for s, t in combinations(del_values, 2):
                max_satis = max(max_satis, max(s, t) + min(s, t) / 2)
        # Update max1 and max2 for different flavors
        current_max = max(del_values)
        if current_max > max1:
            max2 = max1
            max1 = current_max
        elif current_max > max2:
            max2 = current_max
    # Check if we have at least two different flavors
    if max2 == float('-inf'):
        return 0  # No valid pairs can be formed
    # Calculate satisfaction for different flavors
    max_satis = max(max_satis, max1 + max2)
    return int(max_satis)  # Return the maximum satisfaction as an integer