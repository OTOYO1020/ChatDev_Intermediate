'''
This file contains the Subtask class.
'''
import tkinter as tk
import random
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Welcome to Hit and Blow Game!")
        self.label.pack()
        self.remaining_lives = 7
        self.random_number = self.generate_random_number()
        self.previous_guesses = []
        self.create_widgets()
        self.pack()
    def create_widgets(self):
        self.guess_label = tk.Label(self, text="Enter a three-digit number:")
        self.guess_label.pack()
        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack()
        self.remaining_lives_label = tk.Label(self, text=f"Remaining Lives: {self.remaining_lives}")
        self.remaining_lives_label.pack()
    def generate_random_number(self):
        digits = random.sample(range(10), 3)
        return "".join(map(str, digits))
    def check_guess(self):
        guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)  # Clear the guess entry field
        if not guess.isdigit() or len(guess) != 3 or len(set(guess)) != 3:
            self.label.config(text="Invalid input! Please enter a three-digit number with different digits.")
            return
        self.previous_guesses.append(guess)
        hits, blows = self.calculate_hits_and_blows(guess)
        if hits == 3:
            self.end_game("Congratulations! You guessed the number correctly.")
            return  # Exit the method to prevent deducting remaining lives
        if self.remaining_lives == 0:
            self.end_game(f"Game Over! The number was {self.random_number}.")
        else:
            self.remaining_lives -= 1
            self.remaining_lives_label.config(text=f"Remaining Lives: {self.remaining_lives}")
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
    def end_game(self, message):
        self.label.config(text=message)
        self.guess_entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.remaining_lives_label.config(text="")
        self.submit_button.config(state=tk.DISABLED)