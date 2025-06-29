'''
This module contains the GomokuGUI class which manages the graphical interface for the Gomoku game.
'''
from gomoku_game import GomokuGame
import tkinter as tk
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.game = GomokuGame()
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.status_label = tk.Label(master, text="Current Player: X")
        self.status_label.pack()
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(15):
            self.canvas.create_line(40 * i, 0, 40 * i, 600)
            self.canvas.create_line(0, 40 * i, 600, 40 * i)
        for row in range(15):
            for col in range(15):
                if self.game.board[row][col] == 'X':
                    self.canvas.create_oval(col * 40 + 10, row * 40 + 10, col * 40 + 30, row * 40 + 30, fill='black')
                elif self.game.board[row][col] == 'O':
                    self.canvas.create_oval(col * 40 + 10, row * 40 + 10, col * 40 + 30, row * 40 + 30, fill='white')
    def on_click(self, event):
        col = event.x // 40
        row = event.y // 40
        if 0 <= row < 15 and 0 <= col < 15:  # Check for valid move
            try:
                if self.game.board[row][col] == ' ':
                    self.game.make_move(row, col)
                    self.draw_board()
                    if self.game.winner:
                        self.update_status(f"Player {self.game.winner} wins!")
                    elif self.game.is_full():
                        self.update_status("The game is a draw!")
                    else:
                        self.update_status(f"Current Player: {self.game.current_player}")
                else:
                    self.update_status("Invalid move! Cell already occupied.")
            except ValueError as e:
                self.update_status(str(e))  # Display the error message for out of bounds
    def update_status(self, message):
        self.status_label.config(text=message)