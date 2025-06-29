'''
This file contains the Subtask class.
'''
import tkinter as tk
import random
class Subtask(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.label = tk.Label(self, text="Welcome to Hit and Blow Game!")
        self.label.pack()
        self.remaining_lives = 7
        self.generated_number = self.generate_number()
        self.create_input_field()
        self.create_submit_button()
        self.create_remaining_lives_label()
    def generate_number(self):
        digits = random.sample(range(1, 10), 3)
        return "".join(map(str, digits))
    def create_input_field(self):
        self.input_field = tk.Entry(self)
        self.input_field.pack()
    def create_submit_button(self):
        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack()
    def create_remaining_lives_label(self):
        self.remaining_lives_label = tk.Label(self, text=f"Remaining Lives: {self.remaining_lives}")
        self.remaining_lives_label.pack()
    def check_guess(self):
        guess = self.input_field.get()
        if not guess.isdigit() or len(guess) != 3 or len(set(guess)) != 3:
            self.label.config(text="Invalid input. Please enter a valid three-digit number with different digits.")
            return
        hits, blows = self.calculate_hits_and_blows(guess)
        self.label.config(text=f"Hits: {hits}, Blows: {blows}")
        if hits == 3:
            self.end_game(True)
        else:
            self.remaining_lives -= 1
            self.remaining_lives_label.config(text=f"Remaining Lives: {self.remaining_lives}")
            if self.remaining_lives == 0:
                self.end_game(False)
    def calculate_hits_and_blows(self, guess):
        hits = 0
        blows = 0
        matched_positions = []
        for i in range(3):
            if guess[i] == self.generated_number[i]:
                hits += 1
                matched_positions.append(i)
        for i in range(3):
            if i not in matched_positions and guess[i] in self.generated_number:
                blows += 1
        return hits, blows
    def end_game(self, is_winner):
        self.submit_button.config(state=tk.DISABLED)
        if is_winner:
            self.label.config(text="Congratulations! You guessed the number correctly.")
        else:
            self.label.config(text=f"Game over. The number was {self.generated_number}.")