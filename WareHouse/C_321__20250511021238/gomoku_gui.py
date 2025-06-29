'''
This module contains the GomokuGUI class which handles the GUI components
and user interactions for the Gomoku game.
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
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)
    def draw_board(self):
        for i in range(15):
            for j in range(15):
                x1, y1 = j * 40, i * 40
                x2, y2 = x1 + 40, y1 + 40
                self.buttons[i][j] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                self.canvas.create_line(x1, y1, x2, y1, fill="black")
                self.canvas.create_line(x1, y1, x1, y2, fill="black")
    def on_click(self, event):
        # Calculate the row and column based on the click position
        x, y = event.y // 40, event.x // 40
        # Check if the click is within the bounds of the board
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            self.status_label.config(text="Click is out of bounds! Choose a valid cell.")
            return
        if self.game.game_over:  # Check if the game is over
            self.status_label.config(text="Game over! Start a new game.")
            return
        if self.game.board[x][y] is not None:
            self.status_label.config(text="Cell already occupied! Choose another cell.")
            return
        result = self.game.make_move(x, y)
        # Update the visual representation of the board immediately after the move
        self.canvas.itemconfig(self.buttons[x][y], fill="black" if self.game.current_player == 'O' else "white")
        if result:
            self.status_label.config(text=result)
            return
        self.update_status()
    def update_status(self):
        self.status_label.config(text=f"Player {self.game.current_player}'s turn")