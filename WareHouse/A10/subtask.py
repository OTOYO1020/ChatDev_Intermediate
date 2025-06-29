'''
This file contains the Subtask class which represents the GUI for the subtask details.
'''
import tkinter as tk
from tkinter import messagebox
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
        self.random_number = self.generate_random_number()
        self.hits = 0
        self.blows = 0
    def generate_random_number(self):
        digits = random.sample(range(1, 10), 3)
        return int("".join(map(str, digits)))
    def start_game(self):
        guess = self.entry.get()
        if not guess.isdigit() or len(guess) != 3 or len(set(guess)) != 3:
            self.display_message("Invalid input. Please enter a three-digit number with different digits.")
            return
        self.hits, self.blows = self.calculate_hits_and_blows(guess)
        if self.hits == 3:
            self.display_message("Congratulations! You won the game.")
            return
        if self.remaining_lives == 1:
            self.display_message(f"Game over. The correct number was {self.random_number}.")
        else:
            self.remaining_lives -= 1
            self.display_message(f"Hits: {self.hits}, Blows: {self.blows}, Remaining Lives: {self.remaining_lives}")
    def calculate_hits_and_blows(self, guess):
        hits = 0
        blows = 0
        for i in range(3):
            if guess[i] == str(self.random_number)[i]:
                hits += 1
            elif guess[i] in str(self.random_number):
                blows += 1
        return hits, blows
    def display_message(self, message):
        messagebox.showinfo("Message", message)
        self.entry.delete(0, tk.END)
        self.entry.focus_set()