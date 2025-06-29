'''
Main entry point for the Dijkstra's algorithm application.
'''
from graph import Graph
def main():
    # Read number of vertices and edges
    N, M = map(int, input().split())
    # Validate input for number of vertices and edges
    if N <= 0 or M < 0:
        print("Invalid input for number of vertices or edges.")
        return
    # Initialize an array to store the weights of the vertices
    A = list(map(int, input().split()))
    # Validate vertex weights input
    if len(A) != N:
        print("The number of vertex weights must match the number of vertices.")
        return
    # Initialize a list to store edges
    edges = []
    # Read edges
    for _ in range(M):
        u, v, b = map(int, input().split())
        edges.append((u, v, b))
    # Create a graph and add edges
    graph = Graph(N, A)  # Pass the vertex weights to the graph
    for u, v, b in edges:
        graph.add_edge(u, v, b)
    # Compute minimum weights from vertex 1
    distances = graph.dijkstra(1)
    # Print the minimum path weights for vertices 2 through N
    for i in range(2, N + 1):
        if distances[i] == float('inf'):
            print(f"No path from 1 to {i}")
        else:
            print(distances[i])
if __name__ == "__main__":
    main()