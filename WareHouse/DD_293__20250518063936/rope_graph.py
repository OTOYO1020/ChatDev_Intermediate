'''
Module to define the RopeGraph class for managing rope connections and counting cycles.
'''
from typing import List, Tuple
class RopeGraph:
    def __init__(self, N: int):
        self.N = N
        self.adj_list = {i: [] for i in range(N)}
        self.colors = {}
        self.used_colors = set()  # Track used colors for all ends
    def tie_ends(self, end1: int, color1: str, end2: int, color2: str):
        # Prevent tying ends of the same color multiple times
        if (end1, color1) in self.colors or (end2, color2) in self.colors:
            return  
        # Check if end1 or end2 is already tied to any other end
        if end1 in self.colors or end2 in self.colors:
            return  # Prevent tying if either end is already tied
        # Allow tying only if both ends are free
        self.adj_list[end1].append(end2)
        self.adj_list[end2].append(end1)
        self.colors[end1] = (end2, color2)  # Store the tied end and its color
        self.colors[end2] = (end1, color1)  # Store the tied end and its color
        # Mark colors as used only for the specific ends
        self.used_colors.add(color1)  # Mark color1 as used
        self.used_colors.add(color2)  # Mark color2 as used
    def count_cycles_and_non_cycles(self) -> Tuple[int, int]:
        visited = [False] * self.N
        cycles = 0
        non_cycles = 0
        def dfs(node: int) -> Tuple[int, int]:
            stack = [(node, -1)]
            count = 0
            edges = 0
            while stack:
                current, parent = stack.pop()
                if not visited[current]:
                    visited[current] = True
                    count += 1
                    for neighbor in self.adj_list[current]:
                        edges += 1
                        if not visited[neighbor]:
                            stack.append((neighbor, current))
            return count, edges // 2  # Each edge is counted twice
        for i in range(self.N):
            if not visited[i]:
                vertices_count, edges_count = dfs(i)
                if edges_count == vertices_count:
                    cycles += 1
                else:
                    non_cycles += 1
        return cycles, non_cycles