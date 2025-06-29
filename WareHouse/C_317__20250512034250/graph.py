'''
Graph class to represent towns and roads, including methods for adding roads and finding the maximum road length.
'''
from typing import List, Tuple
class Graph:
    def __init__(self, num_towns):
        self.num_towns = num_towns
        self.adjacency_list = {i: [] for i in range(num_towns)}
    def add_road(self, A, B, C):
        self.adjacency_list[A].append((B, C))
        self.adjacency_list[B].append((A, C))  # Assuming roads are bidirectional
    def dfs(self, town, visited, current_length):
        """
        Perform a depth-first search to find the maximum road length starting from a given town.
        Parameters:
        town (int): The current town being visited.
        visited (set): A set of towns that have already been visited.
        current_length (int): The total length of the roads traversed so far.
        Returns:
        int: The maximum road length found from this town.
        """
        visited.add(town)
        max_length = current_length
        for neighbor, length in self.adjacency_list[town]:
            if neighbor not in visited:
                max_length = max(max_length, self.dfs(neighbor, visited, current_length + length))
        visited.remove(town)  # Ensure to remove the town after exploring
        return max_length
    def max_road_length(self):
        if not any(self.adjacency_list.values()):  # Check if there are no roads
            return 0
        max_length = 0  # Initialize to 0 to indicate no valid paths found
        for town in range(self.num_towns):
            visited = set()  # Move the initialization of visited inside the loop
            current_length = self.dfs(town, visited, 0)
            max_length = max(max_length, current_length)  # Update max_length if current_length is greater
        return max_length  # Return the maximum length found