'''
Defines the App class for the GUI of the block simulation application.
'''
import tkinter as tk
from tkinter import messagebox
from block import Block
from block_simulator import BlockSimulator
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Block Simulation")
        self.label = tk.Label(master, text="Enter number of blocks (N):")
        self.label.pack()
        self.n_entry = tk.Entry(master)
        self.n_entry.pack()
        self.height_label = tk.Label(master, text="Enter simulation height:")
        self.height_label.pack()
        self.height_entry = tk.Entry(master)
        self.height_entry.pack()
        self.block_entries = []  # To store block position entries
        self.add_block_button = tk.Button(master, text="Add Block Position", command=self.add_block_entry)
        self.add_block_button.pack()
        self.simulate_button = tk.Button(master, text="Simulate", command=self.run_simulation)
        self.simulate_button.pack()
        self.query_label = tk.Label(master, text="Enter block ID and time (A, T):")
        self.query_label.pack()
        self.query_entry = tk.Entry(master)
        self.query_entry.pack()
        self.query_button = tk.Button(master, text="Query", command=self.handle_query)
        self.query_button.pack()
        self.blocks = []
        self.simulator = None
    def add_block_entry(self):
        entry = tk.Entry(self.master)
        entry.pack()
        self.block_entries.append(entry)
    def run_simulation(self):
        try:
            n = int(self.n_entry.get())
            self.blocks = []
            for entry in self.block_entries:
                x, y = map(int, entry.get().split())
                if x < 0 or x >= int(self.height_entry.get()) or y < 0:
                    messagebox.showerror("Error", "Block position must be within the simulation width and non-negative.")
                    return
                self.blocks.append(Block(x, y, len(self.blocks) + 1))  # Assign unique ID
            height = int(self.height_entry.get())
            if height < max(y for _, y in self.blocks):
                messagebox.showerror("Error", "Simulation height must be greater than the maximum y-coordinate of the blocks.")
                return
            self.simulator = BlockSimulator(self.blocks)
            self.simulator.simulate(height)
            messagebox.showinfo("Simulation", "Simulation completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def handle_query(self):
        try:
            a, t = map(int, self.query_entry.get().split())
            result = self.simulator.query(a, t)
            if result:
                messagebox.showinfo("Query Result", f"Block {a} exists at time {t + 0.5}.")
            else:
                messagebox.showinfo("Query Result", f"Block {a} does not exist at time {t + 0.5}.")
        except Exception as e:
            messagebox.showerror("Error", str(e))