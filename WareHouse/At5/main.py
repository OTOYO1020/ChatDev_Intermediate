'''
This file is the entry point of the software.
'''
from data import Data
from gui import MainWindow
import tkinter as tk
# Create an instance of the Data class
data = Data()
# Load the data from a file
data.load_data("input.txt")
# Process the data
result = data.process_data()
# Save the result to a file
data.save_data("output.txt")
# Create an instance of the MainWindow class
window = MainWindow(master=tk.Tk())
# Run the GUI application
window.mainloop()