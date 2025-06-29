'''
This module contains the GUI for the Gomoku game using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from gomoku_game import GomokuGame  # Import the GomokuGame class
class GomokuGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Gomoku Game")
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.create_widgets()
        self.status_label = tk.Label(self.root, text="Current Player: X")
        self.status_label.grid(row=15, column=0, columnspan=15)
    def create_widgets(self):
        for row in range(15):
            for col in range(15):
                button = tk.Button(self.root, text="", width=4, height=2,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    def on_click(self, row, col):
        move_result, game_over_message = self.game.make_move(row, col)
        if move_result is False:
            messagebox.showwarning("Invalid Move", game_over_message)  # Provide feedback on invalid move
        else:
            self.update_board()
            if self.game.winner:
                messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
                self.reset_game()
    def update_board(self):
        for row in range(15):
            for col in range(15):
                if self.game.board[row][col] is not None:
                    self.buttons[row][col].config(text=self.game.board[row][col])
        if not self.game.winner:
            self.update_status()
    def update_status(self):
        self.status_label.config(text=f"Current Player: {self.game.current_player}")
    def reset_game(self):
        self.game.reset_game()
        self.update_board()
        self.status_label.config(text="Current Player: X")
    def run(self):
        self.root.mainloop()