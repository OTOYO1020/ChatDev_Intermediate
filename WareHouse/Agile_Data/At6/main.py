'''
This is the main file of the software. It contains the entry point of the program and handles the GUI initialization.
'''
import tkinter as tk
from controller import Controller
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Software Name")
        self.geometry("800x600")
        self.create_widgets()
    def create_widgets(self):
        controller = Controller(self)
        controller.gui.create_widgets()
if __name__ == "__main__":
    app = Application()
    app.mainloop()