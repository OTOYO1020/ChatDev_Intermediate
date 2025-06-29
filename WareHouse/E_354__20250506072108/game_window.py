'''
Contains the GameWindow class that creates the GUI for the game.
'''
import tkinter as tk
from tkinter import messagebox
from card_game import CardGame
class GameWindow:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(master, text="Enter card pairs (A_i B_i):")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def start_game(self):
        input_data = self.entry.get().strip().split()
        N = len(input_data) // 2
        if N < 1 or N > 18 or len(input_data) != 2 * N:
            messagebox.showerror("Input Error", "Please enter a valid number of card pairs (1-18).")
            return
        A = list(map(int, input_data[:N]))
        B = list(map(int, input_data[N:]))
        game = CardGame(A, B)
        winner = game.play_game(0)
        self.update_display(winner)
    def update_display(self, winner):
        self.result_label.config(text=f"The winner is: {winner}")
        messagebox.showinfo("Game Over", f"The winner is: {winner}")