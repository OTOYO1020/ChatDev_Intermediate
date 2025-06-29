'''
Main application file for the Tree XOR Distance Calculator.
'''
import sys
from graph import Graph
def main():
    # Read the number of vertices (N)
    N = int(input())
    # Initialize the graph
    graph = Graph(N)
    # Read edges and populate the graph
    for _ in range(N - 1):
        u, v, w = map(int, input().strip().split())
        graph.add_edge(u, v, w)
    # Calculate total XOR distance
    total_sum = graph.calculate_total_xor_distance()
    # Print the final result
    print(total_sum)
if __name__ == "__main__":
    main()