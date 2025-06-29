'''
Main entry point for the minimum path weights application.
'''
from graph import Graph
from typing import List, Tuple
def find_minimum_path_weights(N: int, M: int, A: List[int], edges: List[Tuple[int, int, int]]) -> List[int]:
    graph = Graph(N, M, A)
    for edge in edges:
        u, v, weight = edge
        graph.add_edge(u, v, weight)
    return graph.dijkstra()
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    try:
        N = int(input_data[0])
        M = int(input_data[1])
        if N <= 0 or M <= 0:
            raise ValueError("Number of vertices (N) and edges (M) must be positive integers.")
        A = list(map(int, input_data[2].split(',')))
        if len(A) != N:
            raise ValueError("The number of vertex weights must match the number of vertices (N).")
        edges = []
        for line in input_data[3:]:
            if len(edges) >= M:  # Only process M edges
                break
            try:
                parts = line.split(',')
                if len(parts) != 3:
                    raise ValueError(f"Edge must contain exactly three values: {line}.")
                u, v, weight = map(int, parts)
                if u < 1 or u > N or v < 1 or v > N:
                    raise ValueError(f"Vertex indices must be between 1 and {N}.")
                if weight <= 0:  # Assuming weights must be positive
                    raise ValueError(f"Edge weight must be a positive integer: {weight}.")
                edges.append((u, v, weight))
            except ValueError as ve:
                raise ValueError(f"Invalid edge format or values: {line}. Error: {str(ve)}")
        if len(edges) != M:
            raise ValueError("The number of edges provided does not match M.")
        results = find_minimum_path_weights(N, M, A, edges)
        print("Minimum Path Weights:", ', '.join(map(str, results)))
    except Exception as e:
        print("Input Error:", str(e))