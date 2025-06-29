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
        self.create_widgets()
        self.mainloop()
    def create_widgets(self):
        self.subtask.pack()
if __name__ == "__main__":
    app = Application()