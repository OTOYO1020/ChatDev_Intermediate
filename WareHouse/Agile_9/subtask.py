'''
This file contains the Subtask class.
'''
import tkinter as tk
import random
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.remaining_lives = 7
        self.generated_number = self.generate_random_number()
        self.is_game_over = False
    def create_widgets(self):
        self.label = tk.Label(self, text="Default subtask details")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Submit", command=self.button_click)
        self.button.pack()
    def generate_random_number(self):
        digits = random.sample(range(10), 3)
        return "".join(map(str, digits))
    def check_guess(self, guess):
        hits = 0
        blows = 0
        for i in range(3):
            if guess[i] == self.generated_number[i]:
                hits += 1
            elif guess[i] in self.generated_number:
                blows += 1
        return hits, blows
    def validate_input(self, guess):
        if len(guess) != 3 or not guess.isdigit():
            return False
        if guess[0] == guess[1] or guess[1] == guess[2] or guess[0] == guess[2]:
            return False
        return True
    def update_remaining_lives(self):
        if self.is_game_over:
            return
        self.remaining_lives -= 1
        if self.remaining_lives == 0:
            self.label.config(text="Game Over! The number was " + self.generated_number)
            self.is_game_over = True
    def end_game(self):
        self.label.config(text="Congratulations! You guessed the number " + self.generated_number)
        self.is_game_over = True
    def button_click(self):
        if self.is_game_over:
            return
        guess = self.entry.get()
        self.entry.delete(0, tk.END)
        if not self.validate_input(guess):
            self.label.config(text="Invalid input. Please enter a three-digit number with different digits.")
            return
        if guess == self.generated_number:
            self.end_game()
            return
        hits, blows = self.check_guess(guess)
        if hits == 3 or (hits < 3 and self.remaining_lives > 3):
            self.end_game()
            return
        self.update_remaining_lives()
        if self.is_game_over:
            return
        self.label.config(text=f"Hits: {hits}, Blows: {blows}, Remaining Lives: {self.remaining_lives}")