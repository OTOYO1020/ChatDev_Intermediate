'''
Graph class to represent the directed graph and perform topological sort.
'''
from collections import defaultdict
import heapq
class Graph:
    def __init__(self, vertices):
        '''
        Initializes the graph with a given number of vertices.
        '''
        self.V = vertices
        self.adj = defaultdict(list)
        self.indegree = [0] * (vertices + 1)
        self.edges = set()  # To track added edges
    def add_edge(self, u, v):
        '''
        Adds a directed edge from vertex u to vertex v.
        '''
        if (u, v) not in self.edges:  # Check for duplicate edges
            self.adj[u].append(v)
            self.indegree[v] += 1
            self.edges.add((u, v))  # Add edge to the set
    def topological_sort(self):
        '''
        Performs a topological sort on the directed graph.
        Returns a list of vertices in topological order or -1 if a cycle is detected.
        '''
        min_heap = []
        for i in range(1, self.V + 1):
            if self.indegree[i] == 0:
                heapq.heappush(min_heap, i)  # Use a min-heap to get the smallest element
        result = []
        processed_count = 0  # Count of processed nodes
        while min_heap:
            current = heapq.heappop(min_heap)  # Get the smallest element
            result.append(current)
            processed_count += 1  # Increment processed count
            for neighbor in self.adj[current]:
                self.indegree[neighbor] -= 1
                if self.indegree[neighbor] == 0:
                    heapq.heappush(min_heap, neighbor)  # Push the neighbor into the heap
        # Check if all vertices have been processed
        if processed_count != self.V:
            return -1  # Cycle detected or not all vertices are included
        return result