'''
Contains the GUI implementation for the Gomoku game using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from gomoku_game import GomokuGame
class GomokuGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Gomoku Game")
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()
        self.status_label = tk.Label(self.root, text="Current Player: X")
        self.status_label.pack()
        self.new_game_button = tk.Button(self.root, text="New Game", command=self.new_game)
        self.new_game_button.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(15):
            self.canvas.create_line(i * 40, 0, i * 40, 600, fill="black")
            self.canvas.create_line(0, i * 40, 600, i * 40, fill="black")
        for x in range(15):
            for y in range(15):
                if self.game.board[x][y] == "X":
                    self.canvas.create_oval(x * 40 + 5, y * 40 + 5, x * 40 + 35, y * 40 + 35, fill="black")
                elif self.game.board[x][y] == "O":
                    self.canvas.create_oval(x * 40 + 5, y * 40 + 5, x * 40 + 35, y * 40 + 35, fill="white")
    def on_click(self, event):
        x = event.x // 40
        y = event.y // 40
        if self.game.make_move(x, y):
            self.draw_board()
            if self.game.winner:
                messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
                self.game.reset_game()
                self.draw_board()
                self.update_status("Current Player: X")  # Update status after reset
            else:
                self.update_status(f"Current Player: {self.game.current_player}")
        else:
            messagebox.showwarning("Invalid Move", "The cell is already occupied. Please choose another cell.")
    def update_status(self, message):
        self.status_label.config(text=message)
    def new_game(self):
        self.game.reset_game()
        self.draw_board()
        self.update_status("Current Player: X")  # Reset status for new game
    def run(self):
        self.root.mainloop()