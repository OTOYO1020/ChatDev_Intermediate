'''
Output frame to display the result of the calculation.
'''
import tkinter as tk
class OutputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_result = tk.Label(self, text="Result:")
        self.label_result.grid(row=0, column=0)
        self.result_var = tk.StringVar()
        self.label_display = tk.Label(self, textvariable=self.result_var)
        self.label_display.grid(row=0, column=1)
    def display_result(self, result):
        self.result_var.set(result)