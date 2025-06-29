'''
Application class to check if the graph is a path graph using standard input and output.
'''
import sys
from graph import Graph
class App:
    def run(self):
        # Read integers N and M from standard input
        N, M = map(int, sys.stdin.readline().strip().split())
        # Input validation for N and M
        if N < 1 or M < 0:
            print("NO")
            return
        graph = Graph(N)
        # Read edges one by one
        for _ in range(M):
            try:
                u, v = map(int, sys.stdin.readline().strip().split())
                if u == v:  # Prevent self-loops
                    print("NO")
                    return
                graph.add_edge(u, v)
            except ValueError:
                print("NO")
                return
        # Check if the graph is a path graph and print the result
        result = "YES" if graph.is_path_graph() else "NO"
        print(result)
if __name__ == "__main__":
    app = App()
    app.run()