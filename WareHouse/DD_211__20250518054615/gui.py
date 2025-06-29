'''
GUI class to handle user interface and interactions.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Path Counting Application")
        self.graph = None
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.window, text="Number of Cities (N):").grid(row=0, column=0)
        self.n_entry = tk.Entry(self.window)
        self.n_entry.grid(row=0, column=1)
        tk.Label(self.window, text="Number of Roads (M):").grid(row=1, column=0)
        self.m_entry = tk.Entry(self.window)
        self.m_entry.grid(row=1, column=1)
        tk.Label(self.window, text="Roads (u v; u v; ...):").grid(row=2, column=0)
        self.roads_entry = tk.Entry(self.window)
        self.roads_entry.grid(row=2, column=1)
        self.submit_button = tk.Button(self.window, text="Count Paths", command=self.count_paths)
        self.submit_button.grid(row=3, columnspan=2)
    def count_paths(self):
        try:
            n = int(self.n_entry.get())
            m = int(self.m_entry.get())
            if n <= 0 or m < 0:
                raise ValueError("Number of cities must be positive and number of roads cannot be negative.")
            # Handle the case where there are no roads
            if m == 0:
                self.graph = Graph(n)
                result = self.graph.count_paths(1, n)
                self.display_output(result)
                return
            roads_input = self.roads_entry.get().strip().split(';')
            self.graph = Graph(n)
            for road in roads_input:
                road = road.strip()  # Trim spaces
                if road:  # Ensure the road is not empty
                    parts = road.split()
                    if len(parts) != 2:
                        raise ValueError(f"Invalid road format: {road}. Each road must be in the format 'u v'.")
                    try:
                        u, v = map(int, parts)
                    except ValueError:
                        raise ValueError(f"Invalid road values: {road}. Both u and v must be integers.")
                    if u < 1 or u > n or v < 1 or v > n:
                        raise ValueError(f"Roads must connect cities between 1 and {n}. Invalid road: {road}")
                    self.graph.add_road(u, v)
            result = self.graph.count_paths(1, n)
            self.display_output(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def display_output(self, result):
        messagebox.showinfo("Result", f"Number of distinct shortest paths: {result}")
    def run(self):
        self.window.mainloop()