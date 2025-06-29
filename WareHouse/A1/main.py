'''
This is the main file of the application.
'''
import tkinter as tk
from hit_blow_game import HitBlowGame
from subtask import Subtask
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hit and Blow Game")
        self.geometry("400x300")
        self.hit_blow_game = HitBlowGame()
        self.subtask = Subtask()
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self, text="Enter a three-digit number:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Submit", command=self.submit_guess)
        self.button.pack()
    def submit_guess(self):
        guess = self.entry.get()
        result = self.hit_blow_game.check_guess(guess)
        self.label.config(text=result)
        self.entry.delete(0, tk.END)
        if result == "Congratulations! You guessed the number correctly." or result == "Halfway through. You guessed the number correctly.":
            self.button.config(state=tk.DISABLED)
            self.subtask.set_task_description("Game Over")
            self.subtask.execute()
if __name__ == "__main__":
    app = Application()
    app.mainloop()