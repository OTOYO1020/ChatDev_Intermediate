'''
This file contains the Subtask class.
'''
import tkinter as tk
import random
class Subtask(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.label = tk.Label(self, text="Default subtask details")
        self.label.pack()
        self.button = tk.Button(self, text="Click Me", command=self.start_game)
        self.button.pack()
        self.pack()
    def start_game(self):
        self.label.config(text="Game started!")
        self.button.config(state=tk.DISABLED)
        self.remaining_lives = 7
        self.target_number = self.generate_target_number()
        self.display_remaining_lives()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.button_click)
        self.submit_button.pack()
    def generate_target_number(self):
        digits = list(range(10))
        random.shuffle(digits)
        target_number = "".join(map(str, digits[:3]))
        return target_number
    def display_remaining_lives(self):
        lives_text = f"Remaining Lives: {self.remaining_lives}"
        self.remaining_lives_label = tk.Label(self, text=lives_text)
        self.remaining_lives_label.pack()
    def button_click(self):
        user_input = self.entry.get()
        if self.validate_input(user_input):
            self.check_guess(user_input)
        else:
            self.label.config(text="Invalid input. Please enter a three-digit number with different digits.")
    def validate_input(self, user_input):
        if len(user_input) != 3:
            return False
        if len(set(user_input)) != 3 or len(user_input) != len(set(user_input)):
            return False
        return True
    def check_guess(self, user_input):
        user_input = list(map(int, user_input))
        hits = 0
        blows = 0
        hits_digits = set()
        for i in range(3):
            if user_input[i] == int(self.target_number[i]):
                hits += 1
                hits_digits.add(user_input[i])
        for i in range(3):
            if user_input[i] != int(self.target_number[i]) and user_input[i] in map(int, self.target_number) and user_input[i] not in hits_digits:
                blows += 1
        self.remaining_lives -= 1
        self.display_remaining_lives()
        if hits == 3:
            if self.remaining_lives == 7 // 2:  # Check if user guessed correctly halfway through
                self.remaining_lives = 7 // 2 + 1  # Set remaining lives to half of the total number of lives allowed in the game
                self.label.config(text="Congratulations! You guessed the number correctly halfway through.")
            else:
                self.label.config(text="Congratulations! You guessed the number correctly.")
            self.submit_button.config(state=tk.DISABLED)
            return  # Exit the method if the user has guessed correctly
        elif hits < 3 and self.remaining_lives == 0:
            self.label.config(text=f"Game over! The target number was {self.target_number}.")
            self.submit_button.config(state=tk.DISABLED)
        elif hits < 3:
            result_text = f"Hits: {hits}, Blows: {blows}"
            self.label.config(text=result_text)
        self.entry.delete(0, tk.END)