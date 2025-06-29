'''
Graph class to represent the railroad connections and implement Dijkstra's algorithm.
'''
import heapq
class Graph:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.adjacency_list = [[] for _ in range(num_cities)]
    def add_edge(self, a, b, travel_time, frequency):
        self.adjacency_list[a].append((b, travel_time, frequency))
        self.adjacency_list[b].append((a, travel_time, frequency))
    def dijkstra(self, start, end):
        min_heap = [(0, start)]  # (current_time, city)
        earliest_arrival = [float('inf')] * self.num_cities
        earliest_arrival[start] = 0
        while min_heap:
            current_time, current_city = heapq.heappop(min_heap)
            if current_city == end:
                return current_time
            if current_time > earliest_arrival[current_city]:
                continue
            for neighbor, travel_time, frequency in self.adjacency_list[current_city]:
                next_departure = current_time if current_time % frequency == 0 else current_time + (frequency - current_time % frequency)
                arrival_time = next_departure + travel_time
                if arrival_time < earliest_arrival[neighbor]:
                    earliest_arrival[neighbor] = arrival_time
                    heapq.heappush(min_heap, (arrival_time, neighbor))
        return float('inf')  # unreachable