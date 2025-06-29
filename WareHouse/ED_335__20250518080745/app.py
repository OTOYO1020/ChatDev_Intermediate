'''
Application class to create the GUI for user interaction.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Max Score Path Finder")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.window, text="Number of Vertices (N):").grid(row=0, column=0)
        self.n_entry = tk.Entry(self.window)
        self.n_entry.grid(row=0, column=1)
        tk.Label(self.window, text="Number of Edges (M):").grid(row=1, column=0)
        self.m_entry = tk.Entry(self.window)
        self.m_entry.grid(row=1, column=1)
        tk.Label(self.window, text="Edges (U, V):").grid(row=2, column=0)
        self.edges_entry = tk.Entry(self.window)
        self.edges_entry.grid(row=2, column=1)
        tk.Label(self.window, text="Values (A):").grid(row=3, column=0)
        self.values_entry = tk.Entry(self.window)
        self.values_entry.grid(row=3, column=1)
        self.calculate_button = tk.Button(self.window, text="Calculate Max Score", command=self.calculate_score)
        self.calculate_button.grid(row=4, columnspan=2)
    def run(self):
        self.window.mainloop()
    def calculate_score(self):
        try:
            n = int(self.n_entry.get())
            m = int(self.m_entry.get())
            edges = [tuple(map(int, edge.split(','))) for edge in self.edges_entry.get().split(';')]
            values = list(map(int, self.values_entry.get().split(',')))
            # Validate the number of edges
            if len(edges) != m:
                messagebox.showerror("Error", f"Expected {m} edges, but got {len(edges)}.")
                return
            # Validate vertices and edges
            if n < 1 or m < 0 or len(values) != n:
                messagebox.showerror("Error", "Invalid input for vertices or edges.")
                return
            # Validate edges to ensure they are within the range of vertices
            for u, v in edges:
                if u < 1 or u > n or v < 1 or v > n:
                    messagebox.showerror("Error", "Edge vertices must be between 1 and N.")
                    return
            graph = Graph(n, edges, values)
            max_score = graph.find_max_score_path()
            messagebox.showinfo("Result", f"Maximum Score: {max_score}")
        except Exception as e:
            messagebox.showerror("Error", str(e))