'''
This file contains the Subtask class.
'''
import tkinter as tk
class Subtask(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Subtask")
        self.geometry("300x200")
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self, text="Default subtask details")
        self.label.pack(pady=10)
        self.close_button = tk.Button(self, text="Close", command=self.destroy)
        self.close_button.pack(pady=10)
    def show(self):
        self.deiconify()
    def solve_problem(self, A, B):
        '''
        This method finds the number of integers that satisfy the given condition using the sequences A and B.
        Parameters:
        - A: The first sequence of non-negative integers
        - B: The second sequence of non-negative integers
        Returns:
        - count: The number of integers that satisfy the condition
        '''
        count = 0
        for i in range(len(A) - len(B) + 1):
            subsequence = A[i:i+len(B)]
            ratio = B[0] / subsequence[0]
            if all(B[j] == subsequence[j] * ratio for j in range(len(B))):
                count += 1
        return count