'''
Input frame to gather user input for the list of integers and operations.
'''
import tkinter as tk
class InputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_a = tk.Label(self, text="Enter List of Integers (comma-separated):")
        self.label_a.pack()
        self.entry_a = tk.Entry(self)
        self.entry_a.pack()
        self.label_ops = tk.Label(self, text="Enter Operations (B_i, C_i) as (B,C):")
        self.label_ops.pack()
        self.entry_ops = tk.Entry(self)
        self.entry_ops.pack()
    def get_input(self):
        try:
            A = list(map(int, self.entry_a.get().split(',')))
            operations = []
            for op in self.entry_ops.get().split(';'):
                op = op.strip()  # Trim whitespace
                if op.startswith('(') and op.endswith(')'):
                    op = op[1:-1]  # Remove parentheses
                    B, C = map(int, op.split(','))
                    operations.append((B, C))
                else:
                    raise ValueError("Each operation must be in the format (B,C).")
            N = len(A)
            Q = len(operations)
            return N, Q, A, operations
        except ValueError as e:
            raise ValueError(f"Invalid input: {e}. Please ensure all entries are integers and operations are in the format (B,C).")