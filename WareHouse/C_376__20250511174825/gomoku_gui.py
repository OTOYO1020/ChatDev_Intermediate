'''
This module contains the GUI for the Gomoku game.
'''
import tkinter as tk
from tkinter import messagebox
class GomokuGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.draw_board()
    def draw_board(self):
        for x in range(15):
            for y in range(15):
                button = tk.Button(self.master, text="", width=4, height=2,
                                   command=lambda x=x, y=y: self.on_button_click(x, y))
                button.grid(row=x, column=y)
                self.buttons[x][y] = button  # Assign the button to the corresponding position
        # Add a reset button
        reset_button = tk.Button(self.master, text="Reset Game", command=self.reset)
        reset_button.grid(row=15, column=0, columnspan=15)  # Place it below the board
    def on_button_click(self, x, y):
        if self.game.winner is None:  # Prevent moves after the game has ended
            if self.game.make_move(x, y):
                self.update_board(x, y)
                if self.game.winner:
                    self.show_winner(self.game.winner)
    def update_board(self, x, y):
        self.buttons[x][y].config(text=self.game.board[x][y])
    def show_winner(self, winner):
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset()
    def reset(self):
        self.game.reset_game()
        for x in range(15):
            for y in range(15):
                self.buttons[x][y].config(text="")