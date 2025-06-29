'''
Manages the GUI components for the maze application.
'''
import tkinter as tk
from tkinter import messagebox
from maze import max_moves
class MazeApp:
    def __init__(self, master):
        self.master = master
        master.title("Maze Max Moves Calculator")
        self.label = tk.Label(master, text="Enter maze dimensions (H W):")
        self.label.pack()
        self.dimensions_entry = tk.Entry(master)
        self.dimensions_entry.pack()
        self.maze_label = tk.Label(master, text="Enter maze rows (one per line):")
        self.maze_label.pack()
        self.maze_text = tk.Text(master, height=10, width=30)
        self.maze_text.pack()
        self.calculate_button = tk.Button(master, text="Calculate Max Moves", command=self.calculate_max_moves)
        self.calculate_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def calculate_max_moves(self):
        '''
        Calculates the maximum moves when the button is pressed.
        '''
        try:
            dimensions = self.dimensions_entry.get().split()
            H = int(dimensions[0])
            W = int(dimensions[1])
            S = self.maze_text.get("1.0", tk.END).strip().splitlines()
            S = [row.strip() for row in S]  # Trim each row
            if len(S) != H:
                raise ValueError("Number of rows does not match the specified height.")
            # Validate maze representation
            for row in S:
                if len(row) != W or any(char not in ('.', '#') for char in row):
                    raise ValueError("Each row must have exactly W characters and can only contain '.' and '#' characters.")
            max_moves_result = max_moves(H, W, S)
            self.result_label.config(text=f"Max Moves: {max_moves_result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))