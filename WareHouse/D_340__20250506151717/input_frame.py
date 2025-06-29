'''
Input frame for the stage time calculator.
'''
import tkinter as tk
class InputFrame(tk.Frame):
    def __init__(self, master, calculate_callback):
        super().__init__(master)
        self.calculate_callback = calculate_callback
        self.label_n = tk.Label(self, text="Number of Stages (N):")
        self.label_n.pack()
        self.entry_n = tk.Entry(self)
        self.entry_n.pack()
        self.label_a = tk.Label(self, text="Times for Action A (comma-separated):")
        self.label_a.pack()
        self.entry_a = tk.Entry(self)
        self.entry_a.pack()
        self.label_b = tk.Label(self, text="Times for Action B (comma-separated):")
        self.label_b.pack()
        self.entry_b = tk.Entry(self)
        self.entry_b.pack()
        self.label_x = tk.Label(self, text="Accessible Stages (comma-separated):")
        self.label_x.pack()
        self.entry_x = tk.Entry(self)
        self.entry_x.pack()
        self.calculate_button = tk.Button(self, text="Calculate", command=self.on_calculate)
        self.calculate_button.pack()
    def on_calculate(self):
        self.calculate_callback()
    def get_input(self):
        try:
            N = int(self.entry_n.get())
            if N <= 1:
                raise ValueError("N must be greater than 1.")
            A = list(map(int, self.entry_a.get().split(',')))
            B = list(map(int, self.entry_b.get().split(',')))
            X = list(map(int, self.entry_x.get().split(',')))
            # Validate lengths of A, B, and X
            if len(A) != N - 1 or len(B) != N - 1 or len(X) != N - 1:
                raise ValueError("A, B, and X must have exactly N-1 elements.")
            return N, A, B, X
        except ValueError as e:
            print(f"Input Error: {e}")  # Provide feedback in the console or UI
            return None, None, None, None  # Invalid lengths