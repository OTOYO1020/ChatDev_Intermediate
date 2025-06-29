'''
Main entry point for the Guarded Vertices application.
'''
from graph import find_guarded_vertices
def main():
    try:
        N = int(input("Enter the number of vertices (N): "))
        M = int(input("Enter the number of edges (M): "))
        edges_input = input("Enter edges (format: u,v;u,v;...): ").strip().split(';')
        # Validate edges input
        try:
            edges = [tuple(map(int, edge.split(','))) for edge in edges_input if edge]
        except ValueError:
            raise ValueError("Invalid format for edges. Please use the format: u,v;u,v;...")
        # Validate edges count
        if len(edges) != M:
            raise ValueError(f"The number of edges provided ({len(edges)}) does not match M ({M}).")
        # Validate edges
        for u, v in edges:
            if u < 0 or u >= N or v < 0 or v >= N:
                raise ValueError(f"Edge vertices must be in the range [0, {N-1}]")
        K = int(input("Enter the number of guards (K): "))
        guards_input = input("Enter guards (format: position,stamina;...): ").strip().split(';')
        # Validate guards input
        try:
            guards = [tuple(map(int, guard.split(','))) for guard in guards_input if guard]
        except ValueError:
            raise ValueError("Invalid format for guards. Please use the format: position,stamina;...")
        # Validate guards
        if K != len(guards):
            raise ValueError(f"The number of guards provided ({len(guards)}) does not match K ({K}).")
        for position, stamina in guards:
            if position < 0 or position >= N:
                raise ValueError(f"Guard position must be in the range [0, {N-1}]")
            if stamina < 0:
                raise ValueError(f"Guard stamina must be non-negative.")
        guarded_vertices = find_guarded_vertices(N, M, edges, K, guards)
        display_output(guarded_vertices)
    except ValueError as e:
        print(f"Input Error: {str(e)}")
def display_output(guarded_vertices):
    if guarded_vertices:
        print(f"Guarded Vertices: {', '.join(map(str, guarded_vertices))}")
    else:
        print("No guarded vertices found.")
if __name__ == "__main__":
    main()