'''
This is the main file of the application. It serves as the entry point and contains the main function to start the application.
'''
import random
import tkinter as tk
from tkinter import messagebox
from collections import Counter
class HitAndBlowGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hit and Blow Game")
        self.geometry("400x300")
        self.remaining_lives = 7
        self.target_number = self.generate_target_number()
        self.create_widgets()
    def generate_target_number(self):
        digits = random.sample(range(10), 3)
        return "".join(map(str, digits))
    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Hit and Blow Game!")
        self.label.pack(pady=20)
        self.remaining_lives_label = tk.Label(self, text=f"Remaining Lives: {self.remaining_lives}")
        self.remaining_lives_label.pack()
        self.input_entry = tk.Entry(self)
        self.input_entry.pack(pady=10)
        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)
    def check_guess(self):
        guess = self.input_entry.get()
        hits, blows = self.calculate_hits_and_blows(guess)
        if not self.is_valid_guess(guess):
            messagebox.showerror("Invalid Input", "Please enter a valid three-digit number.")
            self.input_entry.delete(0, tk.END)  # Clear the input entry field
            return
        messagebox.showinfo("Result", f"Hits: {hits}, Blows: {blows}")
        if hits == len(self.target_number):
            messagebox.showinfo("Congratulations", "You guessed the number correctly!")
            self.destroy()
        else:
            if self.remaining_lives > 0:
                self.remaining_lives -= 1
                self.remaining_lives_label.config(text=f"Remaining Lives: {self.remaining_lives}")
            else:
                messagebox.showinfo("Game Over", f"You ran out of lives. The target number was {self.target_number}.")
                self.destroy()
        self.input_entry.delete(0, tk.END)
    def is_valid_guess(self, guess):
        if not guess.isdigit() or len(guess) != 3:
            return False
        digit_counts = Counter(guess)
        return all(count == 1 for count in digit_counts.values()) and len(digit_counts) == 3
    def calculate_hits_and_blows(self, guess):
        hits = 0
        blows = 0
        target_counts = Counter(self.target_number)
        for i, digit in enumerate(guess):
            if digit == self.target_number[i]:
                hits += 1
                target_counts[digit] -= 1
            elif digit in target_counts and target_counts[digit] > 0:
                blows += 1
                target_counts[digit] -= 1
        return hits, blows
def main():
    game = HitAndBlowGame()
    game.mainloop()
if __name__ == "__main__":
    main()