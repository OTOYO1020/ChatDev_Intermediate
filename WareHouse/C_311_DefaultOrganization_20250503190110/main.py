'''
Main entry point for the cycle detection application.
'''
from graph import Graph
def main():
    # Read the number of vertices
    N = int(input("Enter the number of vertices: "))
    # Initialize the graph
    graph = Graph(N)
    # Read edges directly into the array A
    print("Enter the edges (one integer per vertex, format: A[i] for vertex i):")
    A = list(map(int, input().split()))
    if len(A) != N:
        raise ValueError("The number of edges must match the number of vertices.")
    for i in range(N):
        graph.add_edge(i + 1, A[i])  # Adjust for 1-based indexing
    # Detect cycles
    cycles = graph.detect_cycle()
    if cycles:
        print("Cycles found:")
        for cycle in cycles:
            print(cycle)
    else:
        print("No cycles found.")
if __name__ == "__main__":
    main()