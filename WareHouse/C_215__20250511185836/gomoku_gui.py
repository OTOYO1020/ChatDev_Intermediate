'''
This module contains the GUI for the Gomoku game.
'''
import tkinter as tk
from tkinter import messagebox
from gomoku_game import GomokuGame  # Import the GomokuGame class
class GomokuGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
        # Add a reset button
        reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        reset_button.pack()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(15):
            self.canvas.create_line(40 * i, 0, 40 * i, 600)
            self.canvas.create_line(0, 40 * i, 600, 40 * i)
        for x in range(15):
            for y in range(15):
                if self.game.board[x][y] == "X":
                    self.canvas.create_oval(40 * y + 5, 40 * x + 5, 40 * y + 35, 40 * x + 35, fill="black")
                elif self.game.board[x][y] == "O":
                    self.canvas.create_oval(40 * y + 5, 40 * x + 5, 40 * y + 35, 40 * x + 35, fill="white")
    def on_click(self, event):
        x = event.y // 40
        y = event.x // 40
        if self.game.winner:
            messagebox.showinfo("Game Over", "The game is already over. Please reset to play again.")
            return  # Prevent moves after the game is over
        if not (0 <= x < 15 and 0 <= y < 15):
            messagebox.showwarning("Invalid Move", "Click outside the board is not allowed. Please choose a valid cell.")
            return  # Prevent moves outside the board
        if self.game.board[x][y] is not None:
            messagebox.showwarning("Invalid Move", "This cell is already occupied. Please choose another.")
            return  # Prevent moves on occupied cells
        self.game.make_move(x, y)
        self.draw_board()
        if self.game.winner:
            messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
            self.reset_game()  # Reset the game after showing the message
    def reset_game(self):
        self.game.reset_game()
        self.draw_board()