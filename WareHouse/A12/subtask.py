'''
This file contains the Subtask class.
'''
import tkinter as tk
from main import Game
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.game = Game()
        self.label = tk.Label(self, text=f"Remaining Lives: {self.game.remaining_lives}")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Guess", command=self.handle_guess)
        self.button.pack()
    def handle_guess(self):
        """
        Handle the user's guess and update the game accordingly.
        """
        if self.game.game_over:
            return
        guess = self.entry.get()
        if len(guess) != 3 or not guess.isdigit():
            self.label.config(text="Invalid input. Please enter a three-digit number.")
            return
        if len(set(guess)) != 3:
            self.label.config(text="Invalid input. Please enter a number with different digits.")
            return
        hits, blows = self.game.check_guess(int(guess))
        if hits == 3:
            self.game.end_game(hits)
            self.label.config(text="Congratulations! You have won the game.")
            return
        self.game.remaining_lives -= 1
        self.label.config(text=f"Hits: {hits}, Blows: {blows}, Remaining Lives: {self.game.remaining_lives}")
        if self.game.remaining_lives == 0:
            self.game.end_game(hits)
            self.label.config(text="Game Over. You have run out of lives.")
            self.entry.config(state=tk.DISABLED)
            self.button.config(state=tk.DISABLED)
        elif self.game.remaining_lives == 4:
            self.game.end_game(hits)
            self.label.config(text="Congratulations! You have won the game.")
        self.entry.delete(0, tk.END)