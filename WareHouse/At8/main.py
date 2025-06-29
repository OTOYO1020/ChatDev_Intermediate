'''
This is the main file of the software. It contains the entry point of the program and handles the GUI initialization.
'''
import tkinter as tk
from gui import MainWindow
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Software Name")
        self.geometry("800x600")
        # Create and configure GUI elements here
        main_window = MainWindow(self)
        main_window.pack()
        self.mainloop()
if __name__ == "__main__":
    app = Application()
    app.mainloop()