'''
Contains the GUI for the Gomoku game using tkinter.
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
        self.canvas.bind("<Button-1>", self.on_click)
        # Add Reset Button
        self.reset_button = tk.Button(self.window, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()
        self.draw_board()
    def reset_game(self):
        self.game.reset_game()
        self.draw_board()  # Redraw the board after resetting
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(15):
            self.canvas.create_line(40 * i, 0, 40 * i, 600)
            self.canvas.create_line(0, 40 * i, 600, 40 * i)
        for x in range(15):
            for y in range(15):
                if self.game.board[x][y] == "X":
                    self.canvas.create_text(20 + 40 * x, 20 + 40 * y, text="X", font=("Arial", 24))
                elif self.game.board[x][y] == "O":
                    self.canvas.create_text(20 + 40 * x, 20 + 40 * y, text="O", font=("Arial", 24))
    def on_click(self, event):
        x, y = event.x // 40, event.y // 40
        result = self.game.make_move(x, y)
        if result:
            self.update_display(result)
        self.draw_board()
    def update_display(self, message):
        result_window = tk.Toplevel(self.window)
        result_window.title("Game Over")
        label = tk.Label(result_window, text=message)
        label.pack()
        button = tk.Button(result_window, text="OK", command=lambda: [result_window.destroy(), self.reset_game()])
        button.pack()
    def run(self):
        self.window.mainloop()