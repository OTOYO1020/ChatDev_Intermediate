'''
This is the main file of the application. It serves as the entry point and contains the GUI implementation.
'''
import tkinter as tk
from game import HitAndBlowGame
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hit and Blow Game")
        self.geometry("400x300")
        self.game = HitAndBlowGame()
        self.label = tk.Label(self, text="Welcome to Hit and Blow Game!")
        self.label.pack()
        self.input_label = tk.Label(self, text="Enter a three-digit number:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self)
        self.input_entry.pack()
        self.button = tk.Button(self, text="Guess", command=self.button_click)
        self.button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
        self.remaining_lives_label = tk.Label(self, text="Remaining Lives: 7")
        self.remaining_lives_label.pack()
    def button_click(self):
        guess = self.input_entry.get()
        if len(guess) != 3 or not guess.isdigit():
            self.result_label.config(text="Invalid input. Please enter a three-digit number.")
            return
        result = self.game.check_guess(guess)
        self.result_label.config(text=f"Hits: {result['hits']}, Blows: {result['blows']}")
        if result['game_over']:
            if result['hits'] == 3:
                self.result_label.config(text="Congratulations! You guessed the number correctly.")
            else:
                self.result_label.config(text=f"Game Over. The number was {self.game.get_number()}.")
            self.button.config(state=tk.DISABLED)
        else:
            self.game.reduce_life()
            remaining_lives = self.game.get_remaining_lives()
            self.remaining_lives_label.config(text=f"Remaining Lives: {remaining_lives}")
            if remaining_lives == 0:
                self.result_label.config(text=f"Game Over. The number was {self.game.get_number()}.")
                self.button.config(state=tk.DISABLED)
        self.input_entry.delete(0, tk.END)
if __name__ == "__main__":
    app = Application()
    app.mainloop()