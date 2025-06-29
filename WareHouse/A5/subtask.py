'''
This file contains the Subtask class which represents the graphical user interface for the subtask details.
'''
import tkinter as tk
import random
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Hit and Blow Game")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Submit", command=self.start_game)
        self.button.pack()
        self.remaining_lives = 7
        self.generated_number = self.generate_number()
        self.hits = 0
        self.blows = 0
    def generate_number(self):
        """
        Generate a random three-digit number with different digits.
        """
        digits = list(range(1, 10))  # Exclude 0 from the list of digits
        random.shuffle(digits)
        return ''.join(map(str, digits[:3]))
    def validate_input(self, guess):
        """
        Validate the user's input to ensure it is a three-digit number with different digits.
        """
        if len(guess) != 3 or not guess.isdigit():
            return False
        if guess[0] == guess[1] or guess[0] == guess[2] or guess[1] == guess[2]:
            return False
        return True
    def check_hits_and_blows(self, guess):
        """
        Compare the user's guess with the generated number to determine the hits and blows.
        """
        self.hits = 0
        self.blows = 0
        generated_digits = list(self.generated_number)
        for i in range(3):
            if guess[i] == generated_digits[i]:
                self.hits += 1
            elif guess[i] in generated_digits:
                self.blows += 1
    def update_game_state(self, guess):
        """
        Update the game state based on the user's guess.
        """
        if guess == self.generated_number:
            self.label.config(text="Congratulations! You guessed the number.")
            self.button.config(state=tk.DISABLED)
        else:
            self.remaining_lives -= 1
            if self.remaining_lives == 0:
                self.label.config(text=f"Game Over! The number was {self.generated_number}.")
                self.button.config(state=tk.DISABLED)
            else:
                self.label.config(text=f"Hits: {self.hits}, Blows: {self.blows}, Lives: {self.remaining_lives}")
    def start_game(self):
        """
        Start the hit and blow game.
        """
        guess = self.entry.get()
        if not self.validate_input(guess):
            self.label.config(text="Invalid input. Please enter a three-digit number with different digits.")
            return
        self.check_hits_and_blows(guess)
        self.update_game_state(guess)
        if self.hits == 3 or self.remaining_lives == 0:
            self.button.config(state=tk.DISABLED)
        self.entry.delete(0, tk.END)