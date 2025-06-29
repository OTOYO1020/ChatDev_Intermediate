'''
Contains the App class for the GUI application.
'''
import tkinter as tk
from tkinter import messagebox
from grid import Grid
class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Shortest Path Finder")
        self.create_widgets()
    def create_widgets(self):
        self.input_frame = tk.Frame(self.window)
        self.input_frame.pack()
        self.label_H = tk.Label(self.input_frame, text="Height (H):")
        self.label_H.grid(row=0, column=0)
        self.entry_H = tk.Entry(self.input_frame)
        self.entry_H.grid(row=0, column=1)
        self.label_W = tk.Label(self.input_frame, text="Width (W):")
        self.label_W.grid(row=1, column=0)
        self.entry_W = tk.Entry(self.input_frame)
        self.entry_W.grid(row=1, column=1)
        self.label_grid = tk.Label(self.input_frame, text="Grid (use '#' for walls, 'S' for start, 'G' for goal):")
        self.label_grid.grid(row=2, column=0, columnspan=2)
        self.text_grid = tk.Text(self.input_frame, height=10, width=30)
        self.text_grid.grid(row=3, column=0, columnspan=2)
        self.button_find = tk.Button(self.input_frame, text="Find Shortest Path", command=self.find_shortest_path)
        self.button_find.grid(row=4, column=0, columnspan=2)
    def find_shortest_path(self):
        try:
            H = int(self.entry_H.get())
            W = int(self.entry_W.get())
            grid_input = self.text_grid.get("1.0", tk.END).strip().splitlines()
            grid = [list(row) for row in grid_input]
            if len(grid) != H or any(len(row) != W for row in grid):
                raise ValueError("Grid dimensions do not match specified height and width.")
            if sum(row.count('S') for row in grid) != 1 or sum(row.count('G') for row in grid) != 1:
                raise ValueError("Grid must contain exactly one 'S' and one 'G'.")
            grid_obj = Grid(H, W, grid)
            result = grid_obj.find_shortest_time()
            messagebox.showinfo("Result", f"Shortest time: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def run(self):
        self.window.mainloop()