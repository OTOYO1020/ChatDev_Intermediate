'''
App class to create the GUI for the grid navigation application.
'''
import tkinter as tk
from tkinter import messagebox
from grid import Grid
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Grid Navigation")
        self.label = tk.Label(master, text="Enter grid dimensions (H W):")
        self.label.pack()
        self.dim_entry = tk.Entry(master)
        self.dim_entry.pack()
        self.grid_text = tk.Text(master, height=10, width=30)
        self.grid_text.pack()
        self.run_button = tk.Button(master, text="Run", command=self.run_algorithm)
        self.run_button.pack()
    def run_algorithm(self):
        dimensions = self.dim_entry.get().split()
        height, width = int(dimensions[0]), int(dimensions[1])
        grid_lines = self.grid_text.get("1.0", tk.END).splitlines()
        # Check if the number of lines matches the specified height
        if len(grid_lines) != height:
            messagebox.showerror("Input Error", f"Please enter exactly {height} lines for the grid.")
            return
        # Ensure each line has the correct width
        for line in grid_lines:
            if len(line) != width:
                messagebox.showerror("Input Error", f"Each line must have exactly {width} characters.")
                return
        grid_data = [list(line) for line in grid_lines]
        grid = Grid(height, width, grid_data)
        moves = grid.bfs()
        if moves != -1:
            messagebox.showinfo("Result", f"Minimum moves: {moves}")
        else:
            messagebox.showinfo("Result", "Goal is unreachable.")