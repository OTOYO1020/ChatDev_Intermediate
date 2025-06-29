'''
This is the main file of the application. It contains the entry point and the main GUI class.
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
        self.label.pack(pady=20)
        self.input_label = tk.Label(self, text="Enter a three-digit number:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self)
        self.input_entry.pack(pady=10)
        self.button = tk.Button(self, text="Guess", command=self.button_click)
        self.button.pack(pady=10)
        self.lives_label = tk.Label(self, text=f"Lives: {self.game.lives}")
        self.lives_label.pack()
    def button_click(self):
        user_input = self.input_entry.get()
        result = self.game.check_guess(user_input)
        if result == "win":
            self.label.config(text="Congratulations! You guessed the number correctly!")
            self.button.config(state=tk.DISABLED)
        elif result == "lose":
            self.label.config(text=f"Game Over! The number was {self.game.number}.")
            self.button.config(state=tk.DISABLED)
        elif result == "invalid":
            self.label.config(text="Invalid input. Please enter a three-digit number with different digits.")
        else:
            self.label.config(text=f"Hits: {result['hits']}, Blows: {result['blows']}")
            if result['hits'] == 3:
                self.label.config(text="Congratulations! You guessed the number correctly!")
                self.button.config(state=tk.DISABLED)
            elif self.game.lives == 0:
                self.label.config(text=f"Game Over! The number was {self.game.number}.")
                self.button.config(state=tk.DISABLED)
            else:
                self.lives_label.config(text=f"Lives: {self.game.lives}")
        self.input_entry.delete(0, tk.END)
if __name__ == "__main__":
    app = Application()
    app.mainloop()