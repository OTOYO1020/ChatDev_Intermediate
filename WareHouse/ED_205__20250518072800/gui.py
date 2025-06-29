'''
GUI module for the ball arrangement application using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from logic import countArrangements
class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ball Arrangement Calculator")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.window, text="Number of White Balls (N):").pack()
        self.n_entry = tk.Entry(self.window)
        self.n_entry.pack()
        tk.Label(self.window, text="Number of Black Balls (M):").pack()
        self.m_entry = tk.Entry(self.window)
        self.m_entry.pack()
        tk.Label(self.window, text="Maximum Difference (K):").pack()
        self.k_entry = tk.Entry(self.window)
        self.k_entry.pack()
        tk.Button(self.window, text="Calculate", command=self.calculate).pack()
    def calculate(self):
        try:
            N = int(self.n_entry.get())
            M = int(self.m_entry.get())
            K = int(self.k_entry.get())
            result = countArrangements(N, M, K)
            self.display_result(result)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers.")
    def display_result(self, result):
        messagebox.showinfo("Result", f"Valid arrangements: {result}")
    def run(self):
        self.window.mainloop()