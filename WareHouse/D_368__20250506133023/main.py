'''
Main entry point for the application.
'''
from graph import Graph
def main():
    # Read integers N and K from standard input
    N, K = map(int, input().split())
    graph = Graph()
    # Read N-1 edges
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph.add_edge(a, b)
    # Read K specified vertices
    required_vertices = set(map(int, input().split()))
    # Ensure that required_vertices is not empty
    if not required_vertices:
        print("No required vertices provided.")
        return
    # Call dfs starting from the first required vertex
    min_vertices, found_vertices = graph.dfs(next(iter(required_vertices)), -1, required_vertices)
    # Check if all required vertices were found
    if not required_vertices.issubset(found_vertices):
        print("Not all required vertices were found in the subtree.")
    else:
        # Print the result
        print(min_vertices)
if __name__ == "__main__":
    main()