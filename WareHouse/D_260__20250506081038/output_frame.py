'''
Contains the output frame for displaying results.
'''
import tkinter as tk
class OutputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_result = tk.Label(self, text="Results:")
        self.label_result.pack()
        self.result_text = tk.Text(self, height=10, width=50)
        self.result_text.pack()
    def update_output(self, results):
        self.result_text.delete(1.0, tk.END)  # Clear previous results
        self.result_text.insert(tk.END, str(results))  # Display new results