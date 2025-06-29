import tkinter as tk
import random
class HitAndBlowGame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.attempts = 0
        self.remaining_lives = 7
        self.target_number = self.generate_target_number()
        self.create_widgets()
    def generate_target_number(self):
        digits = list(range(10))
        random.shuffle(digits)
        return ''.join(map(str, digits[:3]))
    def create_widgets(self):
        self.label = tk.Label(self, text="Enter a three-digit number:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Submit", command=self.check_guess)
        self.button.pack()
        self.remaining_lives_label = tk.Label(self, text=f"Remaining Lives: {self.remaining_lives}")
        self.remaining_lives_label.pack()
    def check_guess(self):
        guess = self.entry.get()
        if not self.validate_input(guess):
            self.label.config(text="Invalid input. Please enter a three-digit number.")
            return
        self.attempts += 1
        hits, blows = self.calculate_hits_and_blows(guess)
        if hits == 3:
            self.label.config(text="Congratulations! You guessed the number correctly.")
            self.button.config(state=tk.DISABLED)
            return  # End the game if the user guessed correctly
        self.label.config(text=f"Hits: {hits}, Blows: {blows}")
        self.remaining_lives -= 1
        self.remaining_lives_label.config(text=f"Remaining Lives: {self.remaining_lives}")
        if self.remaining_lives == 0:
            self.label.config(text=f"Game Over. The target number was {self.target_number}.")
            self.button.config(state=tk.DISABLED)
    def validate_input(self, guess):
        if len(guess) != 3 or not guess.isdigit():
            return False
        if len(set(guess)) != 3:
            return False
        return True
    def calculate_hits_and_blows(self, guess):
        hits = 0
        blows = 0
        for i in range(3):
            if guess[i] == self.target_number[i]:
                hits += 1
            elif guess[i] in self.target_number:
                blows += 1
        return hits, blows