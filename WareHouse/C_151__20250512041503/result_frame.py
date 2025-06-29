'''
Module for displaying results in the application.
'''
import tkinter as tk
class ResultFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
    def display_results(self, correct_answers: int, penalties: int):
        result_text = f"Correct Answers: {correct_answers}\nTotal Penalties: {penalties}"
        self.result_label.config(text=result_text)