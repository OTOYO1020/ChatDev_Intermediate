'''
This module contains the GomokuGUI class which manages the graphical user interface.
'''
import tkinter as tk
from gomoku import GomokuGame
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gomoku Game")
        self.game = GomokuGame()
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.status_label = tk.Label(master, text="Player X's turn")
        self.status_label.pack()
        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()
        self.draw_board()
    def draw_board(self):
        for row in range(15):
            for col in range(15):
                button = tk.Button(self.master, text=' ', width=4, height=2,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    def on_click(self, row, col):
        if self.game.board[row][col] != ' ':
            self.update_status("Cell already occupied! Please choose another cell.")
            return  # Exit the method if the cell is already occupied
        result = self.game.make_move(row, col)
        self.buttons[row][col].config(text=self.game.current_player)  # Update to show the symbol of the player who just made the move
        if result:
            self.update_status(result)  # Update status to show the winner
            self.disable_buttons()  # Disable buttons after a win
        else:
            self.update_status(f"Player {'O' if self.game.current_player == 'X' else 'X'}'s turn")  # Update to show the next player's turn
    def update_status(self, message):
        self.status_label.config(text=message)
    def reset_game(self):
        self.game.reset_game()
        for row in range(15):
            for col in range(15):
                self.buttons[row][col].config(text=' ')
        self.update_status("Player X's turn")
        self.enable_buttons()  # Re-enable buttons when the game is reset
    def disable_buttons(self):
        for row in range(15):
            for col in range(15):
                self.buttons[row][col].config(state=tk.DISABLED)
    def enable_buttons(self):
        for row in range(15):
            for col in range(15):
                self.buttons[row][col].config(state=tk.NORMAL)