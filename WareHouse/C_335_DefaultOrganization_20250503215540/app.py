'''
Module to create the GUI for the Dragon Movement application.
'''
import tkinter as tk
from tkinter import messagebox
from dragon import Dragon
class App:
    def __init__(self, master):
        '''
        Initializes the main application window and its components.
        '''
        self.master = master
        self.master.title("Dragon Movement")
        # Entry for number of parts
        self.parts_label = tk.Label(master, text="Enter Number of Parts:")
        self.parts_label.pack()
        self.parts_entry = tk.Entry(master)
        self.parts_entry.pack()
        self.initialize_button = tk.Button(master, text="Initialize Dragon", command=self.initialize_dragon)
        self.initialize_button.pack()
        self.direction_label = tk.Label(master, text="Enter Direction (R, L, U, D):")
        self.direction_label.pack()
        self.direction_entry = tk.Entry(master)
        self.direction_entry.pack()
        self.move_button = tk.Button(master, text="Move Dragon", command=self.move_dragon)
        self.move_button.pack()
        self.part_label = tk.Label(master, text="Enter Part Number to Get Position:")
        self.part_label.pack()
        self.part_entry = tk.Entry(master)
        self.part_entry.pack()
        self.position_button = tk.Button(master, text="Get Position", command=self.get_part_position)
        self.position_button.pack()
        self.output_label = tk.Label(master, text="")
        self.output_label.pack()
    def initialize_dragon(self):
        '''
        Initializes the dragon with the number of parts specified by the user.
        '''
        try:
            n = int(self.parts_entry.get())
            if n > 0:
                self.dragon = Dragon(n)  # Initialize dragon with user-defined parts
                self.output_label.config(text=f"Dragon initialized with {n} parts.")
            else:
                messagebox.showerror("Invalid Input", "Number of parts must be a positive integer.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer for number of parts.")
    def move_dragon(self):
        '''
        Handles the movement of the dragon based on user input.
        '''
        direction = self.direction_entry.get().strip().upper()
        if direction in ['R', 'L', 'U', 'D']:
            self.dragon.move(direction)
            self.output_label.config(text=f"Dragon moved {direction}.")
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid direction (R, L, U, D).")
    def get_part_position(self):
        '''
        Retrieves and displays the position of a specified part.
        '''
        try:
            part_number = int(self.part_entry.get())
            if 1 <= part_number <= len(self.dragon.positions):
                position = self.dragon.get_position(part_number)
                self.output_label.config(text=f"Position of part {part_number}: {position}")
            else:
                messagebox.showerror("Invalid Input", "Part number must be between 1 and the number of parts.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer for part number.")