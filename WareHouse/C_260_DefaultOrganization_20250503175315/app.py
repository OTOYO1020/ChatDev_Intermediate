'''
This module contains the App class that defines the GUI for the jewel conversion application.
'''
import tkinter as tk
from tkinter import messagebox
from jewel_converter import JewelConverter
class App:
    def __init__(self, master):
        self.master = master
        master.title("Jewel Converter")
        self.label_n = tk.Label(master, text="Enter level of red jewel (N):")
        self.label_n.pack()
        self.entry_n = tk.Entry(master)
        self.entry_n.pack()
        self.label_x = tk.Label(master, text="Enter blue jewels from red jewel (X):")
        self.label_x.pack()
        self.entry_x = tk.Entry(master)
        self.entry_x.pack()
        self.label_y = tk.Label(master, text="Enter blue jewels from blue jewel (Y):")
        self.label_y.pack()
        self.entry_y = tk.Entry(master)
        self.entry_y.pack()
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def calculate(self):
        try:
            N = int(self.entry_n.get())
            X = int(self.entry_x.get())
            Y = int(self.entry_y.get())
            converter = JewelConverter(N, X, Y)
            total_blue_jewels = converter.convert_jewels()
            self.result_label.config(text=f"Total blue jewels of level 1: {total_blue_jewels}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for N, X, and Y.")