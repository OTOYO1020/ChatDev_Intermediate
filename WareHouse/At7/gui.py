'''
This module contains the GUI class.
It creates a graphical user interface for the program.
'''
import tkinter as tk
from tkinter import messagebox
from utils import find_subsequences
class GUI:
    def __init__(self, root):
        self.root = root
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter two sequences:")
        self.label.pack()
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()
        self.button = tk.Button(self.root, text="Check", command=self.check_sequences)
        self.button.pack()
    def check_sequences(self):
        sequence1 = self.entry1.get()
        sequence2 = self.entry2.get()
        # Convert the input sequences to lists of integers
        sequence1 = [int(num) for num in sequence1.split()]
        sequence2 = [int(num) for num in sequence2.split()]
        result = find_subsequences(sequence1, sequence2)
        messagebox.showinfo("Result", f"The number of subsequences is {result}")
    def run(self):
        self.root.mainloop()