'''
Main entry point for the Graph Edge Remover application.
'''
from edge_calculator import min_edges_to_remove
if __name__ == "__main__":
    # Read input values
    N = int(input("Enter the number of vertices (N): "))
    M = int(input("Enter the number of edges (M): "))
    edges_input = input("Enter the edges (format: u,v;u,v;...): ")
    # Handle the case when M is zero
    if M == 0:
        print("Edges to remove: 0")
    else:
        # Parse edges with validation and consistent ordering
        try:
            edges = [tuple(map(int, edge.split(','))) for edge in edges_input.split(';')]
            # Remove duplicates by converting to a set
            edges = list(set(edges))
        except ValueError:
            raise ValueError("Invalid edge format. Please use the format u,v;u,v;... where u and v are integers.")
        # Validate the number of edges
        if len(edges) > M:
            print(f"Warning: Found {len(edges)} unique edges, which is more than the specified M={M}. Duplicates were removed.")
        # Validate edge values
        for u, v in edges:
            if not (0 <= u < N and 0 <= v < N):
                raise ValueError(f"Edge ({u}, {v}) is out of bounds for the number of vertices N={N}.")
        # Calculate and print the result
        result = min_edges_to_remove(N, M, edges)
        print(f"Edges to remove: {result}")