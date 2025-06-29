'''
This module contains the GomokuGUI class which handles the graphical user interface.
'''
import tkinter as tk
from gomoku_game import GomokuGame
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gomoku Game")
        self.game = GomokuGame()
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.status_label = tk.Label(master, text="Player X's turn")
        self.status_label.grid(row=0, column=0, columnspan=15)  # Use grid for status label
        self.create_board()
    def create_board(self):
        for row in range(15):
            for col in range(15):
                button = tk.Button(self.master, text=' ', width=3, height=1,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row + 1, column=col)  # Adjust row index for buttons
                self.buttons[row][col] = button  # Store button reference
        reset_button = tk.Button(self.master, text='Reset Game', command=self.reset_game)
        reset_button.grid(row=16, column=0, columnspan=15)  # Use grid for reset button
    def on_click(self, row, col):
        result = self.game.make_move(row, col)
        if result is None:  # Only update the button if the move was valid
            self.buttons[row][col].config(text='X' if self.game.current_player == 'X' else 'O')  # Update to show the current player's move
            if self.game.check_winner(row, col):
                self.update_status(f'Player {self.game.current_player} wins!')
                self.disable_buttons()  # Disable all buttons if there's a winner
            else:
                self.update_status(f"Player {self.game.current_player}'s turn")  # Update to show the current player's turn
        else:
            self.update_status("Invalid move, try again.")  # This message is already correct
    def update_status(self, message):
        self.status_label.config(text=message)
    def disable_buttons(self):
        for row in range(15):
            for col in range(15):
                self.buttons[row][col].config(state=tk.DISABLED)  # Disable all buttons
    def reset_game(self):
        self.game.reset_game()
        for row in range(15):
            for col in range(15):
                self.buttons[row][col].config(text=' ', state=tk.NORMAL)  # Reset button text and state
        self.update_status("Player X's turn")  # Reset status label