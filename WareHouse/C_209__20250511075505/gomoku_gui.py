'''
This module contains the GUI for the Gomoku game using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from gomoku_game import GomokuGame  # Importing the GomokuGame class
class GomokuGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Gomoku Game")
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()
        self.status_label = tk.Label(self.root, text="Current Player: X")
        self.status_label.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(self.game.board_size):
            self.canvas.create_line(i * 40, 0, i * 40, 600, fill="black")
            self.canvas.create_line(0, i * 40, 600, i * 40, fill="black")
        for x in range(self.game.board_size):
            for y in range(self.game.board_size):
                if self.game.board[x][y] == 'X':
                    self.canvas.create_oval(y * 40 + 10, x * 40 + 10, y * 40 + 30, x * 40 + 30, fill="black")
                elif self.game.board[x][y] == 'O':
                    self.canvas.create_oval(y * 40 + 10, x * 40 + 10, y * 40 + 30, x * 40 + 30, fill="white")
    def on_click(self, event):
        x = event.y // 40
        y = event.x // 40
        try:
            self.game.make_move(x, y)
            self.draw_board()
            if self.game.winner:
                messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
                self.game.reset_game()
                self.draw_board()
            else:
                self.update_status(f"Current Player: {self.game.current_player}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def update_status(self, message):
        self.status_label.config(text=message)
    def run(self):
        self.root.mainloop()