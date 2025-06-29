'''
Main application file for the gold profit calculator.
'''
import tkinter as tk
from tkinter import messagebox
from graph import Graph
from profit_calculator import max_profit
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gold Profit Calculator")
        # Input fields
        tk.Label(root, text="Number of Towns (N):").grid(row=0, column=0)
        self.n_entry = tk.Entry(root)
        self.n_entry.grid(row=0, column=1)
        tk.Label(root, text="Number of Roads (M):").grid(row=1, column=0)
        self.m_entry = tk.Entry(root)
        self.m_entry.grid(row=1, column=1)
        tk.Label(root, text="Gold Prices (comma-separated):").grid(row=2, column=0)
        self.prices_entry = tk.Entry(root)
        self.prices_entry.grid(row=2, column=1)
        tk.Label(root, text="Roads (format: town1,town2;...):").grid(row=3, column=0)
        self.roads_entry = tk.Entry(root)
        self.roads_entry.grid(row=3, column=1)
        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate Profit", command=self.calculate_profit)
        self.calculate_button.grid(row=4, columnspan=2)
    def calculate_profit(self):
        try:
            N = int(self.n_entry.get())
            M = int(self.m_entry.get())
            A = list(map(int, self.prices_entry.get().split(',')))
            if len(A) != N:
                raise ValueError(f"The number of gold prices must be equal to the number of towns (N={N}).")
            roads_input = self.roads_entry.get().split(';')
            # Validate roads input
            roads = []
            for road in roads_input:
                try:
                    u, v = map(int, road.split(','))
                    roads.append((u, v))
                except ValueError:
                    raise ValueError(f"Invalid road format: {road}. Please use the format 'town1,town2'. Towns are 1-indexed.")
            max_profit_value = max_profit(N, M, A, roads)
            messagebox.showinfo("Result", f"Maximum Profit: {max_profit_value}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()