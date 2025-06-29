'''
GUI class to handle user interface for the increment counters application.
'''
import tkinter as tk
from tkinter import messagebox
from tree import Tree
from typing import List, Tuple
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Increment Counters Application")
        self.tree = None
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Number of Vertices (N):").grid(row=0, column=0)
        self.n_entry = tk.Entry(self.root)
        self.n_entry.grid(row=0, column=1)
        tk.Label(self.root, text="Edges (u,v):").grid(row=1, column=0)
        self.edges_entry = tk.Entry(self.root)
        self.edges_entry.grid(row=1, column=1)
        tk.Label(self.root, text="Number of Operations (Q):").grid(row=2, column=0)
        self.q_entry = tk.Entry(self.root)
        self.q_entry.grid(row=2, column=1)
        tk.Label(self.root, text="Operations (p,x):").grid(row=3, column=0)
        self.operations_entry = tk.Entry(self.root)
        self.operations_entry.grid(row=3, column=1)
        self.submit_button = tk.Button(self.root, text="Submit", command=self.process_input)
        self.submit_button.grid(row=4, columnspan=2)
        self.output_label = tk.Label(self.root, text="")
        self.output_label.grid(row=5, columnspan=2)
    def process_input(self):
        try:
            N = int(self.n_entry.get())
            edges_input = self.edges_entry.get().strip().split(';')
            edges = [tuple(map(int, edge.split(','))) for edge in edges_input]
            Q = int(self.q_entry.get())
            operations_input = self.operations_entry.get().strip().split(';')
            operations = [tuple(map(int, op.split(','))) for op in operations_input]
            self.tree = Tree(N, edges)
            for node, increment in operations:
                self.tree.increment_counters(node, increment)
            self.tree.apply_lazy()  # Apply lazy propagation
            final_counters = self.tree.get_final_counters()
            self.display_output(final_counters)
        except Exception as e:
            messagebox.showerror("Input Error", str(e))
    def display_output(self, final_counters: List[int]):
        self.output_label.config(text=f"Final Counters: {final_counters}")
    def run(self):
        self.root.mainloop()