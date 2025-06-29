'''
Module containing the logic to determine if a unique permutation can be derived from pairs.
'''
from collections import defaultdict, deque
from typing import List, Tuple
def can_determine_permutation(N: int, M: int, pairs: List[Tuple[int, int]]) -> Tuple[bool, List[int]]:
    graph = defaultdict(list)
    in_degree = [0] * (N + 1)
    seen_pairs = set()  # To track unique pairs
    # Build the graph and in-degree array
    for x, y in pairs:
        if (x, y) not in seen_pairs:  # Check for unique pairs
            graph[x].append(y)
            in_degree[y] += 1
            seen_pairs.add((x, y))
    # Queue for nodes with no incoming edges
    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
    sorted_order = []
    while queue:
        if len(queue) > 1:
            # More than one node with no incoming edges means not unique
            return False, []
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    # Check if we have a valid permutation
    if len(sorted_order) == N:
        return True, sorted_order
    else:
        return False, []