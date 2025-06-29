'''
GUI implementation for the application using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from number_utils import find_kth_321_like_number
def create_gui():
    """
    Sets up the GUI components and layout.
    """
    def on_find():
        try:
            K = int(entry.get())
            result = find_kth_321_like_number(K)
            messagebox.showinfo("Result", f"The {K}-th smallest 321-like Number is: {result}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    # Create the main window
    root = tk.Tk()
    root.title("321-like Number Finder")
    # Create and place the input label and entry
    label = tk.Label(root, text="Enter K:")
    label.pack(pady=10)
    entry = tk.Entry(root)
    entry.pack(pady=10)
    # Create and place the find button
    find_button = tk.Button(root, text="Find K-th 321-like Number", command=on_find)
    find_button.pack(pady=20)
    # Start the GUI event loop
    root.mainloop()