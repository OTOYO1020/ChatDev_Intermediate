'''
Main application file for the Tree Coloring program.
'''
from collections import defaultdict
from utils import validate_input
def main():
    while True:
        n = input("Enter the number of vertices (N): ")
        edges_input = input("Enter the edges (format: u v w, separated by commas): ")
        # Validate input
        if not validate_input(n, edges_input):
            continue  # Prompt again for input
        n = int(n)  # Convert to integer after validation
        try:
            edges = [tuple(map(int, edge.strip().split())) for edge in edges_input.split(',') if edge.strip()]
            # Ensure that each edge has exactly three components
            if any(len(edge) != 3 for edge in edges):
                print("Error: Each edge must be in the format 'u v w' where u, v, and w are integers.")
                continue  # Prompt again for input
            # Convert to 0-indexed
            edges = [(u - 1, v - 1, w) for u, v, w in edges]
        except ValueError:
            print("Error parsing edges. Please ensure they are in the correct format.")
            continue  # Prompt again for input
        colors = color_tree(n, edges)
        if colors:  # Only print colors if coloring was successful
            for color in colors:
                print(color)
        break  # Exit the loop after successful processing
def color_tree(n, edges):
    '''
    Colors the tree based on the edges provided.
    '''
    graph = defaultdict(list)
    seen_edges = set()  # To track unique edges
    for edge in edges:
        try:
            u, v, w = edge  # Ensure edge is unpacked correctly
        except ValueError:
            print("Error: Each edge must be a tuple of three integers (u, v, w).")
            return []  # Early exit on invalid edge format
        edge_tuple = (u, v)
        if edge_tuple in seen_edges or (v, u) in seen_edges:
            print(f"Error: Duplicate edge detected between {u} and {v}.")
            return []  # Early exit on duplicate edge
        seen_edges.add(edge_tuple)
        graph[u].append((v, w))
        graph[v].append((u, w))
    # Check for connectivity and acyclic nature
    visited = [False] * n
    def dfs_check(node):
        visited[node] = True
        for neighbor, _ in graph[node]:
            if not visited[neighbor]:
                dfs_check(neighbor)
    dfs_check(0)  # Start DFS from the root (vertex 0)
    if not all(visited):
        print("Error: The graph is not connected. Please ensure it forms a valid tree.")
        return []  # Early exit if the graph is not connected
    colors = [-1] * n  # -1 means undefined
    colors[0] = 0  # Start coloring from vertex 0 (white)
    def dfs(node, color):
        '''
        Depth-First Search to color the tree.
        Parameters:
        node (int): The current vertex being visited.
        color (int): The color assigned to the current vertex (0 or 1).
        '''
        for neighbor, weight in graph[node]:
            if colors[neighbor] == -1:  # Check if the neighbor is unvisited
                colors[neighbor] = color if weight % 2 == 0 else 1 - color
                dfs(neighbor, colors[neighbor])
            elif colors[neighbor] != -1:  # Check if the neighbor has been visited
                expected_color = color if weight % 2 == 0 else 1 - color
                if colors[neighbor] != expected_color:
                    print("Error: Invalid coloring detected due to odd-weight edge.")
                    return []  # Early exit on invalid coloring
    dfs(0, colors[0])
    return colors
if __name__ == "__main__":
    main()