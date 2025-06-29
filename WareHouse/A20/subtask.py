'''
This file contains the HitAndBlowGame class.
'''
import tkinter as tk
import random
class HitAndBlowGame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.generated_number = self.generate_number()
        self.remaining_lives = 7
        self.hits = 0
        self.blows = 0
        self.label = tk.Label(self, text="Welcome to Hit and Blow Game!")
        self.label.pack()
        self.remaining_lives_label = tk.Label(self, text=f"Remaining Lives: {self.remaining_lives}")
        self.remaining_lives_label.pack()
        self.input_label = tk.Label(self, text="Enter a three-digit number:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self)
        self.input_entry.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack()
    def generate_number(self):
        digits = random.sample(range(1, 10), 3)
        return "".join(str(digit) for digit in digits)
    def check_guess(self):
        guess = self.input_entry.get()
        if not guess.isdigit() or len(guess) != 3 or len(set(guess)) != 3:
            self.label.config(text="Invalid input. Please enter a three-digit number with different digits.")
            return
        if guess == self.generated_number:
            self.label.config(text="Congratulations! You guessed the number correctly.")
            self.submit_button.config(state=tk.DISABLED)
            return
        self.remaining_lives -= 1
        self.remaining_lives_label.config(text=f"Remaining Lives: {self.remaining_lives}")
        self.hits = sum(1 for x, y in zip(guess, self.generated_number) if x == y)
        self.blows = sum(1 for x in guess if x in self.generated_number and x != self.generated_number[guess.index(x)])
        self.label.config(text=f"Hits: {self.hits}, Blows: {self.blows}")
        if self.hits == 3:
            self.label.config(text="Congratulations! You guessed the number correctly.")
            self.submit_button.config(state=tk.DISABLED)
            return
        if self.remaining_lives == 0:
            self.label.config(text=f"Game over. The number was {self.generated_number}.")
            self.submit_button.config(state=tk.DISABLED)