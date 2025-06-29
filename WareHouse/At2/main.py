'''
This is the main file of the web application.
'''
import tkinter as tk
from subtask import Subtask
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Web Application")
        self.geometry("400x300")
        self.subtask = None
        self.create_widgets()
    def create_widgets(self):
        self.subtask_button = tk.Button(self, text="Open Subtask", command=self.open_subtask)
        self.subtask_button.pack(pady=10)
    def open_subtask(self):
        if self.subtask is None:
            self.subtask = Subtask(self)
        self.subtask.show()
if __name__ == "__main__":
    app = Application()
    app.mainloop()