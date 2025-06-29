'''
Contains the input frame for user interaction.
'''
import tkinter as tk
class InputFrame(tk.Frame):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback
        self.label_n = tk.Label(self, text="Enter N:")
        self.label_n.pack()
        self.entry_n = tk.Entry(self)
        self.entry_n.pack()
        self.label_k = tk.Label(self, text="Enter K:")
        self.label_k.pack()
        self.entry_k = tk.Entry(self)
        self.entry_k.pack()
        self.label_p = tk.Label(self, text="Enter permutation P (comma-separated):")
        self.label_p.pack()
        self.entry_p = tk.Entry(self)
        self.entry_p.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack()
    def submit(self):
        try:
            N = int(self.entry_n.get())
            K = int(self.entry_k.get())
            P = list(map(int, self.entry_p.get().split(',')))
            if K > N:
                raise ValueError("K should not be greater than N.")
            if len(P) != N or sorted(P) != list(range(1, N + 1)):
                raise ValueError(f"P must be a permutation of integers from 1 to {N} with unique values.")
            if len(set(P)) != N:  # Check for duplicates
                raise ValueError("P must contain unique values.")
            self.callback(N, K, P)  # Call the callback with the input values
        except ValueError as e:
            print(f"Invalid input: {e}")