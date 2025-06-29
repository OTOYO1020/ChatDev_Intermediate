'''
Output frame for displaying results in the stage time calculator.
'''
import tkinter as tk
class OutputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
    def display_result(self, result):
        self.result_label.config(text=result)