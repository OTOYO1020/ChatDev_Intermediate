'''
Main application file for counting level-k stars in a tree.
'''
import sys
from tree_star_counter import TreeStarCounter
def is_connected(tree_counter):
    if tree_counter.n == 0:  # Check if there are no vertices
        return False
    if not tree_counter.adjacency_list:  # Check if the adjacency list is empty
        return False
    visited = set()
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in tree_counter.adjacency_list[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
    # Start DFS from the first vertex that exists in the adjacency list
    start_vertex = next(iter(tree_counter.adjacency_list))  # Get any vertex from the adjacency list
    dfs(start_vertex)
    return len(visited) == tree_counter.n  # Ensure all vertices are visited
def main():
    '''
    Main function to read input and calculate star count.
    '''
    try:
        n = int(input())
        if n < 2:
            raise ValueError("The number of vertices must be at least 2.")
        edges = set()  # Use a set to avoid duplicate edges
        for _ in range(n - 1):
            try:
                u, v = map(int, input().split())
                if u < 1 or u > n or v < 1 or v > n:
                    raise ValueError(f"Vertices must be in the range 1 to {n}.")
                if u == v:  # Check for self-loops
                    raise ValueError(f"Self-loops are not allowed: ({u}, {v}).")
                if (u, v) in edges or (v, u) in edges:
                    raise ValueError(f"Duplicate edge detected: ({u}, {v}).")
                edges.add((u, v))
            except ValueError as ve:
                print(f"Input Error: {str(ve)}", file=sys.stderr)
                return  # Exit the function if input is invalid
        # Check if the number of edges is correct
        if len(edges) != n - 1:
            raise ValueError("The number of edges must be exactly N-1 for a tree.")
        tree_counter = TreeStarCounter(n)
        for u, v in edges:
            tree_counter.add_edge(u, v)
        # Check if the tree is connected
        if not is_connected(tree_counter):
            raise ValueError("The edges do not form a connected tree.")
        star_count = tree_counter.count_stars()
        print(star_count)
    except Exception as e:
        print(f"Input Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()