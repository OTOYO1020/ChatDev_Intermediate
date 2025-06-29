'''
This module contains the GomokuGUI class which handles the graphical user interface.
'''
import tkinter as tk
from gomoku import GomokuGame
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gomoku Game")
        self.game = GomokuGame()
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        self.status_label = tk.Label(master, text="Player X's turn")
        self.status_label.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_canvas_click)  # Bind click event
    def draw_board(self):
        self.canvas.delete("all")  # Clear the canvas
        for row in range(15):
            for col in range(15):
                self.canvas.create_rectangle(col * 40, row * 40, col * 40 + 40, row * 40 + 40, outline="gray")
                if self.game.board[row][col] == "X":
                    self.draw_stone(row, col, "black")  # Black for X
                elif self.game.board[row][col] == "O":
                    self.draw_stone(row, col, "white")  # White for O
    def on_canvas_click(self, event):
        col = event.x // 40
        row = event.y // 40
        if 0 <= col < 15 and 0 <= row < 15:  # Corrected the condition to check column first
            self.on_click(row, col)  # Call the existing on_click method
    def on_click(self, row, col):
        if self.game.winner:
            self.update_status("Game over. Player {} has already won.".format(self.game.winner))
            return
        if self.game.board[row][col] is not None:
            self.update_status("Invalid move. Cell already occupied.")
            return
        result = self.game.make_move(row, col)
        if result:
            self.update_status(result)
            self.disable_canvas()  # Disable canvas if the game is over
        else:
            self.update_status(f"Player {self.game.current_player}'s turn")
            self.draw_board()  # Redraw the board to reflect the new move
    def draw_stone(self, row, col, color):
        self.canvas.create_oval(col * 40, row * 40, col * 40 + 40, row * 40 + 40, fill=color)
    def update_status(self, message):
        self.status_label.config(text=message)
    def disable_canvas(self):
        self.canvas.unbind("<Button-1>")  # Disable click events on the canvas