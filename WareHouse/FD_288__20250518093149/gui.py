'''
Contains the GUI implementation for the application.
'''
import tkinter as tk
from tkinter import messagebox
from calculator import calculate_sum_of_products
class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sum of Products Calculator")
        # Input field for X
        self.label_x = tk.Label(self.window, text="Enter X (string of digits):")
        self.label_x.pack()
        self.entry_x = tk.Entry(self.window)
        self.entry_x.pack()
        # Input field for N
        self.label_n = tk.Label(self.window, text="Enter N (length of X):")
        self.label_n.pack()
        self.entry_n = tk.Entry(self.window)
        self.entry_n.pack()
        # Calculate button
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.pack()
        # Result label
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()
    def calculate(self):
        X = self.entry_x.get()
        try:
            N = int(self.entry_n.get())
            if len(X) != N or '0' in X:
                raise ValueError("Invalid input: X must be of length N and contain no '0' digits.")
            result = calculate_sum_of_products(X, N)
            self.display_result(result)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    def display_result(self, result):
        self.result_label.config(text=f"Result: {result}")
    def run(self):
        self.window.mainloop()