'''
Main entry point for the graph coloring application.
'''
from graph import Graph
def main():
    N = int(input("Enter the number of vertices: "))
    if N < 1:
        print("The number of vertices must be at least 1.")
        return
    graph = Graph(N)
    print("Enter the edges (u v w) for N-1 edges:")
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        if u < 0 or u >= N or v < 0 or v >= N:
            print(f"Invalid edge ({u}, {v}). Vertices must be in the range 0 to {N-1}.")
            return
        graph.add_edge(u, v, w)
    graph.color_graph()
    for color in graph.colors:
        print(color)
if __name__ == "__main__":
    main()