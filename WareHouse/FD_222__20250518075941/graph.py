'''
Graph class to represent towns and roads and calculate travel costs.
'''
import heapq
from typing import List, Tuple
class Graph:
    def __init__(self, towns: int, roads: List[Tuple[int, int, int]], sightseeing_costs: List[int]):
        self.towns = towns
        self.sightseeing_costs = sightseeing_costs
        self.adjacency_list = {i: [] for i in range(towns)}
        for road in roads:
            a, b, cost = road
            self.adjacency_list[a].append((b, cost))
            self.adjacency_list[b].append((a, cost))
    def dijkstra(self, start: int) -> List[int]:
        distances = [float('inf')] * self.towns
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_town = heapq.heappop(priority_queue)
            if current_distance > distances[current_town]:
                continue
            for neighbor, toll in self.adjacency_list[current_town]:
                distance = current_distance + toll
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances
    def max_travel_cost(self) -> List[int]:
        max_costs = []
        if not any(self.adjacency_list.values()):  # Check if there are no roads
            return [-1] * self.towns  # All towns are isolated
        for i in range(self.towns):
            distances = self.dijkstra(i)
            max_cost = -1  # Initialize to -1 to indicate no reachable towns
            for j in range(self.towns):
                if i != j and distances[j] != float('inf'):  # Check if the town is reachable
                    travel_cost = distances[j] + self.sightseeing_costs[j]
                    max_cost = max(max_cost, travel_cost)
            max_costs.append(max_cost)  # Append the max cost or -1 if no towns are reachable
        return max_costs