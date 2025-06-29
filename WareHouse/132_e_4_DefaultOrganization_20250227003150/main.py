'''
Main entry point of the application that reads input and finds the shortest path in a graph.
'''
from collections import deque, defaultdict
import sys
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = defaultdict(list)
    def add_edge(self, u, v):
        # Create edges for the three-layer structure
        for i in range(3):
            self.adj[(u, i)].append((v, (i + 1) % 3))
            self.adj[(v, i)].append((u, (i + 1) % 3))
    def bfs(self, start, target):
        queue = deque([(start, 0)])  # Start from (S, 0)
        visited = set()
        while queue:
            current, distance = queue.popleft()
            if current == (target, 0):
                return distance  # Return the distance directly
            if current not in visited:
                visited.add(current)
                for neighbor in self.adj[current]:
                    if neighbor not in visited:  # Check if neighbor is not visited
                        queue.append((neighbor, distance + 1))  # Increment distance for each step
        return -1
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])  # Number of vertices
    M = int(input_data[1])  # Number of edges
    edges = input_data[2:M + 2]  # Edges
    S = int(input_data[M + 2])  # Starting vertex
    T = int(input_data[M + 3])  # Target vertex
    graph = Graph(N)
    for edge in edges:
        u, v = map(int, edge.split())
        graph.add_edge(u, v)
    result = graph.bfs(S, T)
    if result != -1:
        print(result // 3)  # Divide by 3 only when outputting
    else:
        print(result)
if __name__ == "__main__":
    main()