'''
Main entry point for the application.
'''
from graph import Graph
import sys
def main():
    input = sys.stdin.read
    data = input().splitlines()
    # Read number of vertices and edges
    try:
        N, M = map(int, data[0].split())
    except ValueError:
        print("Invalid input format for number of vertices and edges. Expected format: N M.")
        return
    # Input validation
    if N <= 0 or M < 0:
        print("Number of vertices must be positive and number of edges cannot be negative.")
        return
    # Edge count validation
    if M < N - 1:
        print("Not enough edges to form a valid MST. At least N-1 edges are required.")
        return
    # Initialize the graph
    graph = Graph(N)
    # Read edges
    read_edges(graph, data, M)
    # Compute the MST after adding all edges
    mst_valid, mst_edges = graph.find_mst()
    if not mst_valid:
        return  # Exit if the MST cannot be formed
    # Read number of queries
    try:
        Q = int(data[M + 1])
    except ValueError:
        print("Invalid input format for number of queries. Expected an integer.")
        return
    # Input validation for queries
    if Q < 0:
        print("Number of queries cannot be negative.")
        return
    # Read queries
    queries = []
    read_queries(queries, data, M, Q, graph)  # Pass graph to read_queries
    # Process each query
    results = []
    for query in queries:
        u, v, w = query
        edge = (u, v, w)  # Create edge in the format (a, b, weight)
        if graph.is_edge_in_mst(edge, mst_edges):  # Check if edge is in MST
            results.append("Yes")
        else:
            results.append("No")
    # Print results
    print("\n".join(results))
def read_edges(graph, data, M):
    for i in range(1, M + 1):
        try:
            a, b, c = map(int, data[i].split())
            if 1 <= a <= graph.V and 1 <= b <= graph.V:
                graph.add_edge(a, b, c)
            else:
                print(f"Invalid edge ({a}, {b}) - vertices must be between 1 and {graph.V}.")
        except ValueError:
            print(f"Invalid input format for edge at line {i + 1}. Expected format: a b c.")
def read_queries(queries, data, M, Q, graph):  # Accept graph as a parameter
    for i in range(M + 2, M + 2 + Q):
        try:
            u, v, w = map(int, data[i].split())
            if 1 <= u <= graph.V and 1 <= v <= graph.V:  # Use graph.V instead of queries.V
                queries.append((u, v, w))
            else:
                print(f"Invalid query ({u}, {v}) - vertices must be between 1 and {graph.V}.")
        except ValueError:
            print(f"Invalid input format for query at line {i + 1}. Expected format: u v w.")
if __name__ == "__main__":
    main()