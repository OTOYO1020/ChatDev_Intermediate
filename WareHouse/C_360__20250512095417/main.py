'''
Main application file for the box rearrangement dashboard.
'''
import tkinter as tk
from tkinter import messagebox
from box_manager import BoxManager
from input_validation import InputValidation
class MainApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Box Rearrangement Dashboard")
        tk.Label(self.window, text="Number of Boxes (N):").grid(row=0, column=0)
        self.n_entry = tk.Entry(self.window)
        self.n_entry.grid(row=0, column=1)
        tk.Label(self.window, text="Box Numbers (A):").grid(row=1, column=0)
        self.a_entry = tk.Entry(self.window)
        self.a_entry.grid(row=1, column=1)
        tk.Label(self.window, text="Weights (W):").grid(row=2, column=0)
        self.w_entry = tk.Entry(self.window)
        self.w_entry.grid(row=2, column=1)
        self.calculate_button = tk.Button(self.window, text="Calculate Min Cost", command=self.calculate_min_cost)
        self.calculate_button.grid(row=3, columnspan=2)
        self.result_label = tk.Label(self.window, text="")
        self.result_label.grid(row=4, columnspan=2)
        self.window.mainloop()
    def calculate_min_cost(self):
        try:
            N = int(self.n_entry.get())
            A = list(map(int, self.a_entry.get().split(',')))
            W = list(map(int, self.w_entry.get().split(',')))
            validator = InputValidation()
            if not validator.validate_inputs(N, A, W):
                raise ValueError("Invalid inputs. Please check your data.")
            box_manager = BoxManager(N, A, W)
            min_cost = box_manager.min_cost_to_rearrange_boxes()
            self.result_label.config(text=f"Minimum Cost: {min_cost}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
if __name__ == "__main__":
    MainApp()