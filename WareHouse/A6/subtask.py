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
        self.start_game()
    def start_game(self):
        self.secret_number = self.generate_secret_number()
        self.remaining_lives = 7
        self.label.config(text=f"Remaining Lives: {self.remaining_lives}")
        self.input_entry = tk.Entry(self)
        self.input_entry.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.check_input)
        self.submit_button.pack()
    def generate_secret_number(self):
        digits = list(range(1, 10))
        random.shuffle(digits)
        return ''.join(map(str, digits[:3]))
    def check_input(self):
        user_input = self.input_entry.get()
        if not user_input.isdigit() or len(user_input) != 3:
            self.label.config(text="Invalid input. Please enter a three-digit number.")
            return
        user_digits = [int(digit) for digit in user_input]
        if len(set(user_digits)) != 3:
            self.label.config(text="Invalid input. Please enter a number with different digits.")
            return
        hits, blows = self.calculate_hits_and_blows(user_digits)
        if hits == 3 or self.remaining_lives == 0 or self.remaining_lives == 7 // 2:
            self.end_game()
        else:
            self.remaining_lives -= 1
            self.label.config(text=f"Hits: {hits}, Blows: {blows}, Remaining Lives: {self.remaining_lives}")
    def calculate_hits_and_blows(self, user_digits):
        hits = 0
        blows = 0
        secret_digits = list(map(int, self.secret_number))
        for i in range(3):
            if user_digits[i] == secret_digits[i]:
                hits += 1
            elif user_digits[i] in secret_digits and user_digits[i] != secret_digits[i]:
                blows += 1
        return hits, blows
    def end_game(self):
        if self.remaining_lives == 0:
            self.label.config(text=f"Game over. The secret number was {self.secret_number}")
        elif self.remaining_lives == 7 // 2:
            self.label.config(text="Congratulations! You guessed the secret number halfway through.")
        else:
            self.label.config(text="Congratulations! You guessed the secret number.")
        self.input_entry.config(state="disabled")
        self.submit_button.config(state="disabled")