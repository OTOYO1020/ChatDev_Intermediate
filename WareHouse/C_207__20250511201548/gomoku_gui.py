'''
This module contains the GUI for the Gomoku game using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class GomokuGUI:
    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("Gomoku Game")
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.create_widgets()
        self.status_label = tk.Label(self.window, text="Current Player: X")
        self.status_label.grid(row=15, column=0, columnspan=15)
    def create_widgets(self):
        for x in range(15):
            for y in range(15):
                button = tk.Button(self.window, text="", width=4, height=2,
                                   command=lambda x=x, y=y: self.on_button_click(x, y))
                button.grid(row=x, column=y)
                self.buttons[x][y] = button
        reset_button = tk.Button(self.window, text="Reset Game", command=self.reset_game)
        reset_button.grid(row=16, column=0, columnspan=15)
    def on_button_click(self, x, y):
        result = self.game.make_move(x, y)
        if result == True:
            self.draw_board()
            if self.game.winner:
                if self.game.winner == "Draw":
                    self.update_status("It's a draw!")
                    messagebox.showinfo("Game Over", "It's a draw!")
                else:
                    self.update_status(f"Player {self.game.winner} wins!")
                    messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
                self.reset_game()
        elif result == "Game over. No more moves allowed.":
            messagebox.showinfo("Game Over", result)
        else:
            messagebox.showwarning("Invalid Move", "This cell is already occupied. Please choose another cell.")
    def draw_board(self):
        for x in range(15):
            for y in range(15):
                if self.game.board[x][y] is not None:
                    self.buttons[x][y].config(text=self.game.board[x][y])
    def update_status(self, message):
        self.status_label.config(text=message)
    def reset_game(self):
        self.game.reset_game()
        self.draw_board()
        self.update_status("Current Player: X")
    def run(self):
        self.window.mainloop()