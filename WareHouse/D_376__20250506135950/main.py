'''
Main file to run the graph cycle detection application using standard input and output.
'''
from graph import Graph
def main():
    n = int(input())  # Read number of vertices
    m = int(input())  # Read number of edges
    # Input validation
    if n <= 0:
        print("Number of vertices must be a positive integer.")
        return
    if m < 0:
        print("Number of edges cannot be negative.")
        return
    if m == 0:
        print("No edges exist, thus no cycles can be detected.")
        return
    graph = Graph(n)
    for _ in range(m):
        a, b = map(int, input().split())  # Read edges
        if a < 1 or a > n or b < 1 or b > n:
            print(f"Invalid edge ({a}, {b}). Vertices must be between 1 and {n}.")
            return
        graph.add_edge(a, b)
    result = graph.detect_cycle()
    print(result)
if __name__ == "__main__":
    main()