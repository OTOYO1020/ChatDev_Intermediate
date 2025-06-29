'''
Main application file for the minimum median calculator.
'''
import tkinter as tk
from tkinter import messagebox
from median_calculator import find_minimum_median
class App:
    def __init__(self, master):
        self.master = master
        master.title("Minimum Median Calculator")
        self.label = tk.Label(master, text="Enter grid size (N) and K:")
        self.label.pack()
        self.size_entry = tk.Entry(master)
        self.size_entry.pack()
        self.k_entry = tk.Entry(master)
        self.k_entry.pack()
        self.grid_entry = tk.Text(master, height=10, width=30)
        self.grid_entry.pack()
        self.calculate_button = tk.Button(master, text="Calculate Minimum Median", command=self.calculate_median)
        self.calculate_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def calculate_median(self):
        try:
            n, k = map(int, self.size_entry.get().split())
            grid_input = self.grid_entry.get("1.0", tk.END).strip().splitlines()
            # Validate grid input
            if len(grid_input) != n:
                raise ValueError(f"Grid must have exactly {n} rows.")
            grid = []
            for line in grid_input:
                row = list(map(int, line.split()))
                if len(row) != n:
                    raise ValueError(f"Each row must have exactly {n} integers.")
                grid.append(row)
            # Validate that all entries are integers
            for row in grid:
                for value in row:
                    if not isinstance(value, int):
                        raise ValueError("All grid entries must be integers.")
            min_median = find_minimum_median(n, k, grid)
            self.result_label.config(text=f"Minimum Median: {min_median:.2f}")  # Display as float
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", str(e))
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()