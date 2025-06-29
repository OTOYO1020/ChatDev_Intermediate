'''
Graph class to represent the graph and implement Dijkstra's algorithm.
'''
import heapq
class Graph:
    def __init__(self, N, M, A):
        self.N = N
        self.M = M
        self.A = A
        self.adj_list = {i: [] for i in range(1, N + 1)}
    def add_edge(self, u, v, weight):
        '''
        Add an edge to the graph. If the graph is undirected, add both directions.
        '''
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))  # Assuming undirected graph
    def dijkstra(self):
        min_weights = [float('inf')] * (self.N + 1)
        min_weights[1] = self.A[0]  # Starting point weight
        priority_queue = [(min_weights[1], 1)]  # (weight, vertex)
        while priority_queue:
            current_weight, u = heapq.heappop(priority_queue)
            if current_weight > min_weights[u]:
                continue
            for v, edge_weight in self.adj_list[u]:
                # Total weight to reach vertex v
                weight = current_weight + edge_weight
                if weight < min_weights[v]:  # Compare without adding vertex weight
                    min_weights[v] = weight + self.A[v - 1]  # Update with the correct total weight
                    heapq.heappush(priority_queue, (min_weights[v], v))
        # Replace unreachable vertices with -1
        for i in range(2, self.N + 1):
            if min_weights[i] == float('inf'):
                min_weights[i] = -1  # Indicate unreachable vertices
        return min_weights[2:]  # Return weights from vertex 2 to N