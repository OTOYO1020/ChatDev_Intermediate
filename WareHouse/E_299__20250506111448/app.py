'''
App class to manage the application logic for graph distance checking.
'''
from graph import Graph
from distance_checker import DistanceChecker
from collections import deque
class App:
    def __init__(self):
        self.graph = Graph()
    def run(self):
        # Read number of vertices and edges
        N, M = map(int, input().split())
        for _ in range(M):
            u, v = map(int, input().split())
            self.graph.add_edge(u, v)
        # Read number of distance pairs
        K = int(input())
        pairs = [tuple(map(int, input().split())) for _ in range(K)]
        # Initialize distances and painted vertices
        distances = {vertex: float('inf') for vertex in range(1, N + 1)}
        painted = {vertex: 'white' for vertex in range(1, N + 1)}
        queue = deque()
        # Add vertices that can be painted black to the queue
        for p, d in pairs:
            if p in self.graph.graph:
                queue.append(p)
                distances[p] = 0  # Start painting this vertex black
                painted[p] = 'black'
        # Multi-source BFS
        distances = self.graph.bfs(queue)
        # Check conditions after BFS
        distance_checker = DistanceChecker(distances)
        valid_painting = distance_checker.check_conditions(pairs)
        # Ensure at least one vertex is painted black and valid painting exists
        if valid_painting and any(distances[v] <= d for p, d in pairs for v in painted if painted[v] == 'black'):
            result = ', '.join(f"{vertex}: {color}" for vertex, color in painted.items())
            print(result)
        else:
            print("IMPOSSIBLE")