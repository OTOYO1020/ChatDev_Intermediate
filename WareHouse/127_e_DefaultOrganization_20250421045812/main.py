'''
Main application file for calculating Manhattan distances.
'''
import tkinter as tk
from tkinter import messagebox
from combinatorics import Combinatorics
from distance_calculator import DistanceCalculator
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Manhattan Distance Calculator")
        tk.Label(self.root, text="Enter N (rows):").grid(row=0, column=0)
        self.n_entry = tk.Entry(self.root)
        self.n_entry.grid(row=0, column=1)
        tk.Label(self.root, text="Enter M (columns):").grid(row=1, column=0)
        self.m_entry = tk.Entry(self.root)
        self.m_entry.grid(row=1, column=1)
        tk.Label(self.root, text="Enter K (pieces):").grid(row=2, column=0)
        self.k_entry = tk.Entry(self.root)
        self.k_entry.grid(row=2, column=1)
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, columnspan=2)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=4, columnspan=2)
    def calculate(self):
        try:
            n = int(self.n_entry.get())
            m = int(self.m_entry.get())
            k = int(self.k_entry.get())
            if n <= 0 or m <= 0 or k <= 0:
                raise ValueError("N, M, and K must be positive integers.")
            distance_calculator = DistanceCalculator(n, m, k)
            result = distance_calculator.calculate_distance()
            self.result_label.config(text=f"Total Manhattan Distance: {result}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = MainApp()
    app.run()