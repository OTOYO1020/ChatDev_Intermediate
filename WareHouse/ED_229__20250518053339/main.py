'''
Main entry point for the connected components application.
'''
from typing import List, Tuple
from graph import Graph
def count_connected_components(N: int, M: int, edges: List[Tuple[int, int]]) -> List[int]:
    if N == 0 or M == 0:
        return [0] * N  # Return a list of zeros if there are no vertices or edges
    graph = Graph(N, edges)
    results = []
    for vertex in range(1, N + 1):
        edges_to_restore = graph.delete_vertex(vertex)  # Delete the vertex and get edges
        results.append(graph.count_connected_components())  # Count components after deletion
        graph.restore_vertex(vertex, edges_to_restore)  # Restore the deleted vertex and edges
    return results
if __name__ == "__main__":
    try:
        N = int(input("Enter number of vertices (N): "))
        M = int(input("Enter number of edges (M): "))
        edges_input = input("Enter edges (e.g., 1 2, 2 3): ")
        edges = [tuple(map(int, edge.split())) for edge in edges_input.split(',') if edge.strip()]
        results = count_connected_components(N, M, edges)
        print(f"Connected components after deletion: {results}")
    except ValueError:
        print("Invalid input. Please enter integers for N and M, and valid edges.")