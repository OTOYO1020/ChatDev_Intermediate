'''
App class to create the GUI for the application.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
from painter import Painter
class App:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Graph Painter")
        self.label_n = tk.Label(self.master, text="Number of vertices (N):")
        self.label_n.pack()
        self.entry_n = tk.Entry(self.master)
        self.entry_n.pack()
        self.label_m = tk.Label(self.master, text="Number of edges (M):")
        self.label_m.pack()
        self.entry_m = tk.Entry(self.master)
        self.entry_m.pack()
        self.label_edges = tk.Label(self.master, text="Edges (format: u v):")
        self.label_edges.pack()
        self.entry_edges = tk.Entry(self.master)
        self.entry_edges.pack()
        self.label_k = tk.Label(self.master, text="Number of conditions (K):")
        self.label_k.pack()
        self.entry_k = tk.Entry(self.master)
        self.entry_k.pack()
        self.label_p = tk.Label(self.master, text="Vertices (p):")
        self.label_p.pack()
        self.entry_p = tk.Entry(self.master)
        self.entry_p.pack()
        self.label_d = tk.Label(self.master, text="Distances (d):")
        self.label_d.pack()
        self.entry_d = tk.Entry(self.master)
        self.entry_d.pack()
        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit)
        self.submit_button.pack()
    def run(self):
        self.master.mainloop()
    def submit(self):
        try:
            N = int(self.entry_n.get())
            M = int(self.entry_m.get())
            edges_input = self.entry_edges.get().strip()
            edges = []
            # Validate and parse edges
            if edges_input:
                for edge in edges_input.split(','):
                    try:
                        u, v = map(int, edge.split())
                        if u < 0 or u >= N or v < 0 or v >= N:
                            raise ValueError(f"Edge vertices must be in the range [0, {N-1}]")
                        edges.append((u, v))
                    except ValueError:
                        raise ValueError(f"Invalid edge format: {edge}. Expected format: 'u v'")
            K = int(self.entry_k.get())
            p = list(map(int, self.entry_p.get().split(',')))
            d = list(map(int, self.entry_d.get().split(',')))
            graph = Graph(N)
            for u, v in edges:
                graph.add_edge(u, v)
            painter = Painter(graph, K, p, d)
            possible, colors = painter.can_paint()
            if possible:
                messagebox.showinfo("Result", f"Painting is possible! Colors: {colors}")
            else:
                messagebox.showerror("Result", "Painting is not possible.")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")