'''
This is the main file of the application. It contains the entry point and the GUI implementation.
'''
import tkinter as tk
from game import Game
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hit and Blow Game")
        self.geometry("400x300")
        self.game = Game()
        self.label = tk.Label(self, text="Welcome to the Hit and Blow Game!")
        self.label.pack(pady=20)
        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)
        self.button = tk.Button(self, text="Guess", command=self.button_click)
        self.button.pack(pady=10)
        self.remaining_lives_label = tk.Label(self, text=f"Remaining Lives: {self.game.remaining_lives}")
        self.remaining_lives_label.pack(pady=10)
    def button_click(self):
        guess = self.entry.get()
        result = self.game.make_guess(guess)
        if result == "win":
            self.label.config(text="Congratulations! You guessed the number correctly!")
            self.button.config(state=tk.DISABLED)
        elif result == "lose":
            self.label.config(text=f"Game Over! The number was {self.game.number}")
            self.button.config(state=tk.DISABLED)
        else:
            self.label.config(text=result)
        self.remaining_lives_label.config(text=f"Remaining Lives: {self.game.remaining_lives}")
        self.entry.delete(0, tk.END)
if __name__ == "__main__":
    app = Application()
    app.mainloop()