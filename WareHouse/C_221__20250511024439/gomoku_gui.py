'''
This module contains the GomokuGUI class which handles the graphical interface.
'''
import tkinter as tk  # Import tkinter for GUI components
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
        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(15):
            self.canvas.create_line(i * 40, 0, i * 40, 600)
            self.canvas.create_line(0, i * 40, 600, i * 40)
        for x in range(15):
            for y in range(15):
                if self.game.board[x][y] == 'X':
                    self.canvas.create_oval(x * 40 + 5, y * 40 + 5, x * 40 + 35, y * 40 + 35, fill='black')
                elif self.game.board[x][y] == 'O':
                    self.canvas.create_oval(x * 40 + 5, y * 40 + 5, x * 40 + 35, y * 40 + 35, fill='white')
    def on_click(self, event):
        if self.game.game_over:
            self.update_status("Game over! Please reset to play again.")  # Inform the user
            return  # Exit early if the game is over
        x, y = event.x // 40, event.y // 40
        if not (0 <= x < 15 and 0 <= y < 15):  # Check if the click is within the board limits
            self.update_status("Invalid move! Click within the board.")  # Inform the user
            return  # Exit early if the click is outside the board
        if self.game.board[x][y] is not None:
            self.update_status("Invalid move! Cell already occupied.")  # Inform the user
            return  # Exit early if the cell is already occupied
        result = self.game.make_move(x, y)
        self.draw_board()
        self.update_status(result)
    def update_status(self, message):
        self.status_label.config(text=message)
    def reset_game(self):
        self.game.reset_game()  # Reset the game logic
        self.draw_board()  # Redraw the board
        self.update_status("Player X's turn")  # Reset the status message