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
        self.subtask = Subtask(self)
        self.subtask.pack()
    def start(self):
        self.subtask.start_game()
        self.mainloop()
if __name__ == "__main__":
    app = Application()
    app.start()