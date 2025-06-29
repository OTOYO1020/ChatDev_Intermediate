'''
Main application file for the Graph Path Checker.
'''
from typing import List, Tuple
def dfs(vertex: int, graph: dict, visited: set, parent: int) -> bool:
    '''
    Depth-first search to check connectivity and cycles.
    '''
    visited.add(vertex)
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            if not dfs(neighbor, graph, visited, vertex):
                return False
        elif neighbor != parent:  # A cycle is detected
            return False
    return True
def is_path_graph(N: int, M: int, edges: List[Tuple[int, int]]) -> bool:
    '''
    Determines if the given graph is a path graph.
    '''
    # A path graph must have exactly N - 1 edges
    if M != N - 1:
        return False
    # Initialize graph with all vertices
    graph = {i: [] for i in range(1, N + 1)}
    visited = set()
    edge_set = set()
    for u, v in edges:
        # Check for valid vertex range
        if u < 1 or u > N or v < 1 or v > N:
            raise ValueError(f"Vertex {u} or {v} is out of the valid range (1 to {N}).")
        # Check for self-loops
        if u == v:
            raise ValueError("Graph cannot have self-loops.")
        # Check for multiple edges
        if (u, v) in edge_set or (v, u) in edge_set:
            raise ValueError("Graph cannot have multiple edges.")
        edge_set.add((u, v))
        graph[u].append(v)
        graph[v].append(u)
    # Start DFS from the first vertex in edges
    start_vertex = edges[0][0]
    if not dfs(start_vertex, graph, visited, -1):  # Pass -1 as parent for the root
        return False
    # Check if all vertices are visited
    if len(visited) != N:
        return False
    # Check degrees of vertices
    degree_one_count = 0
    for vertex in graph:
        degree = len(graph[vertex])
        if degree > 2:
            return False
        if degree == 1:
            degree_one_count += 1
    # A path graph must have exactly two vertices with degree 1
    return degree_one_count == 2 and all(len(graph[v]) <= 2 for v in graph if v not in (edges[0][0], edges[-1][1]))
if __name__ == "__main__":
    '''
    Entry point of the application.
    '''
    N = int(input("Enter the number of vertices (N): "))
    M = int(input("Enter the number of edges (M): "))
    edges_input = input("Enter edges (u v) separated by commas: ")
    edges = [tuple(map(int, edge.split())) for edge in edges_input.split(",")]
    # Validate the number of edges
    if len(edges) != M:
        print(f"Input Error: The number of edges provided ({len(edges)}) does not match M ({M}).")
    else:
        try:
            result = is_path_graph(N, M, edges)
            print(f"Is path graph: {result}")
        except Exception as e:
            print(f"Input Error: {str(e)}")