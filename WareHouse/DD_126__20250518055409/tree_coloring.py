'''
Contains the logic for coloring the tree based on levels.
'''
from typing import List, Tuple
from collections import defaultdict, deque
def color_tree(N: int, edges: List[Tuple[int, int, int]]) -> List[str]:
    # Check for the case where all vertices can be painted the same color
    if N == 1:
        return ['white']
    if N == 2 and len(edges) == 1:
        return ['white', 'white']  # Both vertices can be colored the same
    # Validate the number of edges
    if len(edges) != N - 1:
        raise ValueError("The number of edges must be exactly N - 1 for a tree.")
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append(v)
        graph[v].append(u)
    # Ensure vertex 1 is in the graph
    if 1 not in graph:
        raise ValueError("Vertex 1 is not connected; it does not form a valid tree.")
    colors = [''] * (N + 1)
    visited = [False] * (N + 1)
    queue = deque([(1, 0)])  # Start from vertex 1
    while queue:
        vertex, level = queue.popleft()
        if visited[vertex]:
            continue
        visited[vertex] = True
        colors[vertex] = 'white' if level % 2 == 0 else 'black'
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append((neighbor, level + 1))
    # Check if all vertices were visited
    if not all(visited[1:N + 1]):
        raise ValueError("The graph is not connected; it does not form a valid tree.")
    return colors[1:]