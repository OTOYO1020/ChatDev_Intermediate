'''
Module to create the input frame for user input.
'''
import tkinter as tk
from tkinter import messagebox
class InputFrame(tk.Frame):
    def __init__(self, master, calculate_callback):
        super().__init__(master)
        self.calculate_callback = calculate_callback
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self, text="Number of Cities (N):").grid(row=0, column=0)
        self.n_entry = tk.Entry(self)
        self.n_entry.grid(row=0, column=1)
        tk.Label(self, text="Number of Railroads (M):").grid(row=1, column=0)
        self.m_entry = tk.Entry(self)
        self.m_entry.grid(row=1, column=1)
        tk.Label(self, text="Starting City (X):").grid(row=2, column=0)
        self.x_entry = tk.Entry(self)
        self.x_entry.grid(row=2, column=1)
        tk.Label(self, text="Destination City (Y):").grid(row=3, column=0)
        self.y_entry = tk.Entry(self)
        self.y_entry.grid(row=3, column=1)
        tk.Label(self, text="Railroads (A, B, K, T):").grid(row=4, column=0)
        self.railroads_entry = tk.Entry(self)
        self.railroads_entry.grid(row=4, column=1)
        self.calculate_button = tk.Button(self, text="Calculate", command=self.on_calculate)
        self.calculate_button.grid(row=5, columnspan=2)
    def on_calculate(self):
        try:
            N = int(self.n_entry.get())
            M = int(self.m_entry.get())
            X = int(self.x_entry.get())
            Y = int(self.y_entry.get())
            # Validate input values
            if N <= 0 or M < 0 or X <= 0 or Y <= 0:
                raise ValueError("Cities and railroads must be positive integers.")
            # Validate and parse railroads input
            railroads_input = self.railroads_entry.get()
            railroads = []
            for r in railroads_input.split(';'):
                parts = r.split(',')
                if len(parts) != 4:
                    raise ValueError("Each railroad entry must have exactly four values: A, B, K, T.")
                railroads.append(tuple(map(int, parts)))
            result = self.calculate_callback(N, M, X, Y, railroads)
            messagebox.showinfo("Result", f"Earliest Arrival Time: {result}")
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", str(e))