'''
Graph class that represents the graph and implements BFS for shortest path finding.
'''
from collections import deque, defaultdict
class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
    def add_edge(self, u, v):
        # Connect each state of vertex u to the corresponding state of vertex v
        for state in range(3):
            self.adjacency_list[(u, state)].append((v, (state + 1) % 3))
            self.adjacency_list[(v, state)].append((u, (state + 1) % 3))
    def bfs(self, start, target):
        start_node = (start, 0)
        target_node = (target, 0)
        queue = deque([start_node])
        visited = set([start_node])
        distance = 0
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == target_node:
                    return distance  # Return the distance directly
                for neighbor in self.adjacency_list[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return -1  # Return -1 if no path is found