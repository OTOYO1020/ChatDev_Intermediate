'''
Module to represent the city graph and handle city traversal logic.
'''
from typing import List, Tuple
class CityGraph:
    def __init__(self, N: int, roads: List[Tuple[int, int]]):
        self.N = N
        self.graph = {i: [] for i in range(1, N + 1)}
        for road in roads:
            self.graph[road[0]].append(road[1])
            self.graph[road[1]].append(road[0])
        for key in self.graph:
            self.graph[key].sort()  # Sort the adjacency list for ascending order traversal
    def find_visited_cities(self) -> List[int]:
        # Handle the case where there are no cities
        if self.N == 0:
            return []  # Return empty list if there are no cities
        # Handle the case where there are no roads
        if not self.graph[1]:  # If City 1 has no connections
            return [] if self.N > 0 else []  # Return empty list if there are cities, else return empty list
        visited = [False] * (self.N + 1)
        visited_order = []
        stack = [1]  # Start from City 1
        visited[1] = True  # Mark City 1 as visited
        visited_order.append(1)
        while stack:
            current_city = stack[-1]
            # Find unvisited directly connected cities
            unvisited_neighbors = [neighbor for neighbor in self.graph[current_city] if not visited[neighbor]]
            if unvisited_neighbors:
                # Visit the smallest unvisited neighbor
                next_city = unvisited_neighbors[0]
                stack.append(next_city)
                visited[next_city] = True
                visited_order.append(next_city)
            else:
                stack.pop()  # Backtrack if no unvisited neighbors
        return visited_order  # Return the order of visited cities