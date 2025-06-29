'''
Main entry point for the Gomoku game application.
'''
import tkinter as tk  # Import tkinter for GUI
from gui import GomokuGUI  # Import the GUI class
def main():
    root = tk.Tk()  # Create the main window
    game_gui = GomokuGUI(root)  # Initialize the GUI
    root.mainloop()  # Start the GUI event loop
if __name__ == "__main__":
    main()