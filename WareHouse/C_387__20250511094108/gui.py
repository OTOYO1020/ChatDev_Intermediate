'''
Contains the GUI for the Gomoku game using tkinter.
'''
import tkinter as tk
from game import GomokuGame
class GomokuGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.status = tk.Label(master, text="Current Player: X")
        self.status.pack()
        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(15):
            self.canvas.create_line(i * 40, 0, i * 40, 600)
            self.canvas.create_line(0, i * 40, 600, i * 40)
        for x in range(15):
            for y in range(15):
                if self.game.board[x][y] is not None:
                    self.canvas.create_text(x * 40 + 20, y * 40 + 20, text=self.game.board[x][y], font=("Arial", 24))
    def on_click(self, event):
        if self.game.winner is not None:
            return
        x, y = event.y // 40, event.x // 40
        if 0 <= x < 15 and 0 <= y < 15:
            self.game.make_move(x, y)
            self.draw_board()
            if self.game.winner:
                self.update_status(f"Player {self.game.winner} wins!")
            else:
                self.update_status(f"Current Player: {self.game.current_player}")
    def update_status(self, message):
        self.status.config(text=message)
    def reset_game(self):
        self.game.reset_game()
        self.draw_board()
        self.update_status("Current Player: X")