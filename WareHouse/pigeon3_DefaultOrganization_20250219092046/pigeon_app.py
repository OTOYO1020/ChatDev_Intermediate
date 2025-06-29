'''
Module to create the GUI for the Pigeon Management application.
'''
import tkinter as tk
from tkinter import messagebox
from pigeon_manager import PigeonManager
class PigeonApp:
    def __init__(self):
        self.manager = PigeonManager(100)  # Initialize with 100 pigeons
        self.window = tk.Tk()
        self.window.title("Pigeon Management System")
        self.pigeon_label = tk.Label(self.window, text="Pigeon Number:")
        self.pigeon_label.pack()
        self.pigeon_entry = tk.Entry(self.window)
        self.pigeon_entry.pack()
        self.nest_label = tk.Label(self.window, text="Nest Number:")
        self.nest_label.pack()
        self.nest_entry = tk.Entry(self.window)
        self.nest_entry.pack()
        self.move_button = tk.Button(self.window, text="Move Pigeon", command=self.move_pigeon)
        self.move_button.pack()
        self.count_button = tk.Button(self.window, text="Count Nests with Multiple Pigeons", command=self.count_nests)
        self.count_button.pack()
        self.output_area = tk.Text(self.window, height=10, width=50)
        self.output_area.pack()
    def move_pigeon(self):
        try:
            pigeon = int(self.pigeon_entry.get())
            new_nest = int(self.nest_entry.get())
            self.manager.move_pigeon(pigeon, new_nest)
            self.output_area.insert(tk.END, f"Pigeon {pigeon} moved to nest {new_nest}\n")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for pigeon and nest.")
    def count_nests(self):
        count = self.manager.count_multiple_pigeons()
        self.output_area.insert(tk.END, f"Number of nests with multiple pigeons: {count}\n")
    def run(self):
        self.window.mainloop()