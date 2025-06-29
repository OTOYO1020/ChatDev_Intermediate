'''
This module contains the GUI logic for the Gomoku game using tkinter.
'''
import tkinter as tk
from gomoku import GomokuGame
class GomokuGUI:
    def __init__(self):
        self.game = GomokuGame()
        self.window = tk.Tk()
        self.window.title("Gomoku Game")
        self.canvas = tk.Canvas(self.window, width=600, height=600)
        self.canvas.pack()
        self.status_label = tk.Label(self.window, text="Current Player: X")
        self.status_label.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
    def draw_board(self):
        '''
        Draws the Gomoku board on the canvas.
        '''
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
        '''
        Handles mouse click events on the canvas to make a move in the game.
        '''
        col = event.x // 40
        row = event.y // 40
        # Check if the clicked position is within the valid range
        if row < 0 or row >= 15 or col < 0 or col >= 15:
            self.update_status("Invalid move! Click within the board.")
            return
        if self.game.winner:
            self.update_status(f"Game over! Player {self.game.winner} has already won.")
            return
        if self.game.board[row][col] != ' ':
            self.update_status("Invalid move! Cell already occupied.")
            return
        self.game.make_move(row, col)
        self.draw_board()
        if self.game.winner:
            self.update_status(f"Player {self.game.winner} wins!")
        else:
            self.update_status(f"Current Player: {self.game.current_player}")
    def update_status(self, message):
        '''
        Updates the status label with the provided message.
        '''
        self.status_label.config(text=message)
    def run(self):
        '''
        Starts the GUI main loop.
        '''
        self.window.mainloop()