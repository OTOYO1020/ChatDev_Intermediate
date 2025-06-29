'''
Main application file for the sequence counter.
'''
from sequence_counter import count_sequences
def main():
    # Read input values
    N = int(input("Enter N (Number of vertices): "))
    M = int(input("Enter M (Number of edges): "))
    K = int(input("Enter K (Length of sequence): "))
    S = int(input("Enter S (Start vertex): "))
    T = int(input("Enter T (End vertex): "))
    X = int(input("Enter X (Vertex to include): "))
    # Validate input ranges
    if not (1 <= S <= N) or not (1 <= T <= N) or not (1 <= X <= N):
        raise ValueError(f"Vertices S, T, and X must be in the range [1, {N}].")
    if K < 0:
        raise ValueError("K must be a non-negative integer.")
    # Read edges
    edges = []
    print("Enter edges in the format 'U,V' (space-separated for multiple edges): ")
    edges_input = input().strip().split()
    for edge in edges_input:
        try:
            u, v = map(int, edge.split(','))
            edges.append((u, v))
        except ValueError:
            print(f"Invalid edge format: '{edge}'. Expected format is U,V.")
            continue  # Skip invalid edges instead of raising an error
    # Validate the number of edges
    if len(edges) != M:
        raise ValueError(f"Expected {M} edges, but got {len(edges)} edges.")
    result = count_sequences(N, M, K, S, T, X, edges)
    print(f"Valid Sequences: {result}")
if __name__ == "__main__":
    main()