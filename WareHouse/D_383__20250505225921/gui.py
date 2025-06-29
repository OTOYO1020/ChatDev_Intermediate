'''
Module for creating the GUI components and handling user interactions.
'''
import tkinter as tk
from tkinter import messagebox
from divisor_counter import count_numbers_with_nine_divisors
def create_gui(root):
    '''
    Create the GUI components for the application.
    '''
    def on_count_button_click():
        try:
            N = int(entry.get())
            if N < 1:
                messagebox.showerror("Input Error", "Please enter a positive integer greater than 0.")
                return
            result = count_numbers_with_nine_divisors(N)
            messagebox.showinfo("Result", f"Count of numbers with exactly 9 divisors: {result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer.")
    label = tk.Label(root, text="Enter an integer N:")
    label.pack(pady=10)
    entry = tk.Entry(root)
    entry.pack(pady=10)
    count_button = tk.Button(root, text="Count Divisors", command=on_count_button_click)
    count_button.pack(pady=10)