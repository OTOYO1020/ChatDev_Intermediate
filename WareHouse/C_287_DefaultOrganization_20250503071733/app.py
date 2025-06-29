'''
Application class to create the GUI for the path graph checker.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Path Graph Checker")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Enter number of vertices (N):").pack()
        self.vertices_entry = tk.Entry(self.root)
        self.vertices_entry.pack()
        tk.Label(self.root, text="Enter number of edges (M):").pack()
        self.edges_entry = tk.Entry(self.root)
        self.edges_entry.pack()
        tk.Label(self.root, text="Enter edges (u,v) separated by commas (e.g., 1,2,2,3):").pack()
        self.edges_input = tk.Entry(self.root)
        self.edges_input.pack()
        self.check_button = tk.Button(self.root, text="Check Graph", command=self.check_graph)
        self.check_button.pack()
    def check_graph(self):
        try:
            N = int(self.vertices_entry.get())
            M = int(self.edges_entry.get())
            # Input validation for N and M
            if N < 1:
                raise ValueError("Number of vertices (N) must be at least 1.")
            if M < 0:
                raise ValueError("Number of edges (M) cannot be negative.")
            edges_input = self.edges_input.get().strip()
            if not edges_input:
                raise ValueError("Edges input cannot be empty.")
            edges = []
            seen_edges = set()  # To track edges and prevent duplicates
            edge_pairs = edges_input.split(',')
            if len(edge_pairs) % 2 != 0:
                raise ValueError("Edges input must contain an even number of integers.")
            for i in range(0, len(edge_pairs), 2):
                try:
                    u = int(edge_pairs[i].strip())
                    v = int(edge_pairs[i + 1].strip())
                    if (u, v) in seen_edges or (v, u) in seen_edges:  # Check for duplicates
                        raise ValueError(f"Duplicate edge found: {u} - {v}.")
                    edges.append((u, v))
                    seen_edges.add((u, v))
                except ValueError:
                    raise ValueError(f"Invalid edge format: {edge_pairs[i].strip()} or {edge_pairs[i + 1].strip()}. Please use the format 'u,v'.")
            # Validate the number of edges matches M
            if len(edges) != M:
                raise ValueError("Number of edges does not match M.")
            # Validate vertices in edges
            for u, v in edges:
                if u < 1 or u > N or v < 1 or v > N:
                    raise ValueError(f"Vertices {u} and {v} must be between 1 and {N}.")
            graph = Graph(N)
            for u, v in edges:
                graph.add_edge(u, v)
            result = "YES" if graph.is_path_graph() else "NO"
            self.display_result(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def display_result(self, result):
        messagebox.showinfo("Result", result)
    def run(self):
        self.root.mainloop()