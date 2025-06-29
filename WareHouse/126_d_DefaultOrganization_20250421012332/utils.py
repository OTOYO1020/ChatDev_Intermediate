'''
Utility functions for input validation.
'''
def validate_input(n, edges_input):
    '''
    Validates the user input for number of vertices and edges.
    Parameters:
    n (str): The number of vertices as a string.
    edges_input (str): The edges input as a string.
    Returns:
    bool: True if the input is valid, False otherwise.
    '''
    if not n.isdigit() or int(n) <= 0:
        print("Error: Number of vertices must be a positive integer.")
        return False
    n = int(n)
    edges = edges_input.split(',')
    if len(edges) != n - 1:  # Check if the number of edges is exactly N-1
        print(f"Error: Expected {n - 1} edges, but got {len(edges)}.")
        return False
    seen_edges = set()  # To track unique edges
    for edge in edges:
        parts = edge.strip().split()
        if len(parts) != 3 or not all(part.isdigit() for part in parts):
            print("Error: Each edge must be in the format 'u v w' where u, v, and w are integers.")
            return False
        try:
            u, v, w = map(int, parts)
        except ValueError:
            print("Error: Edge values must be integers.")
            return False
        if u < 1 or u > n or v < 1 or v > n:  # Change to 1-indexed check
            print(f"Error: Edge references invalid vertices: {u} or {v}. Valid range is 1 to {n}.")
            return False
        edge_tuple = (u - 1, v - 1)  # Convert to 0-indexed for internal processing
        if edge_tuple in seen_edges or (v - 1, u - 1) in seen_edges:
            print(f"Error: Duplicate edge detected between {u} and {v}.")
            return False
        seen_edges.add(edge_tuple)
    return True