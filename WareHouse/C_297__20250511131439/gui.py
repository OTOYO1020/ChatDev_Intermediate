'''
Contains the GUI for the Gomoku game.
'''
import tkinter as tk
from tkinter import messagebox
class GomokuGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        self.status = tk.Label(master, text="Current Player: X")
        self.status.pack()
        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(1, self.game.board_size):
            self.canvas.create_line(i * 40, 0, i * 40, 600)
            self.canvas.create_line(0, i * 40, 600, i * 40)
        for x in range(self.game.board_size):
            for y in range(self.game.board_size):
                if self.game.board[x][y] == 'X':
                    self.canvas.create_oval(y * 40 + 10, x * 40 + 10, y * 40 + 30, x * 40 + 30, fill='black')
                elif self.game.board[x][y] == 'O':
                    self.canvas.create_oval(y * 40 + 10, x * 40 + 10, y * 40 + 30, x * 40 + 30, fill='white')
    def on_click(self, event):
        x = event.y // 40
        y = event.x // 40
        if 0 <= x < self.game.board_size and 0 <= y < self.game.board_size:  # Check if the click is within bounds
            if not self.game.game_over:  # Check if the game is still ongoing
                if self.game.make_move(x, y):
                    self.draw_board()
                    if self.game.game_over:
                        self.update_status(f"Player {self.game.current_player} wins!")
            else:
                self.update_status("Game over! Please restart to play again.")
    def reset_game(self):
        if messagebox.askyesno("Reset Game", "Are you sure you want to reset the game?"):  # Confirmation dialog
            self.game.reset_game()
            self.draw_board()
            self.update_status("Current Player: X")
    def update_status(self, message):
        self.status.config(text=message)