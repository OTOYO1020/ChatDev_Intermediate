'''
InputFrame class for user input.
'''
import tkinter as tk
from tkinter import messagebox
class InputFrame(tk.Frame):
    def __init__(self, master, calculate_callback):
        super().__init__(master)
        self.calculate_callback = calculate_callback
        self.label_n = tk.Label(self, text="Enter N:")
        self.label_n.pack()
        self.entry_n = tk.Entry(self)
        self.entry_n.pack()
        self.label_k = tk.Label(self, text="Enter K:")
        self.label_k.pack()
        self.entry_k = tk.Entry(self)
        self.entry_k.pack()
        self.label_segments = tk.Label(self, text="Enter segments (L R) separated by commas:")
        self.label_segments.pack()
        self.entry_segments = tk.Entry(self)
        self.entry_segments.pack()
        self.calculate_button = tk.Button(self, text="Calculate", command=self.on_calculate)
        self.calculate_button.pack()
    def on_calculate(self):
        try:
            N = int(self.entry_n.get())
            K = int(self.entry_k.get())
            # Validate N and K
            if N <= 0:
                raise ValueError("N must be a positive integer.")
            if K <= 0:
                raise ValueError("K must be a positive integer.")
            segments_input = self.entry_segments.get()
            # Validate and parse segments
            segments = []
            for seg in segments_input.split(','):
                seg = seg.strip()  # Remove any leading/trailing whitespace
                if len(seg.split()) != 2:
                    raise ValueError("Each segment must contain exactly two integers.")
                L, R = map(int, seg.split())
                if L > R:
                    raise ValueError("Left endpoint must be less than or equal to right endpoint.")
                if L < 1 or R > N:
                    raise ValueError(f"Segment ({L}, {R}) must be within the bounds of 1 and {N}.")
                segments.append((L, R))
            self.calculate_callback(N, K, segments)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))