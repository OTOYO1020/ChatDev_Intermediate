'''
Contains the GUI logic for Gomoku.
'''
import tkinter as tk
from tkinter import messagebox
class GomokuGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
        self.status = tk.Label(master, text="Player X's turn")
        self.status.pack()
    def draw_board(self):
        for i in range(15):
            self.canvas.create_line(i * 40, 0, i * 40, 600)
            self.canvas.create_line(0, i * 40, 600, i * 40)
    def on_click(self, event):
        x, y = event.y // 40, event.x // 40
        if self.game.board[x][y] is not None:
            messagebox.showwarning("Invalid Move", "This cell is already occupied!")
            return
        result = self.game.make_move(x, y)
        if result:
            self.update_status(result)
        self.draw_board()
        self.draw_pieces()
    def draw_pieces(self):
        for x in range(15):
            for y in range(15):
                if self.game.board[x][y] == "X":
                    self.canvas.create_oval(y * 40 + 5, x * 40 + 5, y * 40 + 35, x * 40 + 35, fill="black")
                elif self.game.board[x][y] == "O":
                    self.canvas.create_oval(y * 40 + 5, x * 40 + 5, y * 40 + 35, x * 40 + 35, fill="white")
    def update_status(self, message):
        messagebox.showinfo("Game Over", message)
        self.game.reset_game()
        self.status.config(text="Player X's turn")
        self.canvas.delete("all")
        self.draw_board()