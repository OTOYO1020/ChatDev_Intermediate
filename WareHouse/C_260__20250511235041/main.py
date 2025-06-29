'''
This is the main entry point for the Gomoku game application.
'''
from gomoku_gui import GomokuGUI  # Import the GUI class
import tkinter as tk  # Import tkinter for GUI
def main():
    root = tk.Tk()  # Create the main window
    game_gui = GomokuGUI(root)  # Create an instance of the GomokuGUI
    root.mainloop()  # Start the GUI event loop
if __name__ == "__main__":
    main()