'''
Contains the GUI for the Gomoku game.
'''
import tkinter as tk
from tkinter import messagebox
from gomoku_game import GomokuGame
class GomokuGUI:
    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("Gomoku Game")
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.create_widgets()
    def create_widgets(self):
        '''
        Creates the GUI widgets for the game.
        '''
        for row in range(15):
            for col in range(15):
                button = tk.Button(self.window, text=' ', width=4, height=2,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
        self.status_label = tk.Label(self.window, text="Current Player: X")
        self.status_label.grid(row=15, column=0, columnspan=15)  # Place status label below the board
        self.reset_button = tk.Button(self.window, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=16, column=0, columnspan=15)  # Place reset button below the status label
    def on_click(self, row, col):
        '''
        Handles the click event on the game board.
        '''
        try:
            self.game.make_move(row, col)
            self.update_board()
            self.update_status()  # Update the status label after each move
            if self.game.winner:
                messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
        except ValueError as e:
            messagebox.showwarning("Invalid Move", str(e))
    def update_board(self):
        '''
        Updates the GUI board to reflect the current game state.
        '''
        for row in range(15):
            for col in range(15):
                self.buttons[row][col].config(text=self.game.board[row][col])
    def update_status(self):
        '''
        Updates the status label to show the current player or the winner.
        '''
        if self.game.winner:
            self.status_label.config(text=f"Player {self.game.winner} wins!")
        else:
            self.status_label.config(text=f"Current Player: {self.game.current_player}")
    def reset_game(self):
        '''
        Resets the game when the reset button is clicked.
        '''
        if messagebox.askyesno("Reset Game", "Are you sure you want to reset the game?"):
            self.game.reset_game()
            self.update_board()
            self.status_label.config(text="Current Player: X")
    def run(self):
        '''
        Runs the GUI main loop.
        '''
        self.window.mainloop()