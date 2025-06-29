'''
GUI components for the Climbing Steps application.
'''
import tkinter as tk
from tkinter import messagebox
from climbing_logic import countWaysToClimb
class ClimbingGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Climbing Steps Calculator")
        self.label_n = tk.Label(self.window, text="Enter N (total steps):")
        self.label_n.pack()
        self.entry_n = tk.Entry(self.window)
        self.entry_n.pack()
        self.label_m = tk.Label(self.window, text="Enter M (number of broken steps):")
        self.label_m.pack()
        self.entry_m = tk.Entry(self.window)
        self.entry_m.pack()
        self.label_broken = tk.Label(self.window, text="Enter broken steps (comma-separated integers):")
        self.label_broken.pack()
        self.entry_broken = tk.Entry(self.window)
        self.entry_broken.pack()
        self.button_calculate = tk.Button(self.window, text="Calculate Ways", command=self.calculate_ways)
        self.button_calculate.pack()
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()
    def calculate_ways(self):
        try:
            N = int(self.entry_n.get())
            M = int(self.entry_m.get())  # Validate M input
            broken_steps = list(map(int, self.entry_broken.get().split(',')))
            # Ensure unique broken steps
            unique_broken_steps = list(set(broken_steps))
            # Validate that all broken steps are integers and within range
            if any(not isinstance(step, int) or step < 0 or step > N for step in unique_broken_steps):
                raise ValueError("All broken steps must be integers between 0 and N.")
            # Check that the number of unique broken steps does not exceed M
            if len(unique_broken_steps) > M:
                raise ValueError(f"Number of unique broken steps ({len(unique_broken_steps)}) cannot exceed M ({M}).")
            result = countWaysToClimb(N, len(unique_broken_steps), unique_broken_steps)
            self.result_label.config(text=f"Ways to climb: {result}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    def run(self):
        self.window.mainloop()