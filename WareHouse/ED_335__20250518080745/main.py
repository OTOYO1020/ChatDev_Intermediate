'''
Main entry point for the application.
'''
from graph import Graph
def main():
    # Read input from standard input
    n = int(input("Enter number of vertices (N): "))
    m = int(input("Enter number of edges (M): "))
    edges = []
    print("Enter edges (U, V) separated by semicolons (e.g., '1,2;2,3'):")
    edge_input = input().strip().split(';')
    for edge in edge_input:
        u, v = map(int, edge.split(','))
        edges.append((u, v))
    print("Enter values (A) for each vertex separated by commas (e.g., '1,2,3'):")
    values = list(map(int, input().strip().split(',')))
    # Validate the number of edges
    if len(edges) != m:
        print(f"Error: Expected {m} edges, but got {len(edges)}.")
        return
    # Validate vertices and edges
    if n < 1 or m < 0 or len(values) != n:
        print("Error: Invalid input for vertices or edges.")
        return
    # Validate edges to ensure they are within the range of vertices
    for u, v in edges:
        if u < 1 or u > n or v < 1 or v > n:
            print("Error: Edge vertices must be between 1 and N.")
            return
    graph = Graph(n, edges, values)
    max_score = graph.find_max_score_path()
    print(f"Maximum Score: {max_score}")
if __name__ == "__main__":
    main()