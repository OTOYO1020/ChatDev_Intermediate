'''
Contains the GameApp class that creates the GUI for the game.
'''
import tkinter as tk
from tkinter import messagebox
from game import Game
class GameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Takahashi vs Aoki Game")
        self.label = tk.Label(master, text="Enter N:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()
        self.declare_button = tk.Button(master, text="Declare", command=self.declare, state=tk.DISABLED)
        self.declare_button.pack()
        self.output_label = tk.Label(master, text="")
        self.output_label.pack()
        # New entry field for Aoki's declaration
        self.aoki_label = tk.Label(master, text="Enter Aoki's declaration:")
        self.aoki_label.pack()
        self.aoki_entry = tk.Entry(master)
        self.aoki_entry.pack()
        self.game = None
    def start_game(self):
        try:
            N = int(self.entry.get())
            self.game = Game(N)
            self.output_label.config(text="Game Started! Click 'Declare' to make a move.")
            self.declare_button.config(state=tk.NORMAL)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer for N.")
    def declare(self):
        if self.game:
            takahashi_declaration = self.game.declare_number()
            self.output_label.config(text=f"Takahashi declares: {takahashi_declaration}")
            self.game.add_declared_number(takahashi_declaration)
            try:
                # Get Aoki's declaration from the new entry field
                aoki_declaration = int(self.aoki_entry.get())
                if aoki_declaration < 1 or aoki_declaration > self.game.range_limit or aoki_declaration in self.game.declared_numbers:
                    messagebox.showerror("Input Error", "Aoki's declaration must be a valid integer within the range and not previously declared.")
                else:
                    if self.game.is_game_over(aoki_declaration):
                        self.end_game()
                    else:
                        self.game.add_declared_number(aoki_declaration)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid integer for Aoki's declaration.")
    def end_game(self):
        self.output_label.config(text="Game Over!")
        self.declare_button.config(state=tk.DISABLED)