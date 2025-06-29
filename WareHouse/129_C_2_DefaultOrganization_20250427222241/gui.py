'''
GUI for the stair climbing application.
'''
import tkinter as tk
from tkinter import messagebox
from climb_stairs import countWaysToClimb
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Stair Climbing Ways Calculator")
        self.label_n = tk.Label(master, text="Enter number of steps (N):")
        self.label_n.pack()
        self.entry_n = tk.Entry(master)
        self.entry_n.pack()
        self.label_m = tk.Label(master, text="Enter number of broken steps (M):")
        self.label_m.pack()
        self.entry_m = tk.Entry(master)
        self.entry_m.pack()
        self.label_broken = tk.Label(master, text="Enter broken steps (comma-separated):")
        self.label_broken.pack()
        self.entry_broken = tk.Entry(master)
        self.entry_broken.pack()
        self.calculate_button = tk.Button(master, text="Calculate Ways", command=self.calculate_ways)
        self.calculate_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def calculate_ways(self):
        try:
            N = int(self.entry_n.get())
            M = int(self.entry_m.get())
            if N < 0 or M < 0:
                raise ValueError("N and M must be non-negative integers.")
            broken_steps_input = self.entry_broken.get().strip()
            if broken_steps_input:
                broken_steps = list(map(int, broken_steps_input.split(',')))
            else:
                broken_steps = []
            if len(broken_steps) != M:
                raise ValueError("Number of broken steps does not match M.")
            if any(step < 0 or step > N for step in broken_steps):
                raise ValueError("Broken steps must be in the range from 0 to N.")
            result = countWaysToClimb(N, M, broken_steps)
            self.result_label.config(text=f"Ways to climb: {result}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Unexpected Error", "An unexpected error occurred: " + str(e))