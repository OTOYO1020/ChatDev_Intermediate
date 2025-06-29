'''
Module for calculating the maximum number of projects based on department employee counts.
'''
from typing import List
import heapq
def max_projects(N: int, K: int, A: List[int]) -> int:
    '''
    Calculate the maximum number of projects that can be formed with K departments.
    Parameters:
    N (int): Total number of departments.
    K (int): Number of departments to form a project.
    A (List[int]): List of employee counts for each department.
    Returns:
    int: Maximum number of projects that can be formed.
    '''
    if N < K:
        return 0  # Cannot form any projects if there are fewer departments than required
    # Convert A into a max-heap (invert values for max-heap behavior)
    max_heap = [-a for a in A]
    heapq.heapify(max_heap)
    total_projects = 0
    while len(max_heap) >= K:
        # Select the current group of K departments
        group = [-heapq.heappop(max_heap) for _ in range(K)]
        # Determine the number of projects that can be formed from this group
        min_employees = min(group)
        total_projects += min_employees  # Add the minimum of the current group
        # Reduce the employee counts in the selected departments
        for j in range(K):
            group[j] -= min_employees  # Reduce the count
        # Only push back departments that still have employees left
        for employees in group:
            if employees > 0:
                heapq.heappush(max_heap, -employees)
    return total_projects  # Return the total number of complete projects