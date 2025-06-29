'''
Application class to create the GUI for the user interaction.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Minimum Subtree Finder")
        self.graph = Graph()
        tk.Label(master, text="Enter number of vertices (N):").pack()
        self.n_entry = tk.Entry(master)
        self.n_entry.pack()
        tk.Label(master, text="Enter number of required vertices (K):").pack()
        self.k_entry = tk.Entry(master)
        self.k_entry.pack()
        tk.Label(master, text="Enter edges (A B) separated by new lines:").pack()
        self.edges_text = tk.Text(master, height=10, width=30)
        self.edges_text.pack()
        tk.Label(master, text="Enter required vertices separated by space:").pack()
        self.required_text = tk.Entry(master)
        self.required_text.pack()
        self.run_button = tk.Button(master, text="Run DFS", command=self.run_dfs)
        self.run_button.pack()
    def run_dfs(self):
        try:
            edges = self.edges_text.get("1.0", tk.END).strip().splitlines()
            required_vertices = set(map(int, self.required_text.get().strip().split()))
            for edge in edges:
                a, b = map(int, edge.split())
                self.graph.add_edge(a, b)
            # Ensure that required_vertices is not empty before calling DFS
            if required_vertices:
                result, found_vertices = self.graph.dfs(next(iter(required_vertices)), -1, required_vertices)
                if not required_vertices.issubset(found_vertices):
                    messagebox.showinfo("Result", "Not all required vertices were found in the subtree.")
                else:
                    self.display_result(result)
            else:
                messagebox.showerror("Error", "No required vertices provided.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def display_result(self, result):
        messagebox.showinfo("Result", f"Minimum vertices needed: {result}")