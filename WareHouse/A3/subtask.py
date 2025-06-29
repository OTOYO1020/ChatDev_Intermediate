'''
This file contains the Subtask class.
'''
import tkinter as tk
from random import randint
class Subtask(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.generate_number()
        self.remaining_lives = 7
    def create_widgets(self):
        self.label = tk.Label(self, text="Enter a three-digit number:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Submit", command=self.check_number)
        self.button.pack()
        self.remaining_lives_label = tk.Label(self, text=f"Remaining Lives: {self.remaining_lives}")
        self.remaining_lives_label.pack()
    def generate_number(self):
        self.target_number = str(randint(100, 999))
        print(f"Target Number: {self.target_number}")
    def check_number(self):
        user_input = self.entry.get()
        try:
            number = int(user_input)
            if len(user_input) != 3 or len(set(user_input)) != 3:
                raise ValueError
        except ValueError:
            self.label.config(text="Invalid input. Enter a valid three-digit number.")
            return
        if number == int(self.target_number):
            self.end_game()
            return
        self.remaining_lives -= 1
        self.remaining_lives_label.config(text=f"Remaining Lives: {self.remaining_lives}")
        hits = 0
        blows = 0
        for i in range(3):
            if user_input[i] == self.target_number[i]:
                hits += 1
            elif user_input[i] in self.target_number:
                blows += 1
        self.label.config(text=f"Hits: {hits}, Blows: {blows}")
        if hits == 3 and blows == 0 or self.remaining_lives == 0:
            self.end_game()
    def end_game(self):
        if self.remaining_lives > 0:
            self.label.config(text="Congratulations! You guessed the number.")
        else:
            self.label.config(text=f"Game Over. The number was {self.target_number}.")
        self.button.config(state=tk.DISABLED)