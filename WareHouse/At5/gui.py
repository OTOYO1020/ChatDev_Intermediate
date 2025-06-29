'''
This file contains the GUI classes and functions.
'''
import tkinter as tk
from data import Data
class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.data = Data()
        # Create GUI elements
        self.label = tk.Label(self, text="Welcome to the Software")
        self.label.pack()
        self.button = tk.Button(self, text="Click Me", command=self.button_click)
        self.button.pack()
        self.pack()
    def button_click(self):
        # Load the data from a file
        self.data.load_data("input.txt")
        # Process the data
        result = self.data.process_data()
        # Save the result to a file
        self.data.save_data("output.txt")
        # Update the label text
        self.label.config(text=f"Number of matches: {result}")
# Other GUI classes and functions can be added here