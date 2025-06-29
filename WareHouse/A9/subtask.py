'''
This file contains the Subtask class.
'''
import tkinter as tk
from tkinter import simpledialog, messagebox
import random
class Subtask(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Default subtask details")
        self.label.pack()
        self.button = tk.Button(self, text="Click Me", command=self.button_click)
        self.button.pack()
        self.pack()
        self.random_number = self.generate_random_number()
        self.remaining_lives = 7
        self.previous_guesses = []
    def generate_random_number(self):
        digits = random.sample(range(1, 10), 3)
        return "".join(str(digit) for digit in digits)
    def validate_input(self, user_input):
        if len(user_input) != 3 or not user_input.isdigit():
            return False
        if len(set(user_input)) != 3:
            return False
        return True
    def check_hits_and_blows(self, user_input):
        hits = 0
        blows = 0
        for i in range(3):
            if int(user_input[i]) == int(self.random_number[i]):
                hits += 1
            elif int(user_input[i]) in map(int, self.random_number):
                blows += 1
        return hits, blows
    def button_click(self):
        user_input = simpledialog.askstring("Input", "Enter a three-digit number:")
        if not self.validate_input(user_input):
            messagebox.showerror("Error", "Invalid input. Please enter a three-digit number with different digits.")
            return
        if user_input in self.previous_guesses:
            messagebox.showerror("Error", "Duplicate guess. Please enter a different guess.")
            return
        hits, blows = self.check_hits_and_blows(user_input)
        self.previous_guesses.append(user_input)
        if hits == 3:
            messagebox.showinfo("Result", "Congratulations! You guessed the number correctly.")
            self.destroy()
            return
        self.remaining_lives -= 1
        remaining_lives_text = f"Hits: {hits}, Blows: {blows}, Remaining Lives: {self.remaining_lives}"
        self.label.config(text=remaining_lives_text)
        messagebox.showinfo("Result", remaining_lives_text)
        if self.remaining_lives == 0:
            messagebox.showinfo("Result", f"Game over. The number was {self.random_number}.")
            self.destroy()