'''
Module to define the GUI for the graph coloring application.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
class GraphApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Graph Coloring Application")
        self.graph = None
        self.label_vertices = tk.Label(self.window, text="Number of vertices:")
        self.label_vertices.pack()
        self.entry_vertices = tk.Entry(self.window)
        self.entry_vertices.pack()
        self.label_edges = tk.Label(self.window, text="Enter edges (u v w):")
        self.label_edges.pack()
        self.text_edges = tk.Text(self.window, height=10, width=30)
        self.text_edges.pack()
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_graph)
        self.submit_button.pack()
    def submit_graph(self):
        try:
            vertices = int(self.entry_vertices.get())
            if vertices < 1:
                raise ValueError("The number of vertices must be at least 1.")
            edges_input = self.text_edges.get("1.0", tk.END).strip().splitlines()
            self.graph = Graph(vertices)
            for edge in edges_input:
                u, v, w = map(int, edge.split())
                if u < 0 or u >= vertices or v < 0 or v >= vertices:
                    raise ValueError(f"Invalid edge ({u}, {v}). Vertices must be in the range 0 to {vertices-1}.")
                self.graph.add_edge(u, v, w)
            self.graph.color_graph()
            self.display_colors()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def display_colors(self):
        color_output = "\n".join(str(color) for color in self.graph.colors)
        messagebox.showinfo("Vertex Colors", color_output)
    def run(self):
        self.window.mainloop()