'''
This file contains the Subtask class.
'''
import tkinter as tk
import random
class Subtask(tk.Frame):
    def __init__(self, master, end_game_callback):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.generate_number()
        self.remaining_lives = 7
        self.end_game_callback = end_game_callback
    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Hit and Blow Game!")
        self.label.pack()
        self.input_label = tk.Label(self, text="Enter a three-digit number:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self)
        self.input_entry.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
        self.remaining_lives_label = tk.Label(self, text=f"Remaining Lives: {self.remaining_lives}")
        self.remaining_lives_label.pack()
    def generate_number(self):
        self.generated_number = ''.join(random.sample('123456789', 3))
    def check_guess(self):
        guess = self.input_entry.get()
        # Validate the input
        if not guess.isdigit() or len(guess) != 3 or len(set(guess)) != 3:
            self.result_label.config(text="Invalid input. Please enter a three-digit number with different digits.")
            return
        # Decrement the remaining lives count and update the label
        self.remaining_lives -= 1
        self.remaining_lives_label.config(text=f"Remaining Lives: {self.remaining_lives}")
        # Compare the guess with the generated number
        hits = 0
        blows = 0
        for i in range(3):
            if int(guess[i]) == int(self.generated_number[i]):
                hits += 1
            elif int(guess[i]) in map(int, self.generated_number):
                blows += 1
        # Update the result label
        if hits == 3:
            self.result_label.config(text="Congratulations! You guessed the number correctly.")
            self.submit_button.config(state=tk.DISABLED)
            if self.remaining_lives <= 7 // 2:
                self.end_game_callback()
        else:
            self.result_label.config(text=f"Hits: {hits}, Blows: {blows}")
        # Check if the game is over
        if self.remaining_lives == 0:
            self.result_label.config(text=f"Game Over. The number was {self.generated_number}.")
            self.submit_button.config(state=tk.DISABLED)
        # Clear the input entry
        self.input_entry.delete(0, tk.END)
    def end_game(self):
        self.master.destroy()