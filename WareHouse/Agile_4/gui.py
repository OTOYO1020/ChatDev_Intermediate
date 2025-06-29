import tkinter as tk
from logic import GameLogic
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hit and Blow Game")
        self.geometry("400x300")
        self.data = GameLogic()
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self, text="Enter a three-digit number:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Submit", command=self.check_guess)
        self.button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
    def check_guess(self):
        guess = self.entry.get()
        result, message = self.data.check_guess(guess)
        self.result_label.config(text=message)
        if result:
            self.button.config(state="disabled")
            self.entry.config(state="disabled")