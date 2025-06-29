'''
Module defining the App class for the GUI of the happiness calculator application.
'''
import tkinter as tk
from tkinter import messagebox
from dish import Dish
from happiness_calculator import HappinessCalculator
class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Happiness Calculator")
        self.label_n = tk.Label(self.window, text="Number of Dishes:")
        self.label_n.pack()
        self.entry_n = tk.Entry(self.window)
        self.entry_n.pack()
        self.label_t = tk.Label(self.window, text="Total Time:")
        self.label_t.pack()
        self.entry_t = tk.Entry(self.window)
        self.entry_t.pack()
        self.dishes = []
        self.label_dishes = tk.Label(self.window, text="Enter dishes (time, deliciousness) separated by commas:")
        self.label_dishes.pack()
        self.entry_dishes = tk.Entry(self.window)
        self.entry_dishes.pack()
        self.submit_button = tk.Button(self.window, text="Calculate Happiness", command=self.submit)
        self.submit_button.pack()
    def submit(self):
        try:
            n = int(self.entry_n.get())
            total_time = int(self.entry_t.get())  # Changed to int
            # Input validation for N and T
            if n <= 0 or total_time <= 0:
                raise ValueError("N and T must be positive integers.")
            dishes_input = self.entry_dishes.get().split(',')
            if len(dishes_input) != n:
                raise ValueError("Number of dishes does not match the input provided.")
            self.dishes = []
            for dish_input in dishes_input:
                eating_time, deliciousness = map(int, dish_input.strip().split())  # Changed to int
                # Input validation for eating time and deliciousness
                if eating_time < 0 or deliciousness < 0:
                    raise ValueError("Eating time and deliciousness must be non-negative integers.")
                self.dishes.append(Dish(eating_time, deliciousness))
            calculator = HappinessCalculator()
            max_happiness = calculator.calculate_max_happiness(self.dishes, total_time)
            messagebox.showinfo("Result", f"Maximum Happiness: {max_happiness}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def run(self):
        self.window.mainloop()