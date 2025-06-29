'''
Contains the MainApp class for the GUI of the block simulation application.
'''
import tkinter as tk
from tkinter import ttk
from block_simulator import BlockSimulator
from input_handler import InputHandler
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Block Simulation")
        self.create_widgets()
    def create_widgets(self):
        # Create input fields and buttons
        self.label_N = ttk.Label(self.root, text="Number of Blocks (N):")
        self.label_N.grid(column=0, row=0)
        self.entry_N = ttk.Entry(self.root)
        self.entry_N.grid(column=1, row=0)
        self.label_W = ttk.Label(self.root, text="Number of Columns (W):")
        self.label_W.grid(column=0, row=1)
        self.entry_W = ttk.Entry(self.root)
        self.entry_W.grid(column=1, row=1)
        self.label_blocks = ttk.Label(self.root, text="Blocks (x,y):")
        self.label_blocks.grid(column=0, row=2)
        self.entry_blocks = ttk.Entry(self.root)
        self.entry_blocks.grid(column=1, row=2)
        self.label_Q = ttk.Label(self.root, text="Number of Queries (Q):")
        self.label_Q.grid(column=0, row=3)
        self.entry_Q = ttk.Entry(self.root)
        self.entry_Q.grid(column=1, row=3)
        self.label_queries = ttk.Label(self.root, text="Queries (index,time):")
        self.label_queries.grid(column=0, row=4)
        self.entry_queries = ttk.Entry(self.root)
        self.entry_queries.grid(column=1, row=4)
        self.button_run = ttk.Button(self.root, text="Run Simulation", command=self.run_simulation)
        self.button_run.grid(column=0, row=5, columnspan=2)
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.grid(column=0, row=6, columnspan=2)
    def run_simulation(self):
        try:
            N = int(self.entry_N.get())
            W = int(self.entry_W.get())
            blocks = eval(self.entry_blocks.get())
            Q = int(self.entry_Q.get())
            queries = eval(self.entry_queries.get())
            InputHandler.get_input(N, W, blocks, Q, queries)
            simulator = BlockSimulator(N, W, blocks, Q, queries)
            results = [simulator.block_exists(index, time) for index, time in queries]
            self.update_output(results)
        except Exception as e:
            InputHandler.display_error(str(e))
    def update_output(self, results):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "\n".join(results))
    def run(self):
        self.root.mainloop()