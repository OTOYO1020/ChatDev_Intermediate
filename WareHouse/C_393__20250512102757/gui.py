'''
Contains the GUI implementation for the Graph Edge Remover application.
'''
import tkinter as tk
from tkinter import messagebox
from edge_calculator import min_edges_to_remove
class GraphEdgeRemoverApp:
    '''
    Main GUI application for the Graph Edge Remover.
    '''
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Graph Edge Remover")
        self.label_n = tk.Label(self.window, text="Number of vertices (N):")
        self.label_n.pack()
        self.entry_n = tk.Entry(self.window)
        self.entry_n.pack()
        self.label_m = tk.Label(self.window, text="Number of edges (M):")
        self.label_m.pack()
        self.entry_m = tk.Entry(self.window)
        self.entry_m.pack()
        self.label_edges = tk.Label(self.window, text="Edges (format: u,v;u,v;...):")
        self.label_edges.pack()
        self.entry_edges = tk.Entry(self.window)
        self.entry_edges.pack()
        self.button_calculate = tk.Button(self.window, text="Calculate", command=self.calculate_edges)
        self.button_calculate.pack()
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()
    def calculate_edges(self):
        '''
        Retrieves input, calculates edges to remove, and displays the result.
        '''
        try:
            N = int(self.entry_n.get())
            M = int(self.entry_m.get())
            edges_input = self.entry_edges.get()
            # Handle the case when M is zero
            if M == 0:
                self.result_label.config(text="Edges to remove: 0")
                return
            # Validate and parse edges with consistent ordering
            try:
                edges = [tuple(map(int, edge.split(','))) for edge in edges_input.split(';')]
                # Remove duplicates by converting to a set
                edges = list(set(edges))
            except ValueError:
                raise ValueError("Invalid edge format. Please use the format u,v;u,v;... where u and v are integers.")
            if len(edges) > M:
                messagebox.showwarning("Warning", f"Found {len(edges)} unique edges, which is more than the specified M={M}. Duplicates were removed.")
            # Validate edges
            for u, v in edges:
                if not (0 <= u < N and 0 <= v < N):
                    raise ValueError(f"Edge ({u}, {v}) is out of bounds for the number of vertices N={N}.")
            result = min_edges_to_remove(N, M, edges)
            self.result_label.config(text=f"Edges to remove: {result}")
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Input Error", "An unexpected error occurred. Please check your input.")
    def run(self):
        '''
        Starts the GUI event loop.
        '''
        self.window.mainloop()