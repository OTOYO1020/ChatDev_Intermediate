'''
InputHandler class to parse input data for the tree distance application.
'''
class InputHandler:
    def __init__(self, input_data):
        self.input_data = input_data
    def parse_input(self):
        lines = self.input_data.splitlines()
        n = int(lines[0].strip())
        if n < 1:
            raise ValueError("Number of vertices must be at least 1.")
        edges = []
        for i in range(1, n):
            if i >= len(lines):
                raise ValueError("Not enough edges provided.")
            a, b = map(int, lines[i].strip().split())
            edges.append((a, b))
        if len(edges) != n - 1:
            raise ValueError("The number of edges must be exactly N-1.")
        C = list(map(int, lines[n].strip().split()))
        if len(C) != n:
            raise ValueError("The sequence C must contain exactly N integers.")
        return n, edges, C