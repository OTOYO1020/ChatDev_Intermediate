'''
This is the subtask file for the hit and blow game.
'''
import random
import tkinter as tk
class Subtask:
    def __init__(self, application):
        self.application = application
        self.target_number = self.generate_target_number()
        self.remaining_lives = 7
        self.label = tk.Label(self.application, text="Enter a three-digit number:")
        self.label.pack()
        self.entry = tk.Entry(self.application)
        self.entry.pack()
        self.button = tk.Button(self.application, text="Submit", command=self.check_guess)
        self.button.pack()
        self.result_label = tk.Label(self.application, text="")
        self.result_label.pack()
    def generate_target_number(self):
        target_number = random.sample(range(1, 10), 3)
        return [int(digit) for digit in target_number]
    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit() or len(guess) != 3:
            self.result_label.config(text="Invalid input. Please enter a three-digit number.")
            return
        guess = [int(digit) for digit in guess]
        hits = 0
        blows = 0
        for i in range(3):
            if guess[i] == self.target_number[i]:
                hits += 1
            elif guess[i] in self.target_number and guess[i] != self.target_number[i]:
                blows += 1
        if hits == 3:
            self.result_label.config(text="Congratulations! You guessed the number correctly.")
            self.button.config(state=tk.DISABLED)
        else:
            self.remaining_lives -= 1
            self.result_label.config(text=f"Hits: {hits}, Blows: {blows}, Remaining Lives: {self.remaining_lives}")
            if self.remaining_lives == 0:
                self.result_label.config(text=f"Game Over. The correct number was {self.target_number}.")
                self.button.config(state=tk.DISABLED)