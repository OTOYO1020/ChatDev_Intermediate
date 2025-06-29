'''
Contains the GUI logic for the Gomoku game.
'''
import tkinter as tk
from gomoku import GomokuGame
class GomokuGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.status = tk.Label(master, text="Player 1's turn", font=("Arial", 14))
        self.status.pack()
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(15):
            self.canvas.create_line(40 * i, 0, 40 * i, 600, fill="black")
            self.canvas.create_line(0, 40 * i, 600, 40 * i, fill="black")
        for x in range(15):
            for y in range(15):
                if self.game.board[x][y] == 1:
                    self.canvas.create_oval(40 * y + 5, 40 * x + 5, 40 * y + 35, 40 * x + 35, fill="black")
                elif self.game.board[x][y] == 2:
                    self.canvas.create_oval(40 * y + 5, 40 * x + 5, 40 * y + 35, 40 * x + 35, fill="white")
    def on_click(self, event):
        x, y = event.y // 40, event.x // 40
        if self.game.make_move(x, y):
            self.draw_board()
            if self.game.winner:
                self.update_status(f"Player {self.game.winner} wins!")
            else:
                self.update_status(f"Player {self.game.current_player}'s turn")
        else:
            self.update_status("Invalid move. Try again.")
    def update_status(self, message):
        self.status.config(text=message)