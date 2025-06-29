'''
Main application file for calculating Manhattan distances in a grid.
'''
from tkinter import Tk, Label, Entry, Button, StringVar
from distance_calculator import DistanceCalculator
class MainApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Manhattan Distance Calculator")
        self.N_var = StringVar()
        self.M_var = StringVar()
        self.K_var = StringVar()
        self.result_var = StringVar()
        Label(self.root, text="Enter N (rows):").grid(row=0, column=0)
        Entry(self.root, textvariable=self.N_var).grid(row=0, column=1)
        Label(self.root, text="Enter M (columns):").grid(row=1, column=0)
        Entry(self.root, textvariable=self.M_var).grid(row=1, column=1)
        Label(self.root, text="Enter K (pieces):").grid(row=2, column=0)
        Entry(self.root, textvariable=self.K_var).grid(row=2, column=1)
        Button(self.root, text="Calculate", command=self.calculate_distances).grid(row=3, column=0, columnspan=2)
        Label(self.root, text="Result:").grid(row=4, column=0)
        Label(self.root, textvariable=self.result_var).grid(row=4, column=1)
        self.root.mainloop()
    def calculate_distances(self):
        try:
            N = int(self.N_var.get())
            M = int(self.M_var.get())
            K = int(self.K_var.get())
            if N <= 0 or M <= 0 or K < 0:
                raise ValueError("N and M must be positive integers, and K must be non-negative.")
            calculator = DistanceCalculator(N, M, K)
            result = calculator.calculate_distance_cost()
            self.display_result(result)
        except ValueError as e:
            self.result_var.set(f"Error: {e}")
    def display_result(self, result):
        self.result_var.set(result)
if __name__ == "__main__":
    MainApp()