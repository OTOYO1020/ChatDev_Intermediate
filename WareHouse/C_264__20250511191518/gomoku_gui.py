'''
This module contains the GUI for the Gomoku game using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox  # Import messagebox for displaying alerts
from gomoku import GomokuGame
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gomoku Game")
        self.game = GomokuGame()
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.status_label = tk.Label(master, text="Current Player: X")
        self.status_label.grid(row=15, column=0, columnspan=15)  # Changed to grid
        self.create_board()
        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=16, column=0, columnspan=15)  # Added reset button
    def create_board(self):
        for row in range(15):
            for col in range(15):
                button = tk.Button(self.master, text="", width=4, height=2,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button  # Store the button reference
    def on_click(self, row, col):
        if self.game.board[row][col] is not None:
            messagebox.showinfo("Invalid Move", "This cell is already occupied. Please choose another cell.")
            return  # Exit the method if the move is invalid
        self.game.make_move(row, col)
        self.update_board()
        if self.game.winner:
            self.status_label.config(text=f"Player {self.game.winner} wins!")
        elif all(cell is not None for row in self.game.board for cell in row):
            self.status_label.config(text="It's a draw!")  # Check for draw condition
        else:
            self.status_label.config(text=f"Current Player: {self.game.current_player}")
    def update_board(self):
        for row in range(15):
            for col in range(15):
                if self.game.board[row][col] is not None:
                    self.buttons[row][col].config(text=self.game.board[row][col])
    def reset_game(self):
        self.game.reset_game()
        self.update_board()
        self.status_label.config(text="Current Player: X")