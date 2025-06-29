'''
Main application file to run the graph query application.
'''
from graph import Graph
def main():
    # Read number of vertices and edges
    N, M = map(int, input().split())
    if N < 0 or M < 0:
        raise ValueError("Number of vertices and edges must be non-negative integers.")
    graph = Graph(N)
    # Read edges and build the graph
    for _ in range(M):
        a, b = map(int, input().split())
        try:
            graph.add_edge(a, b)
        except ValueError as e:
            print(e)  # Print error message if edge cannot be added
    # Read number of queries
    Q = int(input())
    results = []
    # Process each query
    for _ in range(Q):
        x, k = map(int, input().split())
        result = graph.sum_of_indices_within_distance(x, k)
        results.append(result)
    # Print results for each query
    for res in results:
        print(res)
if __name__ == "__main__":
    main()