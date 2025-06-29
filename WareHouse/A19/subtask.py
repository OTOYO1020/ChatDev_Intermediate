'''
This file contains the Subtask class.
'''
import tkinter as tk
import random
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.random_number = self.generate_random_number()
        self.remaining_lives = 7
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
    def generate_random_number(self):
        digits = random.sample(range(0, 10), 3)
        return "".join(str(digit) for digit in digits)
    def check_guess(self):
        guess = self.input_entry.get()
        if not guess.isdigit() or len(guess) != 3:
            self.label.config(text="Invalid input. Please enter a three-digit number.")
            return
        if len(set(guess)) != 3:
            self.label.config(text="Invalid input. Please enter a three-digit number with different digits.")
            return
        if guess == self.random_number:
            self.label.config(text="Congratulations! You guessed the number correctly.")
            self.submit_button.config(state=tk.DISABLED)
            return
        self.remaining_lives -= 1
        self.remaining_lives_label.config(text=f"Remaining Lives: {self.remaining_lives}")
        if self.remaining_lives == 0:
            self.label.config(text=f"Game Over. The number was {self.random_number}.")
            self.submit_button.config(state=tk.DISABLED)
        elif self.remaining_lives == 7 // 2 and guess == self.random_number:
            self.label.config(text="Congratulations! You guessed the number correctly.")
            self.submit_button.config(state=tk.DISABLED)
        else:
            hits, blows = self.calculate_hits_and_blows(guess)
            self.label.config(text=f"Hits: {hits}, Blows: {blows}")
    def calculate_hits_and_blows(self, guess):
        hits = 0
        blows = 0
        for i in range(3):
            if guess[i] == self.random_number[i]:
                hits += 1
            elif guess[i] in self.random_number:
                blows += 1
        return hits, blows