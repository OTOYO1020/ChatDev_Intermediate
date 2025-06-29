'''
GraphApp class to handle the graph operations without a GUI.
'''
from graph import Graph
class GraphApp:
    def __init__(self):
        self.graph = None
    def run(self):
        n = int(input("Enter the number of vertices (N): "))
        m = int(input("Enter the number of edges (M): "))
        edges = input("Enter the edges (A B): ").strip().split()
        if len(edges) != 2 * m:
            raise ValueError("Number of edges does not match the input.")
        # Initialize the graph
        self.graph = Graph(n)
        for i in range(m):
            a = int(edges[2 * i])
            b = int(edges[2 * i + 1])
            if 1 <= a <= n and 1 <= b <= n:
                self.graph.add_edge(a, b)
            else:
                raise ValueError(f"Edge vertices {a} and {b} must be between 1 and {n}.")
        components_count = []
        for i in range(1, n + 1):
            deleted = {i}
            components_count.append(self.graph.count_connected_components(deleted))
        print("Connected Components: " + " ".join(map(str, components_count)))