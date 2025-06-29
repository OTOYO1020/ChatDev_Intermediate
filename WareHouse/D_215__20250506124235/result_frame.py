'''
Module for creating the result frame to display results.
'''
from tkinter import Frame, Label
class ResultFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.result_label = Label(self, text="")
        self.result_label.pack()
    def display_results(self, results):
        if isinstance(results, list):
            results_str = ', '.join(map(str, results))
            self.result_label.config(text=f"Coprimes: {results_str}")
        else:
            self.result_label.config(text=results)