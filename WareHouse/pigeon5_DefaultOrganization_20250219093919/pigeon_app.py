'''
PigeonApp class to create the GUI for managing pigeons and nests.
'''
import tkinter as tk
from pigeon_manager import PigeonManager
class PigeonApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pigeon Management Dashboard")
        self.manager = PigeonManager(2, 2)  # Initialize with 2 pigeons and 2 nests
        self.pigeon_id_label = tk.Label(master, text="Pigeon ID:")
        self.pigeon_id_label.pack()
        self.pigeon_id_entry = tk.Entry(master)
        self.pigeon_id_entry.pack()
        self.nest_id_label = tk.Label(master, text="Nest ID:")
        self.nest_id_label.pack()
        self.nest_id_entry = tk.Entry(master)
        self.nest_id_entry.pack()
        self.move_button = tk.Button(master, text="Move Pigeon", command=self.move_pigeon)
        self.move_button.pack()
        self.count_button = tk.Button(master, text="Count Nests with Multiple Pigeons", command=self.count_nests)
        self.count_button.pack()
    def move_pigeon(self):
        try:
            pigeon_id = int(self.pigeon_id_entry.get())
            nest_id = int(self.nest_id_entry.get())
            self.manager.move_pigeon(pigeon_id, nest_id)
            tk.messagebox.showinfo("Success", f"Pigeon {pigeon_id} moved to Nest {nest_id}.")
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))
    def count_nests(self):
        count = self.manager.count_multiple_pigeons()
        tk.messagebox.showinfo("Count", f"Number of nests with multiple pigeons: {count}")