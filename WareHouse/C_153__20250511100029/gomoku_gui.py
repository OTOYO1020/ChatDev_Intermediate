'''
This module contains the GomokuGUI class, which creates the graphical user interface for the Gomoku game.
'''
import tkinter as tk
from gomoku import GomokuGame
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gomoku Game")
        self.game = GomokuGame()
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.status_label = None
        self.create_widgets()
    def create_widgets(self):
        self.status_label = tk.Label(self.master, text="Player X's turn")
        self.status_label.pack()
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.draw_board()
        # Add Reset Button
        reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        reset_button.pack()
    def draw_board(self):
        for row in range(15):
            for col in range(15):
                button = tk.Button(self.frame, width=4, height=2, command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    def on_button_click(self, row, col):
        result = self.game.make_move(row, col)
        if "wins" in result:
            self.buttons[row][col].config(text=self.game.current_player)  # Update button text for the winning move
            self.update_status(result)  # Update status to indicate the winner
            self.disable_buttons()  # Disable all buttons to prevent further moves
        elif "Invalid move" in result:
            self.update_status(result)  # Update status for invalid moves
        else:
            self.buttons[row][col].config(text=self.game.current_player)  # Update button text for the current player's move
            self.update_status(f"Player {self.game.current_player}'s turn")
    def update_status(self, message):
        self.status_label.config(text=message)
    def disable_buttons(self):
        for row in range(15):
            for col in range(15):
                self.buttons[row][col].config(state=tk.DISABLED)
    def reset_game(self):
        '''
        Resets the game state and updates the GUI for a new game.
        '''
        self.game.reset_game()
        for row in range(15):
            for col in range(15):
                self.buttons[row][col].config(text="", state=tk.NORMAL)
        self.update_status("Player X's turn")