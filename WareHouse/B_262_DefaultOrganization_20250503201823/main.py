'''
Application class to input graph data and display results using standard input/output.
'''
from graph import Graph
class App:
    def run(self):
        # Read integers N and M from standard input
        N, M = map(int, input().split())
        graph = Graph(N)
        for _ in range(M):
            u, v = map(int, input().split())
            graph.add_edge(u, v)
        triangle_count = graph.count_triangles()
        print(triangle_count)
if __name__ == "__main__":
    app = App()
    app.run()