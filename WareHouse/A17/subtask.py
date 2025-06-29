'''
This file contains the Subtask class.
'''
import tkinter as tk
from tkinter import simpledialog, messagebox
import random
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Default subtask details")
        self.label.pack()
        self.button = tk.Button(self, text="Click Me", command=self.button_click)
        self.button.pack()
        self.pack()
    def start_game(self):
        self.generated_number = self.generate_number()
        self.remaining_lives = 7
        self.hit_count = 0
        self.blow_count = 0
        self.update_label()
    def generate_number(self):
        digits = random.sample(range(1, 10), 3)
        return "".join(str(d) for d in digits)
    def validate_input(self, guess):
        if len(guess) != 3 or not guess.isdigit():
            return False
        if len(set(guess)) != 3:
            return False
        return True
    def check_guess(self, guess):
        self.hit_count = 0
        self.blow_count = 0
        for i in range(3):
            if guess[i] == self.generated_number[i]:
                self.hit_count += 1
            elif guess[i] in self.generated_number and guess[i] != self.generated_number[i]:
                self.blow_count += 1
        if self.hit_count == 3:
            self.label.config(text="Congratulations! You guessed the number.")
            return  # Exit the method if the user guessed the number correctly
        if self.remaining_lives == 0:
            self.label.config(text="Game Over. The number was: " + self.generated_number)
        else:
            self.remaining_lives -= 1
            self.update_label()
    def update_label(self):
        self.label.config(text=f"Hits: {self.hit_count}, Blows: {self.blow_count}, Lives: {self.remaining_lives}")
    def button_click(self):
        if self.remaining_lives == 0 or self.hit_count == 3:
            return
        guess = simpledialog.askstring("Guess", "Enter a three-digit number:")
        if guess is not None:
            if self.validate_input(guess):
                self.check_guess(guess)
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid three-digit number with different digits.")