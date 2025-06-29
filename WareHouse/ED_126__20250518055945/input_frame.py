'''
Input frame for user to enter the number of cards, conditions, and their values.
'''
import tkinter as tk
from tkinter import messagebox
from typing import List, Tuple
class InputFrame(tk.Frame):
    def __init__(self, master, calculate_callback):
        super().__init__(master)
        self.calculate_callback = calculate_callback
        self.label_n = tk.Label(self, text="Number of Cards (N):")
        self.label_n.grid(row=0, column=0)
        self.entry_n = tk.Entry(self)
        self.entry_n.grid(row=0, column=1)
        self.label_m = tk.Label(self, text="Number of Conditions (M):")
        self.label_m.grid(row=1, column=0)
        self.entry_m = tk.Entry(self)
        self.entry_m.grid(row=1, column=1)
        self.label_conditions = tk.Label(self, text="Conditions (X Y Z):")
        self.label_conditions.grid(row=2, column=0)
        self.entry_conditions = tk.Entry(self)
        self.entry_conditions.grid(row=2, column=1)
        self.button_calculate = tk.Button(self, text="Calculate", command=self.calculate)
        self.button_calculate.grid(row=3, columnspan=2)
    def calculate(self):
        N, M, conditions = self.get_input()
        if N is not None and M is not None and conditions is not None:
            self.calculate_callback(N, M, conditions)
    def get_input(self) -> Tuple[int, int, List[Tuple[int, int, int]]]:
        try:
            N = int(self.entry_n.get())
            M = int(self.entry_m.get())
            conditions_input = self.entry_conditions.get().strip()
            conditions = []
            if conditions_input:
                conditions = [tuple(map(int, cond.split())) for cond in conditions_input.split(',')]
            return N, M, conditions
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for N and M, and conditions in the correct format.")
            return None, None, None