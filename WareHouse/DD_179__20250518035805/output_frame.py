'''
OutputFrame class for displaying results.
'''
import tkinter as tk
class OutputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.result_label = tk.Label(self, text="Result will be displayed here.")
        self.result_label.pack()
    def display_result(self, result):
        self.result_label.config(text=f"Number of ways: {result}")