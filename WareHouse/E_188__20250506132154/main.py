'''
Main application file for the gold profit calculator.
'''
import sys
from graph import Graph
from utils import max_profit
def main():
    try:
        # Read integers N and M from standard input
        N, M = map(int, input().split())
        # Read the array A of length N
        prices = list(map(int, input().split()))
        # Initialize a graph representation to store the roads
        graph = Graph(N)
        # Read the pairs (X_i, Y_i) and populate the graph
        for _ in range(M):
            u, v = map(int, input().split())
            if 1 <= u <= N and 1 <= v <= N:  # Validate input range
                graph.add_edge(u - 1, v - 1)  # Adjusting to zero-based indexing
            else:
                raise ValueError(f"Town indices {u} and {v} are out of range (1 to {N}).")
        # Calculate maximum profit
        profit = max_profit(N, graph, prices)
        # Print the maximum profit as the final output
        print(profit)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
if __name__ == "__main__":
    main()