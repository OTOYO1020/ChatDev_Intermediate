'''
Main application file for the topological sorting application.
'''
import sys
from graph import Graph
def main():
    '''
    Main function to handle input and output for the topological sort.
    '''
    input = sys.stdin.read
    data = input().strip().splitlines()
    # Read N and M
    n, m = map(int, data[0].split())
    # Handle edge cases
    if n < 1:
        print("Error: N must be a positive integer.")
        return
    if m < 0:
        print("Error: M must be a non-negative integer.")
        return
    if m == 0:
        print(" ".join(map(str, range(1, n + 1))))  # Print numbers from 1 to N
        return
    constraints = [tuple(map(int, line.split())) for line in data[1:m+1]]
    graph = Graph(n)
    for a, b in constraints:
        if a < 1 or a > n or b < 1 or b > n:
            print("Error: Constraints must be within the range of 1 to N.")
            return
        if a == b:
            print("Error: Self-loops are not allowed.")
            return
        if (a, b) in graph.edges:  # Check for duplicate edges
            print("Error: Duplicate edges are not allowed.")
            return
        graph.add_edge(a, b)
    result = graph.topological_sort()
    if result == -1:
        print("-1")
    else:
        print(" ".join(map(str, result)))
if __name__ == "__main__":
    main()