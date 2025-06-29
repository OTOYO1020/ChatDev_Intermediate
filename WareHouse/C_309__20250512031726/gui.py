'''
Contains the GUI-related functions and classes.
'''
from tkinter import Label, Entry, Button, StringVar, messagebox
from input_handler import InputHandler
from pills_calculator import PillsCalculator
from typing import List, Tuple
def parse_days_input(days_input: str) -> List[Tuple[int, int]]:
    days = []
    for day in days_input.strip().split(','):
        try:
            a, b = map(int, day.strip().split())
            if a < 1 or b < 1:  # Ensure a_i and b_i are positive integers
                raise ValueError(f"Both a_i and b_i must be positive integers for day: '{day}'.")
            days.append((a, b))
        except ValueError:
            raise ValueError(f"Invalid format for day: '{day}'. Please enter as 'a_i b_i' pairs separated by commas.")
    return days
def create_gui(root):
    Label(root, text="Number of Medicine Types (N):").grid(row=0, column=0)
    n_entry = Entry(root)
    n_entry.grid(row=0, column=1)
    Label(root, text="Threshold (K):").grid(row=1, column=0)
    k_entry = Entry(root)
    k_entry.grid(row=1, column=1)
    Label(root, text="Days (a_i, b_i) - comma separated:").grid(row=2, column=0)
    days_entry = Entry(root)
    days_entry.grid(row=2, column=1)
    result_var = StringVar()
    def calculate():
        try:
            n = int(n_entry.get())
            k = int(k_entry.get())
            days_input = days_entry.get().strip()
            if not days_input:
                messagebox.showerror("Input Error", "Days input cannot be empty.")
                return
            days = parse_days_input(days_input)
            input_handler = InputHandler(n, k, days)
            if not input_handler.validate_input():
                messagebox.showerror("Input Error", "Invalid input values.")
                return
            calculator = PillsCalculator(n, k, days)
            result = calculator.first_day_with_k_or_less_pills()
            result_var.set(f"First day with K or less pills: {result if result != -1 else 'No such day'}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))
    Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)
    Label(root, textvariable=result_var).grid(row=4, column=0, columnspan=2)