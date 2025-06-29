'''
This is the main module of the program.
It creates a GUI and runs it.
'''
import tkinter as tk
from gui import GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    gui.create_widgets()
    gui.run()