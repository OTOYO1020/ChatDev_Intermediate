'''
Main application file for the Tree Coloring application.
'''
from tree import Tree  # Ensure Tree class is imported
def color_tree(vertex, color, tree, colors):
    """
    Colors the tree using DFS.
    Parameters:
    vertex (int): The current vertex to color.
    color (int): The color to assign (0 for white, 1 for black).
    tree (Tree): The tree structure containing the adjacency list.
    colors (list): The list storing the colors of the vertices, initialized with -1 for uncolored.
    """
    # Check if the vertex is within bounds
    if vertex < 1 or vertex > len(colors) - 1:
        return
    # If the current vertex is already colored, check for conflicts
    if colors[vertex] != -1:
        if colors[vertex] == color:
            raise ValueError("Conflict detected: adjacent vertices cannot have the same color.")
        return
    # Color the current vertex
    colors[vertex] = color
    # Recursively color all adjacent vertices with the opposite color
    for neighbor in tree[vertex]:  # Accessing adjacency list using __getitem__
        color_tree(neighbor, 1 - color, tree, colors)
def is_connected(tree, n):
    """
    Checks if the tree is connected using DFS.
    Parameters:
    tree (Tree): The tree structure containing the adjacency list.
    n (int): The number of vertices in the tree.
    Returns:
    bool: True if the tree is connected, False otherwise.
    """
    visited = [False] * (n + 1)
    def dfs(vertex):
        visited[vertex] = True
        for neighbor in tree[vertex]:  # Accessing adjacency list using __getitem__
            if not visited[neighbor]:
                dfs(neighbor)
    dfs(1)  # Start DFS from vertex 1
    return all(visited[1:])  # Check if all vertices are visited
def main():
    # Read number of vertices
    n = int(input())
    tree = Tree(n)
    # Read edges and populate the tree
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        if u < 1 or u > n or v < 1 or v > n:
            print(f"Error: Vertex indices must be between 1 and {n}.")
            return
        tree.add_edge(u, v, w)
    # Check if the tree is connected
    if not is_connected(tree, n):
        print("Error: The tree is not connected.")
        return
    # Initialize colors array with -1 to indicate uncolored
    colors = [-1] * (n + 1)  # Change initialization to -1
    # Start coloring from vertex 1 with color 0 (white)
    try:
        color_tree(1, 0, tree, colors)
    except ValueError as e:
        print(f"Error: {e}")
        return
    # Prepare output
    colors_output = ' '.join(str(color) for color in colors[1:])  # Output all colors
    print(colors_output)
if __name__ == "__main__":
    main()