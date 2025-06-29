'''
This file contains the GUI implementation.
'''
import tkinter as tk
class GUI:
    def __init__(self, root):
        self.root = root
        self.create_widgets()
    def create_widgets(self):
        self.label_A = tk.Label(self.root, text="Enter sequence A:")
        self.label_A.pack()
        self.entry_A = tk.Entry(self.root)
        self.entry_A.pack()
        self.label_B = tk.Label(self.root, text="Enter sequence B:")
        self.label_B.pack()
        self.entry_B = tk.Entry(self.root)
        self.entry_B.pack()
        self.label_M = tk.Label(self.root, text="Enter M:")
        self.label_M.pack()
        self.entry_M = tk.Entry(self.root)
        self.entry_M.pack()
        self.button = tk.Button(self.root, text="Perform Task", command=self.perform_task)
        self.button.pack()
    def perform_task(self):
        A = [int(x) for x in self.entry_A.get().split()]
        B = [int(x) for x in self.entry_B.get().split()]
        M = int(self.entry_M.get())
        count, A, B, C = self.logic.perform_task(A, B, M)
        print("Number of integers satisfying the condition:", count)
        print("Updated sequence A:", A)
        print("Updated sequence B:", B)
        print("Updated sequence C:", C)
    def register_callback(self, callback):
        self.perform_task = callback