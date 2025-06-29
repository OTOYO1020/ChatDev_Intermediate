'''
Module for calculating XOR distances in a tree structure.
'''
from collections import defaultdict
def calculate_xor_distances(N: int, edges: list) -> int:
    MOD = 10**9 + 7
    if N < 1:
        raise ValueError("The number of vertices N must be at least 1.")
    if N == 1:
        return 0  # No edges, hence no XOR distance
    graph = defaultdict(list)
    edge_set = set()  # To track unique edges
    # Build the adjacency list
    for u, v, w in edges:
        if (u, v, w) in edge_set or (v, u, w) in edge_set:
            raise ValueError(f"Duplicate edge found: ({u}, {v}, {w})")
        edge_set.add((u, v, w))
        graph[u].append((v, w))
        graph[v].append((u, w))
    # Check if the number of edges is exactly N - 1
    if len(edges) != N - 1:
        raise ValueError("The number of edges must be exactly N - 1 for a connected tree.")
    # Check if all vertices from 1 to N are present in the graph
    if any(i not in graph for i in range(1, N + 1)):
        raise ValueError("Not all vertices from 1 to N are present in the edges provided.")
    # Check if the graph is connected after building it
    if not is_connected(graph, N):
        raise ValueError("The graph is not connected. Please provide a valid tree structure.")
    # To store the XOR distance from the root and parent information
    xor_distance = [0] * (N + 1)
    parent = [-1] * (N + 1)
    depth = [0] * (N + 1)
    def dfs(node, par, current_xor, current_depth):
        parent[node] = par
        xor_distance[node] = current_xor
        depth[node] = current_depth
        for neighbor, weight in graph[node]:
            if neighbor != par:
                dfs(neighbor, node, current_xor ^ weight, current_depth + 1)
    # Start DFS from the first node in the edges (or any node)
    start_node = edges[0][0]  # or any node present in the edges
    dfs(start_node, -1, 0, 0)
    total_xor_distance = 0
    # Function to find the Lowest Common Ancestor (LCA)
    def find_lca(u, v):
        # Check if u and v are valid nodes
        if u < 1 or u > N or v < 1 or v > N or parent[u] == -1 or parent[v] == -1:
            raise ValueError(f"Nodes {u} and {v} must be valid nodes in the range 1 to {N} and must be connected.")
        # Move u and v to the same level
        while depth[u] > depth[v]:
            u = parent[u]
        while depth[v] > depth[u]:
            v = parent[v]
        # Move both u and v up until they meet
        while u != v:
            u = parent[u]
            v = parent[v]
        return u
    # Calculate total XOR distances for all pairs (i, j)
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            lca = find_lca(i, j)
            path_xor = xor_distance[i] ^ xor_distance[j] ^ xor_distance[lca]
            total_xor_distance = (total_xor_distance + path_xor) % MOD
    return total_xor_distance
def is_connected(graph, N):
    visited = [False] * (N + 1)
    def dfs(node):
        visited[node] = True
        for neighbor, _ in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    # Start DFS from the first node in the graph
    start_node = next(iter(graph), None)
    if start_node is not None:
        dfs(start_node)  # Start DFS from a valid node
    return all(visited[1:N + 1])  # Check if all nodes from 1 to N are visited