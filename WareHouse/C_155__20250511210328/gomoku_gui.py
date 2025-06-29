'''
This module contains the GomokuGUI class which handles the graphical user interface.
'''
from gomoku import GomokuGame
import tkinter as tk
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gomoku Game")
        self.game = GomokuGame()
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
            self.canvas.create_line(40 * i, 0, 40 * i, 600)
            self.canvas.create_line(0, 40 * i, 600, 40 * i)
        for x in range(self.game.board_size):
            for y in range(self.game.board_size):
                if self.game.board[x][y] == 'X':
                    self.canvas.create_oval(40 * y + 10, 40 * x + 10, 40 * y + 30, 40 * x + 30, fill='black')
                elif self.game.board[x][y] == 'O':
                    self.canvas.create_oval(40 * y + 10, 40 * x + 10, 40 * y + 30, 40 * x + 30, fill='white')
    def on_click(self, event):
        x = event.y // 40
        y = event.x // 40
        # Validate the coordinates
        if self.game.winner:
            self.update_status(f"Player {self.game.winner} has already won! Reset to play again.")
            return
        if 0 <= x < self.game.board_size and 0 <= y < self.game.board_size:
            if self.game.make_move(x, y):
                self.draw_board()
                if self.game.winner:
                    self.update_status(f"Player {self.game.winner} wins!")
                else:
                    self.update_status(f"Current Player: {self.game.current_player}")
            else:
                self.update_status("Invalid move! Cell already occupied.")
        else:
            self.update_status("Invalid move! Click was outside the board.")
    def update_status(self, message):
        self.status.config(text=message)
    def reset_game(self):
        self.game.reset_game()
        self.draw_board()
        self.update_status("Current Player: X")