'''
App class to create the GUI for the BFS shortest path application.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("BFS Shortest Path Finder")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.master, text="Number of Vertices (N):").grid(row=0, column=0)
        self.n_entry = tk.Entry(self.master)
        self.n_entry.grid(row=0, column=1)
        tk.Label(self.master, text="Number of Edges (M):").grid(row=1, column=0)
        self.m_entry = tk.Entry(self.master)
        self.m_entry.grid(row=1, column=1)
        tk.Label(self.master, text="Edges (u v):").grid(row=2, column=0)
        self.edges_entry = tk.Entry(self.master)
        self.edges_entry.grid(row=2, column=1)
        tk.Label(self.master, text="Starting Vertex (S):").grid(row=3, column=0)
        self.s_entry = tk.Entry(self.master)
        self.s_entry.grid(row=3, column=1)
        tk.Label(self.master, text="Target Vertex (T):").grid(row=4, column=0)
        self.t_entry = tk.Entry(self.master)
        self.t_entry.grid(row=4, column=1)
        self.run_button = tk.Button(self.master, text="Run BFS", command=self.run_bfs)
        self.run_button.grid(row=5, columnspan=2)
    def run_bfs(self):
        try:
            N = int(self.n_entry.get())
            M = int(self.m_entry.get())
            edges = self.edges_entry.get().strip().split()
            S = int(self.s_entry.get())
            T = int(self.t_entry.get())
            graph = Graph(N)
            for i in range(0, len(edges), 2):
                u = int(edges[i])
                v = int(edges[i + 1])
                graph.add_edge(u, v)
            result = graph.bfs(S, T)
            messagebox.showinfo("Result", f"Shortest Path Length: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))