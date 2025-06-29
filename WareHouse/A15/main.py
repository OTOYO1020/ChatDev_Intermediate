'''
This file contains the main function to start the Hit and Blow game.
'''
import tkinter as tk
from subtask import Subtask
def main():
    root = tk.Tk()
    app = Subtask(root)
    root.mainloop()
if __name__ == "__main__":
    main()