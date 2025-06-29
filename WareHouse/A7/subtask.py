'''
This file contains the Subtask class.
'''
import tkinter as tk
from random import sample
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Enter a three-digit number:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Guess", command=self.handle_guess)
        self.button.pack()
        self.remaining_lives = 7
        self.generated_number = self.generate_number()
        self.game_over = False
    def generate_number(self):
        digits = sample(range(1, 10), 3)
        return "".join(str(d) for d in digits)
    def handle_guess(self):
        if self.game_over:
            return
        guess = self.entry.get()
        if not guess.isdigit() or len(guess) != 3:
            self.label.config(text="Invalid input. Enter a three-digit number.")
            return
        if len(set(guess)) != 3 or len(guess) != len(set(guess)):
            self.label.config(text="Invalid input. Digits must be different.")
            return
        hits = 0
        blows = 0
        for i, digit in enumerate(guess):
            if digit == self.generated_number[i]:
                hits += 1
            elif digit in self.generated_number:
                blows += 1
        if hits == 3:
            self.label.config(text="Congratulations! You guessed the number.")
            self.game_over = True
        else:
            self.remaining_lives -= 1
            if self.remaining_lives == 0:
                self.label.config(text=f"Game over. The number was {self.generated_number}.")
                self.game_over = True
            else:
                self.label.config(text=f"Hits: {hits}, Blows: {blows}, Lives: {self.remaining_lives}")
                if hits == 2 and self.remaining_lives == 3:
                    self.label.config(text="Congratulations! You guessed the number halfway through.")
                    self.game_over = True