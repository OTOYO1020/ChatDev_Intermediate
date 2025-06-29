'''
Main entry point for the tree counter application.
'''
import sys
from tree import Tree
def main():
    # Read all input at once
    input_data = sys.stdin.read().strip().splitlines()
    # Read integers N and Q from the first line
    n, q = map(int, input_data[0].strip().split())
    # Validate input values
    if not (1 <= n <= 100000) or not (1 <= q <= 100000):
        raise ValueError("N and Q must be between 1 and 100000.")
    # Initialize the Tree structure
    tree = Tree(n)
    # Create the adjacency list 'tree' using N-1 edges
    for i in range(1, n):
        a, b = map(int, input_data[i].strip().split())
        if not (1 <= a <= n) or not (1 <= b <= n):
            raise ValueError("Edge vertices must be between 1 and N.")
        tree.add_edge(a, b)
    # For each operation j from 1 to Q
    for i in range(n + 1, n + 1 + q):  # Start reading operations after edges
        p, x = map(int, input_data[i].strip().split())
        if not (1 <= p <= n):
            raise ValueError("Vertex p must be between 1 and N.")
        tree.update_counters(p, x)
    # Finalize the counters after processing all operations
    tree.finalize_counters(1)  # You can change this to any valid root based on input
    # Output the final values of the 'counters' array
    results = tree.get_counters()
    for count in results:
        print(count)
if __name__ == "__main__":
    main()