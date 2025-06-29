'''
This module contains the GUI for the Pigeon Management application.
'''
import tkinter as tk
from tkinter import messagebox
from pigeon_manager import PigeonManager
class PigeonApp:
    def __init__(self):
        self.manager = PigeonManager(10)  # Initialize with 10 pigeons
        self.root = tk.Tk()
        self.root.title("Pigeon Management System")
        # Create GUI components
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Pigeon ID:").grid(row=0, column=0)
        self.pigeon_id_entry = tk.Entry(self.root)
        self.pigeon_id_entry.grid(row=0, column=1)
        tk.Label(self.root, text="Nest ID:").grid(row=1, column=0)
        self.nest_id_entry = tk.Entry(self.root)
        self.nest_id_entry.grid(row=1, column=1)
        self.move_button = tk.Button(self.root, text="Move Pigeon", command=self.move_pigeon)
        self.move_button.grid(row=2, columnspan=2)
        self.count_button = tk.Button(self.root, text="Count Nests", command=self.count_nests)
        self.count_button.grid(row=3, columnspan=2)
    def move_pigeon(self):
        try:
            pigeon_id = int(self.pigeon_id_entry.get())
            nest_id = int(self.nest_id_entry.get())
            self.manager.move_pigeon(pigeon_id, nest_id)
            messagebox.showinfo("Success", f"Pigeon {pigeon_id} moved to Nest {nest_id}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer IDs.")
    def count_nests(self):
        count = self.manager.count_multiple_pigeons()
        messagebox.showinfo("Count of Nests", f"Nests with multiple pigeons: {count}")
    def run(self):
        self.root.mainloop()