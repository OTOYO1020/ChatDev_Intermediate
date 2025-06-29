'''
App class to create the application for the graph painting task.
'''
import sys
from graph import Graph
class App:
    def run(self):
        # Read integers N and M from standard input
        n, m = map(int, sys.stdin.readline().strip().split())
        # Ensure that k is read from the input
        try:
            k = int(sys.stdin.readline().strip())
        except ValueError:
            print("Error: Number of Red Vertices (K) must be an integer.")
            return
        except IndexError:
            print("Error: Missing input for the number of Red Vertices (K).")
            return
        # Input validation for K
        if k <= 0:
            print("Error: Number of Red Vertices (K) must be greater than 0.")
            return
        if k > n:
            print("Error: Number of Red Vertices (K) cannot be greater than Number of Vertices (N).")
            return
        edges = []
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().strip().split())
            # Input validation for edges
            if not (1 <= u <= n and 1 <= v <= n):
                print(f"Error: Edge vertices must be between 1 and {n}.")
                return
            edges.append((u - 1, v - 1))  # Adjust for 0-indexing
        graph = Graph(n)
        for edge in edges:
            graph.add_edge(edge[0], edge[1])
        result = graph.count_ways(k)
        print(result)
if __name__ == "__main__":
    app = App()
    app.run()