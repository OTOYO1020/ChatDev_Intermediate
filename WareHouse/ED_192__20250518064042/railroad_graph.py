'''
Module to handle the railroad graph and calculate the earliest arrival time.
'''
from typing import List, Tuple, Union
import heapq
class RailroadGraph:
    def __init__(self, N: int, M: int, railroads: List[Tuple[int, int, int, int]]):
        self.N = N
        self.M = M
        self.graph = self.build_graph(railroads)
    def build_graph(self, railroads: List[Tuple[int, int, int, int]]):
        graph = {i: [] for i in range(1, self.N + 1)}
        for A, B, K, T in railroads:
            if not (1 <= A <= self.N) or not (1 <= B <= self.N) or K <= 0 or T <= 0:
                raise ValueError(f"Invalid railroad entry: A={A}, B={B}, K={K}, T={T}. Ensure cities are within range and K, T are positive.")
            graph[A].append((B, K, T))
            # Removed the following line to prevent assuming bidirectionality
            # graph[B].append((A, K, T))  # Assuming bidirectional railroads
        return graph
    def earliest_arrival_time(self, X: int, Y: int) -> Union[int, str]:
        min_heap = [(0, X)]  # (current_time, city)
        earliest_times = {i: float('inf') for i in range(1, self.N + 1)}
        earliest_times[X] = 0
        while min_heap:
            current_time, city = heapq.heappop(min_heap)
            if city == Y:
                return current_time
            for neighbor, K, T in self.graph[city]:
                # Calculate the next available departure time
                next_departure = current_time if current_time % K == 0 else current_time + (K - current_time % K)
                arrival_time = next_departure + T
                # Only push to heap if the new arrival time is better
                if arrival_time < earliest_times[neighbor]:
                    earliest_times[neighbor] = arrival_time
                    heapq.heappush(min_heap, (arrival_time, neighbor))
        # Check if city Y is unreachable
        if earliest_times[Y] == float('inf'):
            return 'unreachable'
        return earliest_times[Y]