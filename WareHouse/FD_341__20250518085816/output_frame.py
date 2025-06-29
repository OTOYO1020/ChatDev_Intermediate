'''
OutputFrame class to display the output results.
'''
from tkinter import Frame, Label
class OutputFrame(Frame):
    def __init__(self):
        super().__init__()
        self.result_label = Label(self, text="Result: ")
        self.result_label.pack()
    def display_result(self, result):
        self.result_label.config(text=f"Result: {result}")