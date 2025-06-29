'''
GUI components for the grid reachability application.
'''
import tkinter as tk
from tkinter import messagebox
from grid import Grid
class MainApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Grid Reachability")
        self.create_widgets()
    def create_widgets(self):
        self.size_label = tk.Label(self.window, text="Grid Size (N):")
        self.size_label.pack()
        self.size_entry = tk.Entry(self.window)
        self.size_entry.pack()
        self.distance_label = tk.Label(self.window, text="Distance Squared (M):")
        self.distance_label.pack()
        self.distance_entry = tk.Entry(self.window)
        self.distance_entry.pack()
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.pack()
        self.result_frame = tk.Frame(self.window)
        self.result_frame.pack()
    def calculate(self):
        try:
            size = int(self.size_entry.get())
            distance_squared = int(self.distance_entry.get())
            grid = Grid(size, distance_squared)
            self.display_results(grid)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for size and distance.")
    def display_results(self, grid):
        reachable = grid.get_reachable()
        min_operations = grid.get_min_operations()
        # Clear previous results
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        tk.Label(self.result_frame, text="Reachable Grid:").pack()
        for row in reachable:  # No need to skip the first row for 0-based indexing
            tk.Label(self.result_frame, text=row).pack()  # No need to skip the first column for 0-based indexing
        tk.Label(self.result_frame, text="Minimum Operations:").pack()
        for row in min_operations:  # No need to skip the first row for 0-based indexing
            tk.Label(self.result_frame, text=row).pack()  # No need to skip the first column for 0-based indexing
    def run(self):
        self.window.mainloop()