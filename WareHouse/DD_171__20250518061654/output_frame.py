'''
Output frame to display the results of the operations performed on the list.
'''
import tkinter as tk
class OutputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_results = tk.Label(self, text="Results:")
        self.label_results.pack()
        self.results_text = tk.Text(self, height=10, width=50)
        self.results_text.pack()
    def display_results(self, results):
        self.results_text.delete(1.0, tk.END)  # Clear previous results
        for result in results:
            self.results_text.insert(tk.END, f"{result}\n")