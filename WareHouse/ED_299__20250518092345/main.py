'''
App class to create the application for the graph painting logic.
'''
import sys
from graph import Graph
from painter import Painter
class App:
    def __init__(self):
        self.input_data = self.get_input()
        self.process_input()
    def get_input(self):
        # Read input from standard input
        input_data = sys.stdin.read().strip().splitlines()
        return input_data
    def process_input(self):
        try:
            N = int(self.input_data[0])
            M = int(self.input_data[1])
            edges_input = self.input_data[2:M+2]  # Get edges input
            K = int(self.input_data[M+2])
            p = list(map(int, self.input_data[M+3].split(',')))
            d = list(map(int, self.input_data[M+4].split(',')))
            graph = Graph(N)
            edges = []
            for edge in edges_input:
                try:
                    u, v = map(int, edge.split())
                    if u < 0 or u >= N or v < 0 or v >= N:
                        raise ValueError(f"Edge vertices must be in the range [0, {N-1}]")
                    edges.append((u, v))
                except ValueError:
                    raise ValueError(f"Invalid edge format: {edge}. Expected format: 'u v'")
            for u, v in edges:
                graph.add_edge(u, v)
            painter = Painter(graph, K, p, d)
            possible, colors = painter.can_paint()
            if possible:
                print(f"Painting is possible! Colors: {colors}")
            else:
                print("Painting is not possible.")
        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    app = App()