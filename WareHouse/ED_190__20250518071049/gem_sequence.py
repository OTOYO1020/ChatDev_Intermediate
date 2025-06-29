'''
Module containing the logic to determine if a valid gem sequence can be formed.
'''
from collections import defaultdict, deque
from typing import List, Tuple
def can_form_sequence(N: int, M: int, pairs: List[Tuple[int, int]], required_gems: List[int]) -> Tuple[bool, int]:
    # Handle edge case where there are no gems
    if N == 0:
        return (len(required_gems) == 0, 0)  # No gems, check if no required gems
    if M == 0:
        # If there are required gems and no pairs, return False
        if required_gems:
            return (False, 0)  # Cannot form a valid sequence without pairs
        return (True, 0)  # Return True if no required gems
    # Check for invalid required gems
    if any(gem < 1 or gem > N for gem in required_gems):
        return (False, 0)  # Invalid required gems
    # Handle edge case where there is only one required gem
    if len(required_gems) == 1 and required_gems[0] > N:
        return (False, 0)  # Required gem is not present in the range of gems
    graph = defaultdict(list)
    for a, b in pairs:
        graph[a].append(b)
        graph[b].append(a)
    visited = set()
    components = []
    def bfs(start):
        """
        Perform BFS to find all gems in the connected component starting from 'start'.
        Parameters:
        start (int): The starting gem for the BFS traversal.
        Returns:
        set: A set of gems in the connected component.
        """
        queue = deque([start])
        component = set()
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                component.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return component
    for gem in range(1, N + 1):
        if gem not in visited:
            component = bfs(gem)
            components.append(component)
    # Create a set of required gems for easy checking, filtering out invalid gems
    required_set = {gem for gem in required_gems if 1 <= gem <= N}
    # Check if the number of unique required gems is greater than the total number of gems
    if len(required_set) > N:
        return (False, 0)  # More required gems than available gems
    found_required_gems = set()
    for component in components:
        found_required_gems.update(component.intersection(required_set))
    # Check if all required gems are found in the components
    if all(gem in found_required_gems for gem in required_set):
        min_gems = len(required_set.intersection(found_required_gems))  # Count only the unique required gems found
        return (True, min_gems)
    # Handle case where required_gems is empty
    if not required_set:
        return (True, 0)  # No gems needed
    return (False, 0)