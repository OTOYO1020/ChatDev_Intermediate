'''
Module for calculating the lexicographically smallest permutation based on constraints.
'''
from collections import defaultdict
from typing import List, Tuple
import heapq  # Importing heapq for priority queue functionality
class ConstraintError(Exception):
    pass
def find_lexicographically_smallest_permutation(N: int, M: int, constraints: List[Tuple[int, int]]):
    # Handle the case when there are no constraints
    if M == 0:
        return list(range(1, N + 1))  # Return sorted list from 1 to N
    graph = defaultdict(list)
    in_degree = [0] * (N + 1)
    # Build the graph and in-degree array
    for A, B in constraints:
        if A == B:
            raise ConstraintError("Self-loop detected: A and B cannot be the same. Please provide valid constraints.")
        if 1 <= A <= N and 1 <= B <= N:  # Validate constraints
            graph[A].append(B)
            in_degree[B] += 1
        else:
            raise ConstraintError(f"Constraint ({A}, {B}) is out of bounds. Must be between 1 and {N}.")
    # Use a priority queue to maintain the nodes with zero in-degree
    zero_in_degree = []
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            heapq.heappush(zero_in_degree, i)
    sorted_order = []
    visited = set()  # Track visited nodes to detect cycles
    # Perform topological sort
    while zero_in_degree:
        current = heapq.heappop(zero_in_degree)  # Get the smallest element
        sorted_order.append(current)
        visited.add(current)  # Mark the current node as visited
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(zero_in_degree, neighbor)
    # Check if we have a valid topological sort
    if len(sorted_order) != N:
        return -1  # Cycle detected or not all nodes are included
    return sorted_order