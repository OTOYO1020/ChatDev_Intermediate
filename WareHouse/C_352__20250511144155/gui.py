'''
Contains the GUI logic for the Gomoku game using tkinter.
'''
import tkinter as tk
from gomoku import GomokuGame
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.game = GomokuGame()
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        self.status_label = tk.Label(master, text="Player 1's turn")
        self.status_label.pack()
        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(15):
            self.canvas.create_line(40 * i, 0, 40 * i, 600)
            self.canvas.create_line(0, 40 * i, 600, 40 * i)
        for x in range(15):
            for y in range(15):
                if self.game.board[x][y] == 1:
                    self.canvas.create_oval(40 * y + 10, 40 * x + 10, 40 * y + 30, 40 * x + 30, fill="black")
                elif self.game.board[x][y] == 2:
                    self.canvas.create_oval(40 * y + 10, 40 * x + 10, 40 * y + 30, 40 * x + 30, fill="white")
    def on_click(self, event):
        if self.game.game_over:
            self.update_status("Game is over! Please reset to play again.")
            return  # Prevent further clicks if the game is over
        x = event.y // 40
        y = event.x // 40
        # Check if the click is within the bounds of the board
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            self.update_status("Click is out of bounds! Try again.")
            return  # Do not proceed if the click is out of bounds
        if self.game.board[x][y] != 0:
            self.update_status("Cell already occupied! Try again.")
            return  # Do not proceed with the move if the cell is occupied
        self.game.make_move(x, y)
        self.draw_board()
        if self.game.game_over:
            self.update_status(f"Player {3 - self.game.current_player} wins!")
        else:
            self.update_status(f"Player {self.game.current_player}'s turn")
    def update_status(self, message):
        self.status_label.config(text=message)
    def reset_game(self):
        self.game.reset_game()
        self.draw_board()
        self.update_status("Player 1's turn")