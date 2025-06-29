'''
Application class to manage the GUI for the graph query application.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Graph Query Application")
        self.graph = None
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.window, text="Number of Vertices:").grid(row=0, column=0)
        self.vertices_entry = tk.Entry(self.window)
        self.vertices_entry.grid(row=0, column=1)
        tk.Label(self.window, text="Edges (format: a b; separate multiple edges with commas):").grid(row=1, column=0)
        self.edges_entry = tk.Entry(self.window)
        self.edges_entry.grid(row=1, column=1)
        tk.Button(self.window, text="Submit Graph", command=self.submit_graph).grid(row=2, columnspan=2)
        tk.Label(self.window, text="Vertex for Query:").grid(row=3, column=0)
        self.query_vertex_entry = tk.Entry(self.window)
        self.query_vertex_entry.grid(row=3, column=1)
        tk.Label(self.window, text="Distance:").grid(row=4, column=0)
        self.query_distance_entry = tk.Entry(self.window)
        self.query_distance_entry.grid(row=4, column=1)
        tk.Button(self.window, text="Submit Query", command=self.submit_query).grid(row=5, columnspan=2)
    def submit_graph(self):
        try:
            vertices = int(self.vertices_entry.get())
            if vertices < 1:
                raise ValueError("Number of vertices must be a positive integer.")
            edges_input = self.edges_entry.get().strip()
            self.graph = Graph(vertices)
            if edges_input == "":
                messagebox.showinfo("Success", "Graph created successfully with no edges!")
                return
            edges = edges_input.replace(',', ' ').split()  # Replace commas with spaces and split
            for i in range(0, len(edges), 2):  # Process pairs of edges
                try:
                    a = int(edges[i])
                    b = int(edges[i + 1])
                    if a < 1 or a > vertices or b < 1 or b > vertices:
                        raise ValueError("Vertex indices must be within the range of the number of vertices.")
                    self.graph.add_edge(a, b)  # Use original 1-based indices for adding edges
                except (ValueError, IndexError) as e:
                    messagebox.showerror("Error", f"Invalid edge input '{edges_input}': {str(e)}")  # Show error for invalid edge
                    return  # Stop processing further edges if one is invalid
            messagebox.showinfo("Success", "Graph created successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def submit_query(self):
        try:
            x = int(self.query_vertex_entry.get())
            k = int(self.query_distance_entry.get())
            result = self.graph.sum_of_indices_within_distance(x, k)
            messagebox.showinfo("Query Result", f"Sum of indices within distance {k} from {x}: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def run(self):
        self.window.mainloop()