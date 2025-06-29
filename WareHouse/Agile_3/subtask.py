'''
This file contains the Subtask class.
'''
import tkinter as tk
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self, text="Default subtask details")
        self.label.pack()
        self.button = tk.Button(self, text="Click Me", command=self.button_click)
        self.button.pack()
    def button_click(self):
        self.label.config(text="Button clicked!")