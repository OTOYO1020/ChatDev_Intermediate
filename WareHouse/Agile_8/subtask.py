'''
This file contains the Subtask class.
'''
import tkinter as tk
from tkinter import messagebox
import random
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.remaining_lives = 7
        self.generated_number = self.generate_number()
        self.label = tk.Label(self, text=f"Remaining Lives: {self.remaining_lives}")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Submit", command=self.check_guess)
        self.button.pack()
    def generate_number(self):
        digits = random.sample(range(10), 3)
        return "".join(map(str, digits))
    def start_game(self):
        self.remaining_lives = 7
        self.generated_number = self.generate_number()
        self.label.config(text=f"Remaining Lives: {self.remaining_lives}")
    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit() or len(guess) != 3:
            messagebox.showerror("Invalid Input", "Please enter a three-digit number.")
            return
        if len(set(guess)) != 3:
            messagebox.showerror("Invalid Input", "Please enter a number with different digits.")
            return
        hits = sum(1 for g, n in zip(guess, self.generated_number) if g == n)
        blows = sum(1 for digit in guess if digit in self.generated_number and guess.count(digit) != self.generated_number.count(digit))
        if hits == len(guess):
            messagebox.showinfo("Game Over", "Congratulations! You guessed the number correctly.")
            self.master.destroy()
        else:
            if self.remaining_lives == 1:
                messagebox.showinfo("Game Over", f"Game Over! The number was {self.generated_number}.")
                self.master.destroy()
            else:
                self.remaining_lives -= 1
                self.label.config(text=f"Remaining Lives: {self.remaining_lives}")
                messagebox.showinfo("Guess Result", f"Hits: {hits}, Blows: {blows}")
                self.entry.delete(0, tk.END)