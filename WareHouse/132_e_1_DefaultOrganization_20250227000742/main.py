'''
Main entry point for the shortest path application.
'''
from collections import deque, defaultdict
import sys
from graph import Graph  # Importing the Graph class from graph.py
def main():
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])  # Number of vertices
    M = int(data[1])  # Number of edges
    S = int(data[2])  # Starting vertex
    T = int(data[3])  # Target vertex
    # Validate S and T
    if S < 1 or S > N or T < 1 or T > N:
        print(-1)
        return
    graph = Graph(N * 3)  # Create a graph with 3 layers
    for i in range(M):
        u, v = map(int, data[4 + i].split())
        # Add edges for the three-layer structure
        for j in range(3):
            graph.add_edge((u, j), (v, j))  # Same layer edges
            graph.add_edge((u, j), (v, (j + 1) % 3))  # Transition to next layer
    result = graph.bfs((S, 0), (T, 0))
    print(result)  # Output the result
if __name__ == "__main__":
    main()