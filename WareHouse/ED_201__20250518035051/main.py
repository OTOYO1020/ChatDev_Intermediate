'''
Main application file for the XOR Distance Calculator.
'''
from xor_distance import calculate_xor_distances
def main():
    try:
        N = int(input("Enter number of vertices (N): "))
        edges_input = input("Enter edges (u, v, w) separated by semicolons: ")
        edges = [tuple(map(int, edge.split(','))) for edge in edges_input.split(';')]
        # Validate edges
        if len(edges) < N - 1:
            raise ValueError("Not enough edges to form a connected tree.")
        if any(len(edge) != 3 for edge in edges):
            raise ValueError("Each edge must contain exactly three integers (u, v, w).")
        # Validate that all vertices are within the range of 1 to N
        for u, v, w in edges:
            if not (1 <= u <= N and 1 <= v <= N):
                raise ValueError(f"Vertices {u} and {v} must be between 1 and {N}.")
        result = calculate_xor_distances(N, edges)
        print(f"Total XOR Distance: {result}")
    except ValueError as ve:
        print("Input Error:", str(ve))
    except Exception as e:
        print("An unexpected error occurred:", str(e))
if __name__ == "__main__":
    main()