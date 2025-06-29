'''
This file contains the Subtask class.
'''
import tkinter as tk
import random
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.attempts = 0
        self.max_attempts = 7
        self.target_number = self.generate_target_number()
        self.create_widgets()
    def generate_target_number(self):
        digits = list(range(10))
        random.shuffle(digits)
        target_number = "".join(str(digit) for digit in digits[:3])
        return int(target_number)
    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Hit and Blow Game!")
        self.label.pack()
        self.entry_label = tk.Label(self, text="Enter a three-digit number:")
        self.entry_label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack()
        self.remaining_attempts_label = tk.Label(self, text=f"Remaining attempts: {self.max_attempts}")
        self.remaining_attempts_label.pack()
    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit() or len(guess) != 3:
            self.label.config(text="Invalid input! Please enter a three-digit number.")
            return
        if len(set(guess)) != 3 or guess[0] == guess[1] or guess[1] == guess[2] or guess[0] == guess[2]:
            self.label.config(text="Invalid input! Please enter a three-digit number with different digits.")
            return
        guess = [int(digit) for digit in guess]
        self.attempts += 1
        hits = 0
        blows = 0
        matched_indices = []
        guess_digit_count = [0] * 10
        target_digit_count = [0] * 10
        for i in range(3):
            if guess[i] == self.target_number[i]:
                hits += 1
                matched_indices.append(i)
            guess_digit_count[guess[i]] += 1
            target_digit_count[self.target_number[i]] += 1
        for i in range(3):
            if i not in matched_indices:
                blows += min(guess_digit_count[guess[i]], target_digit_count[guess[i]])
                target_digit_count[guess[i]] = 0  # Reset the count in target_digit_count to avoid counting it again
                guess_digit_count[guess[i]] = 0  # Reset the count in guess_digit_count to avoid counting it again
        if hits == 3 and self.attempts <= self.max_attempts // 2:
            self.label.config(text="You answered correctly halfway through. Game over!")
            self.submit_button.config(state=tk.DISABLED)
            return
        if hits == 3:
            self.label.config(text="Congratulations! You guessed the number correctly.")
            self.submit_button.config(state=tk.DISABLED)
            return
        self.label.config(text=f"Hits: {hits}, Blows: {blows}")
        self.remaining_attempts_label.config(text=f"Remaining attempts: {self.max_attempts - self.attempts}")
        if self.attempts >= self.max_attempts:
            self.label.config(text=f"Game over! The target number was {self.target_number}.")
            self.submit_button.config(state=tk.DISABLED)