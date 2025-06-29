'''
Contains the GUI class for the shortest distance calculator application.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph, ShortestDistanceCalculator
class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Shortest Distance Calculator")
        self.graph = None
        self.label = tk.Label(self.window, text="Enter number of vertices and edges:")
        self.label.pack()
        self.vertex_entry = tk.Entry(self.window)
        self.vertex_entry.pack()
        self.edge_entry = tk.Entry(self.window)
        self.edge_entry.pack()
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.pack()
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()
    def calculate(self):
        try:
            vertices = int(self.vertex_entry.get())
            edges_input = self.edge_entry.get().strip().split(',')
            self.graph = Graph(vertices)
            edges = []
            for edge in edges_input:
                u, v = map(int, edge.split())
                self.graph.add_edge(u, v)
                edges.append((u, v))  # Store the edges for calculation
            calculator = ShortestDistanceCalculator(self.graph, edges)  # Pass edges to the calculator
            results = calculator.calculate_shortest_distances()
            self.result_label.config(text=str(results))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for vertices and edges.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def run(self):
        self.window.mainloop()