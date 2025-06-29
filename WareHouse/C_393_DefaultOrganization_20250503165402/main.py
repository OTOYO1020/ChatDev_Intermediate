'''
Main entry point for the Graph Edge Counter application.
This program reads the number of vertices and edges, followed by pairs of edges,
and counts the number of edges that need to be removed to make the graph simple.
'''
from edge_counter import EdgeCounter  # Ensure this line is present
def main():
    # Read the number of vertices (N) and edges (M)
    try:
        n = int(input("Enter the number of vertices (N): "))
        m = int(input("Enter the number of edges (M): "))
        if n <= 0 or m < 0:
            raise ValueError("N must be positive and M must be non-negative.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    edge_list = []
    for i in range(m):
        while True:  # Loop until valid input is received
            try:
                u, v = map(int, input(f"Enter edge {i + 1} (format: u v): ").split())
                if u < 1 or u > n or v < 1 or v > n:
                    raise ValueError(f"Vertices must be between 1 and {n}.")
                if u == v:
                    raise ValueError("Self-loops are not allowed.")
                edge_list.append((u, v))
                break  # Exit the loop if input is valid
            except ValueError as e:
                print(f"Invalid edge input: {e}. Please try again.")
    # Initialize the EdgeCounter
    edge_counter = EdgeCounter()
    # Count the number of edges to remove to make the graph simple
    removal_count = edge_counter.count_edges_to_remove(edge_list)
    # Output the result
    print(removal_count)
if __name__ == "__main__":
    main()