'''
OutputFrame class to display results.
'''
from tkinter import Frame, Label
class OutputFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.result_label = Label(self, text="Result will be displayed here.")
        self.result_label.pack()
    def display_result(self, result):
        self.result_label.config(text=f"Minimum Cost: {result}")