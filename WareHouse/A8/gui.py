'''
This file contains the GUI-related classes and functions.
'''
import tkinter as tk
from data import GameData
from utils import format_output
class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.game_data = GameData()
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self, text="Enter a three-digit number:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Guess", command=self.check_guess)
        self.button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
        self.remaining_lives_label = tk.Label(self, text=f"Remaining lives: {self.game_data.remaining_lives}")
        self.remaining_lives_label.pack()
    def check_guess(self):
        guess = self.entry.get()
        if not self.validate_input(guess):
            self.result_label.config(text="Invalid input. Enter a three-digit number.")
            return
        hits, blows = self.game_data.check_guess(guess)
        self.result_label.config(text=format_output((hits, blows)))
        self.remaining_lives_label.config(text=f"Remaining lives: {self.game_data.remaining_lives}")
        if self.game_data.is_game_over():
            self.button.config(state=tk.DISABLED)
            if self.game_data.is_game_won():
                self.result_label.config(text="Congratulations! You guessed the number.")
            else:
                self.result_label.config(text=f"Game over. The number was {self.game_data.generated_number}.")
    def validate_input(self, user_input):
        if len(user_input) != 3 or not user_input.isdigit():
            return False
        digits = set(user_input)
        if len(digits) != 3 or len(user_input) != len(digits):
            return False
        return True