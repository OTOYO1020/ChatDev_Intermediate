'''
This module contains the GomokuGUI class which handles the graphical user interface for Gomoku.
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
        self.status_label.pack()
        self.draw_board()
    def draw_board(self):
        for x in range(15):
            for y in range(15):
                button = tk.Button(self.master, text='', width=4, height=2,
                                   command=lambda x=x, y=y: self.on_click(x, y))
                button.grid(row=x, column=y)
                self.buttons[x][y] = button
    def on_click(self, x, y):
        result = self.game.make_move(x, y)
        if result:
            self.update_status(result)
        else:
            self.update_status(f"Player {self.game.current_player}'s turn")
        self.update_buttons()
    def update_buttons(self):
        for x in range(15):
            for y in range(15):
                if self.game.board[x][y] is not None:
                    self.buttons[x][y].config(text=self.game.board[x][y])
    def update_status(self, message):
        self.status_label.config(text=message)