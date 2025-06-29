'''
This is the main entry point of the Gomoku game application.
'''
import tkinter as tk  # Import tkinter for GUI components
from gomoku_gui import GomokuGUI  # Import the GUI class
def main():
    root = tk.Tk()  # Create the main window
    app = GomokuGUI(root)  # Initialize the Gomoku GUI
    root.mainloop()  # Start the GUI event loop
if __name__ == "__main__":
    main()