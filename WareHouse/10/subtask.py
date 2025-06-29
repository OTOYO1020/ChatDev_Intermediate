'''
This file contains the Subtask class.
'''
import tkinter as tk
import random
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Default subtask details")
        self.label.pack()
        self.remaining_lives = 7
        self.generated_number = self.generate_number()
        self.game_over = False  # New variable to track game over
        self.create_widgets()
    def generate_number(self):
        digits = random.sample(range(1, 10), 3)
        return int("".join(str(digit) for digit in digits))
    def create_widgets(self):
        self.remaining_lives_label = tk.Label(self, text=f"Remaining Lives: {self.remaining_lives}")
        self.remaining_lives_label.pack()
        self.input_label = tk.Label(self, text="Enter a three-digit number:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self)
        self.input_entry.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.check_number)
        self.submit_button.pack()
    def check_number(self):
        if self.game_over:  # Check if game is already over
            return
        user_input = self.input_entry.get()
        if not user_input.isdigit() or len(user_input) != 3:
            self.label.config(text="Invalid input. Please enter a three-digit number.")
            return
        user_digits = [int(digit) for digit in user_input]
        if len(set(user_digits)) != 3:
            self.label.config(text="Invalid input. Please enter a number with unique digits.")
            return
        user_number = int(user_input)
        hits, blows = self.calculate_hits_and_blows(user_number)
        if user_number == self.generated_number and self.remaining_lives > 0:
            self.label.config(text="Congratulations! You guessed the number correctly. You won the game!")
            self.submit_button.config(state=tk.DISABLED)
            self.game_over = True  # Set game over to True
        else:
            if self.remaining_lives == 1:
                self.label.config(text=f"Game Over. The correct number was {self.generated_number}.")
                self.submit_button.config(state=tk.DISABLED)
                self.game_over = True  # Set game over to True
            else:
                self.remaining_lives -= 1
                self.remaining_lives_label.config(text=f"Remaining Lives: {self.remaining_lives}")
                self.label.config(text=f"Hits: {hits}, Blows: {blows}")
    def calculate_hits_and_blows(self, user_number):
        generated_digits = [int(digit) for digit in str(self.generated_number)]
        user_digits = [int(digit) for digit in str(user_number)]
        hits = sum(generated_digit == user_digit for generated_digit, user_digit in zip(generated_digits, user_digits))
        blows = sum(generated_digit in user_digits and generated_digit != user_digit for generated_digit in generated_digits)
        return hits, blows