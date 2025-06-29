'''
Module for the GUI of the grid painting application.
'''
import tkinter as tk
from tkinter import messagebox
from grid_painter import GridPainter
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Grid Painter")
        self.grid_painter = GridPainter(5, 5)  # Example grid size 5x5
        self.row_entry = tk.Entry(master)
        self.row_entry.pack()
        self.row_entry.insert(0, "Row (0-4)")
        self.column_entry = tk.Entry(master)
        self.column_entry.pack()
        self.column_entry.insert(0, "Column (0-4)")
        self.color_entry = tk.Entry(master)
        self.color_entry.pack()
        self.color_entry.insert(0, "Color (int)")
        self.paint_row_button = tk.Button(master, text="Paint Row", command=self.paint_row)
        self.paint_row_button.pack()
        self.paint_column_button = tk.Button(master, text="Paint Column", command=self.paint_column)
        self.paint_column_button.pack()
        self.color_count_button = tk.Button(master, text="Count Colors", command=self.update_color_count)
        self.color_count_button.pack()
        self.color_count_label = tk.Label(master, text="")
        self.color_count_label.pack()
    def paint_row(self):
        try:
            row = int(self.row_entry.get())
            color = int(self.color_entry.get())
            self.grid_painter.apply_paint([(1, row, color)])  # Paint row with the specified color
            messagebox.showinfo("Success", f"Row {row} painted with color {color}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for row and color.")
    def paint_column(self):
        try:
            column = int(self.column_entry.get())
            color = int(self.color_entry.get())
            self.grid_painter.apply_paint([(2, column, color)])  # Paint column with the specified color
            messagebox.showinfo("Success", f"Column {column} painted with color {color}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for column and color.")
    def update_color_count(self):
        color_count = self.grid_painter.count_colors()
        self.color_count_label.config(text=str(color_count))