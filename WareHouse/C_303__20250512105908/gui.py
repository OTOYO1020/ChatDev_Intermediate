'''
Contains the GUI components and layout for the application.
'''
import tkinter as tk
from game_logic import can_complete_moves
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Takahashi Moves Game")
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter moves (R, L, U, D):")
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.grid_size_label = tk.Label(self.root, text="Enter grid size (M, N):")
        self.grid_size_label.pack()
        self.grid_size_entry = tk.Entry(self.root)
        self.grid_size_entry.pack()
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
    def submit(self):
        moves = self.entry.get()
        num_moves = len(moves)  # Renamed to avoid confusion
        # Get grid size from user input
        grid_size = self.grid_size_entry.get().split(',')
        M = int(grid_size[0].strip())  # Number of columns
        num_rows = int(grid_size[1].strip())  # Renamed to avoid confusion
        H = 10  # Initial health
        K = 10  # Health restore value
        items = [(1, 1), (2, 2)]  # Example item coordinates
        result = can_complete_moves(num_moves, M, H, K, moves, items)
        if result:
            self.result_label.config(text="YES")
        else:
            self.result_label.config(text="NO")
    def run(self):
        self.root.mainloop()