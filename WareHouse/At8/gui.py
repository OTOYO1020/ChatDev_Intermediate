'''
This file contains the GUI code.
'''
import tkinter as tk
from utils import find_matching_indices
class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self, text="Hello World")
        self.label.pack()
        self.button = tk.Button(self, text="Click Me", command=self.button_click)
        self.button.pack()
    def button_click(self):
        # Handle button click event here
        A = [1, 2, 3, 4, 5]
        B = [0, 2, 0, 4, 0]
        M = 3
        count = find_matching_indices(A, B, M)
        print(f"Number of matching indices: {count}")