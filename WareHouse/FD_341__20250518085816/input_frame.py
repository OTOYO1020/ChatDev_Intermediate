'''
InputFrame class to handle user input for the graph parameters.
'''
from tkinter import Frame, Label, Entry, Button
from typing import List, Tuple
class InputFrame(Frame):
    def __init__(self, run_callback):
        super().__init__()
        self.run_callback = run_callback
        Label(self, text="Number of Vertices (N):").grid(row=0, column=0)
        self.n_entry = Entry(self)
        self.n_entry.grid(row=0, column=1)
        Label(self, text="Number of Edges (M):").grid(row=1, column=0)
        self.m_entry = Entry(self)
        self.m_entry.grid(row=1, column=1)
        Label(self, text="Edges (comma-separated):").grid(row=2, column=0)
        self.edges_entry = Entry(self)
        self.edges_entry.grid(row=2, column=1)
        Label(self, text="Weights (comma-separated):").grid(row=3, column=0)
        self.weights_entry = Entry(self)
        self.weights_entry.grid(row=3, column=1)
        Label(self, text="Pieces (comma-separated):").grid(row=4, column=0)
        self.pieces_entry = Entry(self)
        self.pieces_entry.grid(row=4, column=1)
        Button(self, text="Run", command=self.run_callback).grid(row=5, columnspan=2)
    def get_input(self) -> Tuple[int, int, List[Tuple[int, int]], List[int], List[int]]:
        N = int(self.n_entry.get())
        M = int(self.m_entry.get())
        edges_input = self.edges_entry.get().split(';')
        # Validate edges input
        edges = []
        for edge in edges_input:
            try:
                u, v = map(int, edge.split(','))
                if u < 0 or u >= N or v < 0 or v >= N:
                    raise ValueError("Edge vertices must be within the range of 0 to N-1.")
                edges.append((u, v))
            except ValueError as e:
                raise ValueError(f"Invalid edge format: {edge}. Error: {str(e)}")
        weights = list(map(int, self.weights_entry.get().split(',')))
        if any(weight < 0 for weight in weights):
            raise ValueError("Weights must be non-negative integers.")
        pieces = list(map(int, self.pieces_entry.get().split(',')))
        if any(piece < 0 for piece in pieces):
            raise ValueError("Pieces must be non-negative integers.")
        return N, M, edges, weights, pieces