'''
Contains the GUI for the Gomoku game.
'''
import tkinter as tk
from gomoku_game import GomokuGame
class GomokuGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.status_label = tk.Label(master, text="Current Player: X")
        self.status_label.pack()
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(15):
            self.canvas.create_line(40 * i, 0, 40 * i, 600)
            self.canvas.create_line(0, 40 * i, 600, 40 * i)
        for x in range(15):
            for y in range(15):
                if self.game.board[x][y] == "X":
                    self.canvas.create_oval(40 * y + 10, 40 * x + 10, 40 * y + 30, 40 * x + 30, fill="black")
                elif self.game.board[x][y] == "O":
                    self.canvas.create_oval(40 * y + 10, 40 * x + 10, 40 * y + 30, 40 * x + 30, fill="white")
    def on_click(self, event):
        if self.game.winner is not None:  # Prevent further moves if the game is over
            return
        x, y = event.y // 40, event.x // 40
        if 0 <= x < 15 and 0 <= y < 15:  # Ensure the click is within bounds
            if self.game.board[x][y] is not None:  # Check if the cell is already occupied
                self.update_status("Invalid move! Cell already occupied.")
                return
            if self.game.make_move(x, y):
                self.draw_board()
                if self.game.winner:
                    self.update_status(f"Player {self.game.winner} wins!" if self.game.winner != "Draw" else "It's a Draw!")
                else:
                    self.update_status(f"Current Player: {self.game.current_player}")
                    # Switch players after a successful move
                    self.game.current_player = "O" if self.game.current_player == "X" else "X"
    def update_status(self, message):
        self.status_label.config(text=message)