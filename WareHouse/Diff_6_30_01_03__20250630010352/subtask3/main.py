'''
Main application file for the smallest integer finder.
'''
import tkinter as tk
from tkinter import messagebox
from utils import find_smallest_x
class App:
    def __init__(self, master):
        self.master = master
        master.title("Smallest Integer Finder")
        self.label = tk.Label(master, text="Enter an integer N:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.find_button = tk.Button(master, text="Find Smallest X", command=self.handle_find)
        self.find_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def handle_find(self):
        try:
            n = int(self.entry.get())
            result = find_smallest_x(n)
            self.result_label.config(text=f"The smallest integer X is: {result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer.")
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()