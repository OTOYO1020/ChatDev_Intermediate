'''
This is the main file of the application.
'''
import tkinter as tk
from subtask import Subtask
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hit and Blow Game")
        self.geometry("400x350")
        self.subtask = Subtask()
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self, text="Enter a three-digit number:")
        self.label.pack()
        self.entry = tk.Entry(self, width=50)
        self.entry.pack()
        self.button = tk.Button(self, text="Submit", command=self.submit_guess)
        self.button.pack()
        self.remaining_lives_label = tk.Label(self, text="Remaining Lives: 7")
        self.remaining_lives_label.pack()
    def submit_guess(self):
        guess = self.entry.get()
        if not self.subtask.is_valid_guess(guess):
            self.display_result("Invalid input. Please enter a valid three-digit number.")
            return  # Exit the method without decreasing the remaining lives
        is_correct, result = self.subtask.check_guess(guess)
        self.display_result(result)
        self.update_remaining_lives()
        if is_correct:
            self.end_game()
    def display_result(self, result):
        result_label = tk.Label(self, text=result)
        result_label.pack()
    def update_remaining_lives(self):
        remaining_lives = self.subtask.get_remaining_lives()
        self.remaining_lives_label.config(text=f"Remaining Lives: {remaining_lives}")
    def end_game(self):
        self.button.config(state=tk.DISABLED)  # Disable the submit button
        self.entry.config(state=tk.DISABLED)  # Disable the input field
        target_label = tk.Label(self, text=f"The target number was {self.subtask.target_number}.")
        target_label.pack()
if __name__ == "__main__":
    app = Application()
    app.mainloop()