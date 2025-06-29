'''
This module contains the GUI for the Gomoku game using tkinter.
'''
import tkinter as tk
from gomoku import GomokuGame
class GomokuGUI:
    def __init__(self, master):
        '''
        Initializes the GUI components for the Gomoku game.
        '''
        self.master = master
        self.master.title("Gomoku Game")
        self.game = GomokuGame()
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.status_label = tk.Label(master, text="Current Player: X")
        self.status_label.grid(row=15, column=0, columnspan=15)
        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=16, column=0, columnspan=15)
        self.draw_board()
    def draw_board(self):
        '''
        Draws the game board with buttons for each cell.
        '''
        for row in range(15):
            for col in range(15):
                button = tk.Button(self.master, text=' ', width=4, height=2,
                                   command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    def handle_click(self, row, col):
        '''
        Handles the click event for a cell on the board.
        '''
        if self.game.winner is None:
            self.game.make_move(row, col)
            if self.game.winner:
                self.status_label.config(text=f"Player {self.game.winner} wins!")
            else:
                self.update_board()
                self.status_label.config(text=f"Current Player: {self.game.current_player}")
        else:
            self.status_label.config(text="Invalid move. The game has already been won.")
    def update_board(self):
        '''
        Updates the GUI to reflect the current state of the game board.
        '''
        for row in range(15):
            for col in range(15):
                self.buttons[row][col].config(text=self.game.board[row][col])
    def reset_game(self):
        '''
        Resets the game state and updates the GUI.
        '''
        self.game.reset_game()
        self.update_board()
        self.status_label.config(text="Current Player: X")