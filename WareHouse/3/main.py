'''
This file contains the Application class.
'''
import tkinter as tk
from hit_and_blow_game import HitAndBlowGame
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hit and Blow Game")
        self.geometry("400x300")
        self.game = HitAndBlowGame()
        self.create_widgets()
        self.mainloop()
    def create_widgets(self):
        self.label = tk.Label(self, text="Enter a three-digit number:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Submit", command=self.button_click)
        self.button.pack()
    def button_click(self):
        guess = self.entry.get()
        result = self.game.check_guess(guess)
        self.label.config(text=result)
        self.entry.delete(0, tk.END)
        if result.startswith("Congratulations!") or result.startswith("Game Over"):
            self.button.config(state=tk.DISABLED)
if __name__ == "__main__":
    app = Application()