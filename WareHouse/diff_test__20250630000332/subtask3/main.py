'''
Main application file for the integer finder GUI.
'''
import tkinter as tk
from tkinter import messagebox
from integer_finder import find_smallest_integer
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Smallest Integer Finder")
        self.label = tk.Label(root, text="Enter an integer N (0 <= N <= 10^18):")
        self.label.pack(pady=10)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)
        self.button = tk.Button(root, text="Find Smallest Integer", command=self.find_integer)
        self.button.pack(pady=10)
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
    def find_integer(self):
        try:
            N = int(self.entry.get())
            result = find_smallest_integer(N)
            self.result_label.config(text=f"Smallest Integer X: {result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()