'''
App class to create the GUI for the minimum path weights application.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
class App:
    def __init__(self, master):
        self.master = master
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.master, text="Number of Vertices (N):").grid(row=0, column=0)
        self.n_entry = tk.Entry(self.master)
        self.n_entry.grid(row=0, column=1)
        tk.Label(self.master, text="Number of Edges (M):").grid(row=1, column=0)
        self.m_entry = tk.Entry(self.master)
        self.m_entry.grid(row=1, column=1)
        tk.Label(self.master, text="Vertex Weights (A):").grid(row=2, column=0)
        self.a_entry = tk.Entry(self.master)
        self.a_entry.grid(row=2, column=1)
        tk.Label(self.master, text="Edges (u, v, weight):").grid(row=3, column=0)
        self.edges_entry = tk.Entry(self.master)
        self.edges_entry.grid(row=3, column=1)
        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate_min_weights)
        self.calculate_button.grid(row=4, columnspan=2)
        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=5, columnspan=2)
    def calculate_min_weights(self):
        try:
            N = int(self.n_entry.get())
            M = int(self.m_entry.get())
            if N <= 0 or M <= 0:
                raise ValueError("Number of vertices (N) and edges (M) must be positive integers.")
            A = list(map(int, self.a_entry.get().split(',')))
            if len(A) != N:
                raise ValueError("The number of vertex weights must match the number of vertices (N).")
            edges_info = self.edges_entry.get().strip().split(';')
            edges = []
            for edge in edges_info:
                parts = edge.split(',')
                if len(parts) != 3:
                    raise ValueError(f"Edge must contain exactly three values: {edge}.")
                u, v, weight = map(int, parts)
                if u < 1 or u > N or v < 1 or v > N:
                    raise ValueError(f"Vertex indices must be between 1 and {N}.")
                if weight <= 0:  # Assuming weights must be positive
                    raise ValueError(f"Edge weight must be a positive integer: {weight}.")
                edges.append((u, v, weight))
            if len(edges) != M:
                raise ValueError("The number of edges provided does not match M.")
            graph = Graph(N, M, A)
            for edge in edges:
                graph.add_edge(edge[0], edge[1], edge[2])
            results = graph.dijkstra()
            self.display_results(results)
        except Exception as e:
            messagebox.showerror("Input Error", str(e))
    def display_results(self, results):
        self.result_label.config(text="Minimum Path Weights: " + ', '.join(map(str, results)))