'''
This is the main file of the application.
'''
import tkinter as tk
from subtask import Subtask
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application")
        self.geometry("400x300")
        self.subtask = Subtask(self, self.end_game)
        self.mainloop()
    def end_game(self):
        self.subtask.end_game()
if __name__ == "__main__":
    app = Application()