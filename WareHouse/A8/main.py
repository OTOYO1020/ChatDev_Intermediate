'''
This is the main file of the application. It contains the entry point of the program and handles the GUI initialization.
'''
import tkinter as tk
from gui import MainWindow
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hit and Blow Game")
        self.geometry("400x300")
        self.create_widgets()
    def create_widgets(self):
        main_window = MainWindow(self)
        main_window.pack()
if __name__ == "__main__":
    app = Application()
    app.mainloop()