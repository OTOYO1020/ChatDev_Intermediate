'''
Module to define the GUI application for Dijkstra's algorithm.
'''
from tkinter import Frame, Label, Entry, Button, Text, END
from graph import Graph
class App:
    def __init__(self, master):
        self.master = master
        master.title("Dijkstra's Algorithm GUI")
        self.label_n = Label(master, text="Number of vertices (N):")
        self.label_n.pack()
        self.entry_n = Entry(master)
        self.entry_n.pack()
        self.label_m = Label(master, text="Number of edges (M):")
        self.label_m.pack()
        self.entry_m = Entry(master)
        self.entry_m.pack()
        self.label_weights = Label(master, text="Enter vertex weights (space-separated):")
        self.label_weights.pack()
        self.entry_weights = Entry(master)
        self.entry_weights.pack()
        self.label_edges = Label(master, text="Enter edges (U, V, B) one per line:")
        self.label_edges.pack()
        self.text_edges = Text(master, height=10, width=50)
        self.text_edges.pack()
        self.calculate_button = Button(master, text="Calculate Minimum Path", command=self.calculate_min_path)
        self.calculate_button.pack()
        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack()
    def calculate_min_path(self):
        n = int(self.entry_n.get())
        m = int(self.entry_m.get())
        # Validate input for number of vertices and edges
        if n <= 0 or m < 0:
            self.result_text.insert(END, "Invalid input for number of vertices or edges.\n")
            return
        edges_input = self.text_edges.get("1.0", END).strip().splitlines()
        weights_input = list(map(int, self.entry_weights.get().split()))  # Read vertex weights from the entry
        # Validate vertex weights input
        if len(weights_input) != n:
            self.result_text.insert(END, "The number of vertex weights must match the number of vertices.\n")
            return
        graph = Graph(n, weights_input)  # Pass the vertex weights to the graph
        for edge in edges_input:
            u, v, b = map(int, edge.split())
            graph.add_edge(u, v, b)
        distances = graph.dijkstra(1)
        self.display_results(distances)
    def display_results(self, results):
        self.result_text.delete("1.0", END)
        for i in range(2, len(results) + 1):
            if results[i] == float('inf'):
                self.result_text.insert(END, f"No path from 1 to {i}\n")
            else:
                self.result_text.insert(END, f"Minimum path weight from 1 to {i}: {results[i]}\n")