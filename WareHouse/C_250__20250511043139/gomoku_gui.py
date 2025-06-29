'''
This module contains the GUI for the Gomoku game using tkinter.
'''
import tkinter as tk
from gomoku_game import GomokuGame
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.game = GomokuGame()
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.status_label = tk.Label(master, text="Current Player: X")
        self.status_label.grid(row=15, column=0, columnspan=15)  # Place status label at the bottom
        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=16, column=0, columnspan=15)  # Place reset button below the status label
        self.draw_board()
    def draw_board(self):
        for row in range(15):
            for col in range(15):
                button = tk.Button(self.master, text='', width=4, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    def on_button_click(self, row, col):
        if self.game.board[row][col] is not None:
            self.update_status("Invalid move! Cell already occupied.")
            return  # Exit the function if the move is invalid
        self.game.make_move(row, col)
        self.update_board()
        if self.game.winner:
            self.update_status(f"Player {self.game.winner} wins!")
        else:
            self.update_status(f"Current Player: {self.game.current_player}")
    def update_board(self):
        for row in range(15):
            for col in range(15):
                if self.game.board[row][col] is not None:
                    self.buttons[row][col].config(text=self.game.board[row][col])
    def update_status(self, message):
        self.status_label.config(text=message)
    def reset_game(self):
        self.game.reset_game()
        self.update_board()
        self.update_status("Current Player: X")