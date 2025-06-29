'''
This module contains the GomokuGUI class that manages the GUI for the Gomoku game.
'''
import tkinter as tk
from gomoku_game import GomokuGame
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.game = GomokuGame()
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.status_label = None  # Initialize status_label
        self.draw_board()
        self.update_status("Player X's turn")
    def draw_board(self):
        self.status_label = tk.Label(self.master, text="Player X's turn", font=("Arial", 12))
        self.status_label.grid(row=0, column=0, columnspan=15)
        reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        reset_button.grid(row=1, column=0, columnspan=15)  # Add reset button below the status label
        for i in range(15):
            for j in range(15):
                button = tk.Button(self.master, text="", width=3, command=lambda x=i, y=j: self.on_click(x, y))
                button.grid(row=i + 2, column=j)  # Offset by 2 for the status label and reset button
                self.buttons[i][j] = button
    def on_click(self, x, y):
        if self.game.game_over:  # Prevent further moves if the game has ended
            return
        result = self.game.make_move(x, y)
        if result:
            self.update_status(result)
            if "wins" in result:  # If a player wins, disable all buttons
                self.disable_buttons()
        else:
            self.update_status(f"Player {self.game.current_player}'s turn")
        self.redraw_board()
    def redraw_board(self):
        for i in range(15):
            for j in range(15):
                if self.game.board[i][j] == "X":
                    self.buttons[i][j].config(text="X", bg="lightblue")
                elif self.game.board[i][j] == "O":
                    self.buttons[i][j].config(text="O", bg="lightgreen")
    def update_status(self, message):
        self.status_label.config(text=message)
    def disable_buttons(self):
        for i in range(15):
            for j in range(15):
                self.buttons[i][j].config(state=tk.DISABLED)  # Disable all buttons
        self.update_status("Game Over! Click 'Reset Game' to play again.")
    def reset_game(self):
        self.game.reset_game()
        self.redraw_board()
        self.update_status("Player X's turn")